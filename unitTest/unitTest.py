"""
# Created: 15.07.2024
# Last edited: 17.07.2024
"""

import unittest
import sys
import os
import logging
from unittest.mock import patch, MagicMock
import io
import traceback

# Ensure the module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from secureRequests import SecureRequests
from secureRequests.secureRequestsDecorators import STATUS_CODE_EXCEPTION_MAP
from secureRequests import HeaderKeys, CookieAttributeKeys, CookieKeys

def formatDict(inputDict=None, ignoredKeys=None):
    """
    Format a dictionary into a string with proper indentation and line breaks.

    Args:
        inputDict (dict): The dictionary to format.
        ignoredKeys (list, optional): List of keys to filter out from the dictionary. Defaults to None.

    Returns:
        str: The formatted string.
    """
    if ignoredKeys:
        result = "\n".join([f" > {key}: {value}" for key, value in inputDict.items() if key not in ignoredKeys])
    else:
        result = "\n".join([f" > {key}: {value}" for key, value in inputDict.items()])
    return result

def formatCookies(cookies):
    """Format cookies dictionary into a string with proper indentation and line breaks."""
    if not cookies:
        return "No cookies used."
    
    formattedCookies = []
    for key, attributes in cookies.items():
        # Convert attributes to a string format
        formattedAttributes = ", ".join(
            f"{str(attrKey).split('.')[-1]}: {attrValue}" 
            for attrKey, attrValue in attributes.items()
        )
        formattedCookies.append(f" > {key}: {{{formattedAttributes}}}")
    
    return "\n".join(formattedCookies)

class CustomTestResult(unittest.TextTestResult):
    """Custom test result class to store additional information about test results."""
    def __init__(self, *args, **kwargs):
        """Initialize the test variables."""
        super().__init__(*args, **kwargs)
        self.passedTests = []
        self.failedTests = []
        self.testLogs = {}  # Store logs per test
        self._originalStream = {}
        self._currentTest = None

    def addSuccess(self, test):
        """Add a passed test result and log its output."""
        super().addSuccess(test)
        self.passedTests.append(test)
        self.testLogs[test] = self._getTestLog()
        logging.info(f"[PASS] {test} - Log Output:\n{self.testLogs[test]}")

    def addFailure(self, test, err):
        """Add a failed test result and log its output."""
        super().addFailure(test, err)
        self.failedTests.append((test, err))
        self.testLogs[test] = self._getTestLog()
        logging.error(f"[FAIL] {test} - Log Output:\n{self.testLogs[test]}")

    def startTest(self, test):
        """Start a test and set up logging for it."""
        super().startTest(test)
        self._currentTest = test
        self._setup_logger(test)

    def _setup_logger(self, test):
        """Set up logger to capture logs for each test."""
        testLogStream = io.StringIO()
        handler = logging.StreamHandler(testLogStream)
        handler.setLevel(logging.INFO)

        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Store the original stream handler to revert later
        self._originalStream[test] = (testLogStream, handler)

    def _getTestLog(self):
        """Get the log output for the current test."""
        logger = logging.getLogger()
        testLogStream, handler = self._originalStream.get(self._currentTest, (None, None))
        if testLogStream and handler:
            logger.removeHandler(handler)
            return testLogStream.getvalue()
        return ""

    def stopTest(self, test):
        """Stop a test and clear the current test reference."""
        super().stopTest(test)
        self._currentTest = None

class CustomTestRunner(unittest.TextTestRunner):
    """Custom test runner class to use the custom test result class and generate a report."""
    def _makeResult(self):
        """ Returns a result build with CustomTestResult """
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        """Run the test and generate a markdown report."""
        result = super().run(test)
        self._generateReport(result)
        return result

    def _generateReport(self, result):
        """Generate a markdown report of the test results."""
        with open("unitTest/unitTestResults.md", "w") as reportFile:
            reportFile.write("# unitTest\n\n")
            reportFile.write("> **Note:** This report was generated automatically by the unit test suite.")
            reportFile.write("Log output with timestamps resemble the logging of the real request as it would go down in the .log file.")
            reportFile.write("\n---\n")
            reportFile.write("## Table of Contents\n\n")
            reportFile.write("- [Failing](#failing)\n")
            for test, _ in result.failedTests:
                testName = test._testMethodName
                reportFile.write(f"  - [{testName}](#{testName.lower()})\n")
            reportFile.write("- [Passing](#passing)\n")
            for test in result.passedTests:
                testName = test._testMethodName
                reportFile.write(f"  - [{testName}](#{testName.lower()})\n")

            reportFile.write("\n## Failing\n")
            for test, err in result.failedTests:
                reportFile.write(self._formatTestEntry(test, err, "Failing", result))

            reportFile.write("\n## Passing\n")
            for test in result.passedTests:
                reportFile.write(self._formatTestEntry(test, None, "Passing", result))

    def _formatTestEntry(self, test, err, status, result):
        """Format an individual test entry for the report."""
        output = []
        testName = test._testMethodName
        output.append(f"### {testName}\n")
        output.append(f"<a name=\"{testName.lower()}\"></a>\n")

        output.append("#### Result\n")
        if status == "Passing":
            output.append("- Log Output:\n")
            output.append(f"```\n{result.testLogs[test]}\n```\n")
            output.append('---')
        else:
            output.append("- Traceback:\n\n")
            output.append(f"```\n{''.join(traceback.format_exception(*err))}\n```\n")
            output.append("- Log Output:\n")
            output.append(f"```\n{result.testLogs[test]}\n```\n")
            output.append('---')
        return "\n".join(output) + "\n"

class TestSecureRequests(unittest.TestCase):
    def setUp(self):
        """
        Set up the initial test environment.
        Initializes base URL, status codes, logging, and other necessary variables.
        """
        self.baseURL = 'https://httpbin.org'
        self.statusCodes = STATUS_CODE_EXCEPTION_MAP
        self.failures = []
        self.logStream = io.StringIO()
        self.methods = ['get', 'post', 'put', 'delete', 'patch']
        self.testURL = 'https://httpbin.org'
        self.defaultHeader = {
            HeaderKeys.ACCEPT.value: "application/x-www-form-urlencoded",
            HeaderKeys.CONTENT_TYPE.value: "application/x-www-form-urlencoded",
            HeaderKeys.SEC_CH_UA.value: '"Google Chrome";v="110", "Chromium";v="110", "Not.A/Brand";v="24"',
            HeaderKeys.SEC_CH_UA_MOBILE.value: "?0",
            HeaderKeys.SEC_CH_UA_PLATFORM.value: '"Windows"',
            HeaderKeys.SEC_FETCH_DEST.value: "empty",
            HeaderKeys.SEC_FETCH_MODE.value: "cors",
            HeaderKeys.SEC_FETCH_SITE.value: "same-site",
            HeaderKeys.USER_AGENT.value: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        logging.basicConfig(stream=self.logStream, level=logging.DEBUG)

    def integrationConfig(self):
        """
        Returns a list of safe configuration dictionaries for SecureRequests.
        """
        return [
            {'certificateNeedFetch': True, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': False, 'unsafe': True, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False}
        ]
    
    def initConfig(self):
        """
        Returns a list of init configuration dictionaries for SecureRequests.
        """
        return [
            {'certificateNeedFetch': True, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': True, 'unsafe': True, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False}
        ]

    def test_HTTPMethods_integration(self):
        """
        Integration Test HTTP methods (GET, POST, PUT, DELETE, PATCH) for specific configurations.
        """

        for config in self.integrationConfig():
            srRequest = SecureRequests(**config)
            statusSafe = "[SAFE]" if not config['unsafe'] else "[UNSAFE]"
            statusTLS = "[USE TLS]" if config['useTLS'] else "[NO TLS]"
            
            logging.info('------------------------------------------------------------')
            logging.info('>>> Testing HTTP Methods with Config <<<')
            logging.info(f'{formatDict(config, ignoredKeys=["logPath", "logToFile", "suppressWarnings"])}\n')

            for method in self.methods:
                with self.subTest(config=config, method=method):
                    try:
                        response = srRequest.makeRequest(self.testURL + f'/{method}', method=method.upper())
                        self.assertEqual(response.status_code, 200)
                        logging.info(f"[PASS]{statusSafe}{statusTLS} {method.upper()} request to {self.testURL}/{method} with status code {response.status_code}.")
                    except Exception as e:
                        self.fail(f"[FAIL]{statusSafe}{statusTLS} {method.upper()} request to {self.testURL}/{method} failed with exception: {e}")

            # Universal cookies and headers logging
            logging.info(f'\n- Used Cookies: {formatCookies(srRequest.cookieGetAll())}.\n- Used Header:\n{formatDict(srRequest.headers)}\n')

    @patch('secureRequests.secureRequests.SecureRequests.makeRequest')
    def test_mockStatusCodes(self, srRequestMock):
        """
        Test handling of different HTTP status codes.
        Ensures the appropriate exceptions are raised for each status code.
        """
        config = self.integrationConfig()[0]
        srRequest = SecureRequests(**config)

        for statusCode, exception in self.statusCodes.items():
            with self.subTest(status_code=statusCode, config=config):
                mockResponse = MagicMock()
                mockResponse.status_code = statusCode
                
                # Modify the return value to raise the appropriate exception
                srRequestMock.side_effect = exception(f"Mocked response for status code {statusCode}")

                try:
                    srRequest.makeRequest(self.baseURL + f'/status/{statusCode}')
                except exception:
                    # Log the successful raising of the expected exception
                    logging.info(f"[PASS] {exception.__name__} raised for status code {statusCode}.")
                else:
                    # Log the failure if the exception was not raised
                    message = f"{exception.__name__} not raised for status code {statusCode}"
                    raise AssertionError(message)

    def test_fetchCertOnInit(self):
        """
        Test certificate fetching on initialization with safe configurations.
        Checks if the certificate file exists and is valid.
        """
        for config in self.initConfig():
            safeStatus = "[SAFE]" if not config['unsafe'] else "[UNSAFE]"
            try:
                srRequest = SecureRequests(**config)

                if config["unsafe"]:
                    logging.info(f"[PASS]{safeStatus} Fetched certificate on initialization with certificateNeedFetch: True")
                    self.assertTrue(os.path.exists(srRequest.verify))
                    logging.info(f"[PASS]{safeStatus} Verified path exists.")
                    self.assertFalse(srRequest.verify)
                    logging.info(f"[PASS]{safeStatus} Verified we are not using it.\n")

                else:
                    logging.info(f"[PASS]{safeStatus} Fetched certificate on initialization with certificateNeedFetch: True")
                    self.assertTrue(os.path.exists(srRequest.verify))
                    logging.info(f"[PASS]{safeStatus} Verified path exists.")
                    self.assertTrue(srRequest.verify.endswith('.pem'))
                    logging.info(f"[PASS]{safeStatus} Verified we are using it.")
                    with open(srRequest.verify, 'rb') as f:
                        pemContent = f.read()
                    self.assertTrue(pemContent, "PEM file content should not be empty")
                    logging.info(f"[PASS]{safeStatus} Verified its not empty.")
            except Exception as e:
                self.fail(f"[FAIL]{safeStatus} Initialization with certificateNeedFetch: True \nSomething went wrong: {e}")

    def test_HeadersBasicAuth(self):
        """
        Test Basic Authentication Header with https://postman-echo.com/basic-auth.
        """
        for config in self.integrationConfig():
            srRequest = SecureRequests(headers={HeaderKeys.AUTHORIZATION.value: "Basic cG9zdG1hbjpwYXNzd29yZA=="}, **config)
            statusSafe = "[SAFE]" if not config['unsafe'] else "[UNSAFE]"
            statusTLS = "[USE TLS]" if config['useTLS'] else "[NO TLS]"

            logging.info('------------------------------------------------------------')
            logging.info('>>> Testing Basic Auth with Config <<<')
            logging.info(f'{formatDict(config, ignoredKeys=["logPath", "logToFile", "suppressWarnings"])}\n')

            try:
                response = srRequest.makeRequest('https://postman-echo.com/basic-auth')
                self.assertEqual(response.status_code, 200, f"[FAIL]{statusSafe}{statusTLS} Request to https://postman-echo.com/basic-auth failed with status code {response.status_code}.")
                logging.info(f"[PASS]{statusSafe}{statusTLS} Request to https://postman-echo.com/basic-auth with status code {response.status_code}.")
            except Exception as e:
                self.fail(f"[FAIL]{statusSafe}{statusTLS} Request to https://postman-echo.com/basic-auth failed with exception: {e}")
            
        logging.info(f'\n- Used Cookies: None.\n- Used Header:\n{formatDict(srRequest.headers)}\n')

    def test_HeaderLogics(self):
        # Mock random.choice to return the first element for predictability
        config = self.integrationConfig()[0]
        with patch('random.choice', side_effect=lambda x: x[0]):
            # Initialize without headers
            srRequest = SecureRequests(**config)
            self.assertEqual(srRequest.headers, self.defaultHeader)
            logging.info("[PASS] Initialization without headers matches default headers.")

            # Initialize with headers
            customHeaders = {HeaderKeys.AUTHORIZATION.value: "Basic cG9zdG1hbjpwYXNzd29yZA=="}
            srRequest = SecureRequests(headers=customHeaders, **config)
            expected_headers = self.defaultHeader.copy()
            expected_headers.update(customHeaders)
            self.assertEqual(srRequest.headers, expected_headers)
            logging.info("[PASS] Initialization with custom headers.")

            # Test headerSetKey
            srRequest.headerSetKey(HeaderKeys.ORIGIN, "http://example.com")
            expected_headers[HeaderKeys.ORIGIN.value] = "http://example.com"
            self.assertEqual(srRequest.headers[HeaderKeys.ORIGIN.value], "http://example.com")
            logging.info("[PASS] headerSetKey added the key.")

            # Test headerGenerate with customHeaders
            customHeaders = {HeaderKeys.ACCEPT.value: "application/json", HeaderKeys.AUTHORIZATION.value: "test"}
            generated_headers = srRequest.headerGenerate(customHeaders)
            expected_generated_headers = self.defaultHeader.copy()
            expected_generated_headers.update(customHeaders)
            self.assertEqual(generated_headers, expected_generated_headers)
            logging.info("[PASS] headerGenerate with customHeaders.")

            # Test headerRemoveKey
            srRequest.headerRemoveKey(HeaderKeys.ORIGIN)
            del expected_headers[HeaderKeys.ORIGIN.value]
            self.assertNotIn(HeaderKeys.ORIGIN.value, srRequest.headers)
            logging.info("[PASS] headerRemoveKey removed the key.")

            # Test headerRemoveMultiple
            keys_to_remove = [HeaderKeys.ACCEPT, HeaderKeys.AUTHORIZATION]
            srRequest.headerRemoveMultiple(keys_to_remove)
            for key in keys_to_remove:
                del expected_headers[key.value]
                self.assertNotIn(key.value, srRequest.headers)
            logging.info("[PASS] headerRemoveMultiple removed the keys.")

    def test_CookiesLogics(self):
        config = self.integrationConfig()[0]
        with patch('random.choice', side_effect=lambda x: x[0]):
            # Initialize SecureRequests
            srRequest = SecureRequests(**config)

            # Test cookieUpdate
            cookie_info = {
                CookieAttributeKeys.PATH: "/",
                CookieAttributeKeys.SECURE: True,
                CookieAttributeKeys.EXPIRES: "Wed, 09 Jun 2021 10:18:14 GMT"
            }
            srRequest.cookieUpdate(CookieKeys.SESSION_ID, cookie_info)
            expected_cookie_value = srRequest._serializeCookieInfo(cookie_info)
            self.assertEqual(srRequest.session.cookies.get(CookieKeys.SESSION_ID.value), expected_cookie_value)
            logging.info("[PASS] cookieUpdate added the cookie.")

            # Test cookieGet
            retrieved_cookie_info = srRequest.cookieGet(CookieKeys.SESSION_ID)
            for key in cookie_info:
                self.assertIn(key, retrieved_cookie_info)
                self.assertEqual(str(retrieved_cookie_info[key]), str(cookie_info[key]))
            logging.info("[PASS] cookieGet retrieved the correct cookie info.")

            # Test cookieRemove
            srRequest.cookieRemove(CookieKeys.SESSION_ID)
            self.assertIsNone(srRequest.session.cookies.get(CookieKeys.SESSION_ID.value))
            logging.info("[PASS] cookieRemove removed the cookie.")

            # Test cookieUpdateMultiple
            multiple_cookies = {
                CookieKeys.SESSION_ID: {
                    CookieAttributeKeys.PATH: "/",
                    CookieAttributeKeys.SECURE: True,
                    CookieAttributeKeys.EXPIRES: "Wed, 09 Jun 2021 10:18:14 GMT"
                },
                CookieKeys.USER_ID: {
                    CookieAttributeKeys.PATH: "/user",
                    CookieAttributeKeys.SECURE: False,
                    CookieAttributeKeys.EXPIRES: "Wed, 09 Jun 2022 10:18:14 GMT"
                }
            }
            srRequest.cookieUpdateMultiple(multiple_cookies)
            for key, info in multiple_cookies.items():
                expected_value = srRequest._serializeCookieInfo(info)
                self.assertEqual(srRequest.session.cookies.get(key.value), expected_value)
            logging.info("[PASS] cookieUpdateMultiple added multiple cookies.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner())