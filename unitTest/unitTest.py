"""
MIT License

...

# Created: 15.07.2024
# Last edited: 17.07.2024
"""

import unittest
import sys
import os
import logging
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
import io
import traceback

# Ensure the module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from secureRequests import SecureRequests
from secureRequests.secureRequestsDecorators import STATUS_CODE_EXCEPTION_MAP
from secureRequests import HeaderKeys, CookieAttributeKeys, CookieKeys

def formatHeaders(headers):
    """Format headers dictionary into a string with proper indentation and line breaks."""
    if not headers:
        return "None"
    return "\n".join([f" > {key}: {value}" for key, value in headers.items()])

def formatCookies(cookies):
    """Format cookies dictionary into a string with proper indentation and line breaks."""
    if not cookies:
        return "."
    
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passedTests = []
        self.failedTests = []
        self.testLogs = {}  # Store logs per test
        self._originalStream = {}
        self._currentTest = None

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passedTests.append(test)
        self.testLogs[test] = self._getTestLog()
        logging.info(f"[PASS] {test} - Log Output:\n{self.testLogs[test]}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failedTests.append((test, err))
        self.testLogs[test] = self._getTestLog()
        logging.error(f"[FAIL] {test} - Log Output:\n{self.testLogs[test]}")

    def startTest(self, test):
        super().startTest(test)
        self._currentTest = test
        self._setup_logger(test)

    def _setup_logger(self, test):
        # Set up logger to capture logs for each test
        testLogStream = io.StringIO()
        handler = logging.StreamHandler(testLogStream)
        handler.setLevel(logging.INFO)

        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Store the original stream handler to revert later
        self._originalStream[test] = (testLogStream, handler)

    def _getTestLog(self):
        logger = logging.getLogger()
        testLogStream, handler = self._originalStream.get(self._currentTest, (None, None))
        if testLogStream and handler:
            logger.removeHandler(handler)
            return testLogStream.getvalue()
        return ""

    def stopTest(self, test):
        super().stopTest(test)
        self._currentTest = None

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        result = super().run(test)
        self._generateReport(result)
        return result

    def _generateReport(self, result):
        with open("unitTest/unitTestResults.md", "w") as reportFile:
            reportFile.write("# unitTest\n\n")
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
        output = []
        testName = test._testMethodName
        output.append(f"### {testName}\n")
        output.append(f"<a name=\"{testName.lower()}\"></a>\n")
        output.append("#### Configurations\n")

        # Extracting configurations from the test instance
        config = self._extractConfig(test)
        for key, value in config.items():
            output.append(f"- {key}: {value}\n")

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

    def _extractConfig(self, test):
        # Extract configurations from the test instance
        if hasattr(test, 'test_config'):
            return test.test_config
        return {}

class TestSecureRequests(unittest.TestCase):
    def setUp(self):
        self.baseURL = 'https://httpbin.org'
        self.statusCodes = STATUS_CODE_EXCEPTION_MAP
        self.failures = []
        self.logStream = io.StringIO()
        logging.basicConfig(stream=self.logStream, level=logging.INFO)

    def configsSAFE(self):
        return [
            {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': True, 'unsafe': False, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': True, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
        ]

    def configsUNSAFE(self):
        return [
            {'certificateNeedFetch': False, 'unsafe': True, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': False, 'unsafe': True, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': True, 'unsafe': True, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': True, 'unsafe': True, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
        ]

    @patch('secureRequests.secureRequests.SecureRequests.makeRequest')
    def test_HTTPMethods_SAFE(self, srRequestMock):
        config = self.configsSAFE()[1]
        srRequest = SecureRequests(**config)
        methods = ['get', 'post', 'put', 'delete', 'patch']
        for method in methods:
            with self.subTest(method=method):
                logging.info('------------------------------------------------------------')
                mockResponse = MagicMock()
                logging.info('>>> Testing Status Code 200 <<<')
                mockResponse.status_code = 200
                srRequestMock.return_value = mockResponse
                response = srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 200)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 200.")

                logging.info('\n>>> Testing Status Code 400 <<<')
                mockResponse.status_code = 400
                mockResponse.reason = "Bad Request"
                mockResponse.text = "Mocked response for status code 400"
                srRequestMock.return_value = mockResponse

                srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 400.")
                logging.info(f'\n- Used Cookies: {formatCookies(srRequest.cookieGetAll())}.\n- Used Header:\n{formatHeaders(srRequest.headers)}\n')

        self.test_config = config

    @patch('secureRequests.secureRequests.SecureRequests.makeRequest')
    def test_HTTPMethods_Cookies_SAFE(self, srRequestMock):
        config = self.configsSAFE()[1]
        srRequest = SecureRequests(**config)
        srRequest.cookieUpdate(CookieKeys.SESSION_ID, {
            CookieAttributeKeys.PATH: '/',
            CookieAttributeKeys.EXPIRES: datetime.now() + timedelta(days=7),
            CookieAttributeKeys.SECURE: True
        })
        srRequest.headerGenerate(customHeaders={HeaderKeys.CONTENT_TYPE: "application/json"})

        methods = ['get', 'post', 'put', 'delete', 'patch']
        for method in methods:
            with self.subTest(method=method):
                logging.info('------------------------------------------------------------')
                logging.info('>>> Testing Status Code 200 <<<')
                # Test with status code 200
                mockResponse = MagicMock()
                mockResponse.status_code = 200
                srRequestMock.return_value = mockResponse

                response = srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 200)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 200.\n")

                logging.info('\n>>> Testing Status Code 400')
                # Test with status code 400
                mockResponse.status_code = 400
                mockResponse.reason = "Bad Request"
                mockResponse.text = "Mocked response for status code 400"
                srRequestMock.return_value = mockResponse

                srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 400)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 400.")
                logging.info(f'\n- Used Cookies: {formatCookies(srRequest.cookieGetAll())}.\n- Used Header:\n{formatHeaders(srRequest.headers)}\n')
                

        self.test_config = config

    @patch('secureRequests.secureRequests.SecureRequests.makeRequest')
    def test_HTTPMethods_Cookies_UNSAFE(self, srRequestMock):
        config = self.configsUNSAFE()[0]
        srRequest = SecureRequests(**config)
        srRequest.cookieUpdate(CookieKeys.SESSION_ID, {
            CookieAttributeKeys.PATH: '/',
            CookieAttributeKeys.EXPIRES: datetime.now() + timedelta(days=7),
            CookieAttributeKeys.SECURE: True
        })
        methods = ['get', 'post', 'put', 'delete', 'patch']
        srRequest.headerGenerate(customHeaders={HeaderKeys.CONTENT_TYPE: "application/json"})
        for method in methods:
            with self.subTest(method=method):
                # Test with status code 200
                logging.info('------------------------------------------------------------')
                logging.info('>>> Testing Status Code 200 <<<')
                mockResponse = MagicMock()
                mockResponse.status_code = 200
                srRequestMock.return_value = mockResponse

                response = srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 200)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 200.")

                # Test with status code 400
                logging.info('>>> Testing Status Code 400 <<<')
                mockResponse.status_code = 400
                mockResponse.reason = "Bad Request"
                mockResponse.text = "Mocked response for status code 400"
                srRequestMock.return_value = mockResponse

                srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 400)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 400.")
                logging.info(f'\n- Used Cookies: {formatCookies(srRequest.cookieGetAll())}.\n- Used Header:\n{formatHeaders(srRequest.headers)}\n')

        self.test_config = config

    @patch('secureRequests.secureRequests.SecureRequests.makeRequest')
    def test_HTTPMethods_UNSAFE(self, srRequestMock):
        config = self.configsUNSAFE()[0]
        srRequest = SecureRequests(**config)
        methods = ['get', 'post', 'put', 'delete', 'patch']
        for method in methods:
            with self.subTest(method=method):
                logging.info('------------------------------------------------------------')
                logging.info('>>> Testing Status Code 200 <<<')
                mockResponse = MagicMock()
                mockResponse.status_code = 200
                srRequestMock.return_value = mockResponse

                response = srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 200)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 200.")

                logging.info('>>> Testing Status Code 400 <<<')
                mockResponse.status_code = 400
                mockResponse.reason = "Bad Request"
                mockResponse.text = "Mocked response for status code 400"
                srRequestMock.return_value = mockResponse

                srRequest.makeRequest(self.baseURL + f'/{method.upper()}', method=method.upper())
                self.assertEqual(response.status_code, 400)
                logging.info(f"[PASS][SAFE] {method.upper()} request to {self.baseURL}/{method.upper()} with status code 400.")
                logging.info(f'\n- Used Cookies: {formatCookies(srRequest.cookieGetAll())}.\n- Used Header:\n{formatHeaders(srRequest.headers)}\n')

        self.test_config = config

    def test_fetchCertOnInit_SAFE(self):
        config = self.configsSAFE()[2]
        srRequest = SecureRequests(**config)
        if config['certificateNeedFetch']:
            self.assertTrue(srRequest.verify)
            self.assertTrue(srRequest.verify.endswith('.pem'))
            self.assertTrue(os.path.exists(srRequest.verify))
            with open(srRequest.verify, 'rb') as f:
                pemContent = f.read()
            self.assertTrue(pemContent, "PEM file content should not be empty")
        else:
            self.assertFalse(srRequest.verify)
        logging.info(f"[PASS][SAFE] Initialization with certificateNeedFetch: {config['certificateNeedFetch']}")
        self.test_config = config

    def test_fetchCertOnInit_UNSAFE(self):
        config = self.configsUNSAFE()[2]
        srRequest = SecureRequests(**config)

        if config['certificateNeedFetch']:
            self.assertTrue(os.path.exists(srRequest.certificatePath), f"{srRequest.certificatePath} should exist")
            with open(srRequest.certificatePath, 'rb') as f:
                pemContent = f.read()
            self.assertTrue(pemContent, "PEM file content should not be empty")
        else:
            self.assertFalse(os.path.exists(srRequest.certificatePath), f"{srRequest.certificatePath} should not exist")

        self.assertFalse(srRequest.verify, "verify should be False for unsafe configuration")
        logging.info(f"[PASS][UNSAFE] Initialization with certificateNeedFetch: {config['certificateNeedFetch']}")
        self.test_config = config



    @patch('secureRequests.secureRequests.SecureRequests.makeRequest')
    def test_mockStatusCodes(self, srRequestMock):
        config = self.configsSAFE()[1]
        srRequest = SecureRequests(**config)
        
        for statusCode, exception in self.statusCodes.items():
            with self.subTest(status_code=statusCode, config=config):
                mockResponse = MagicMock()
                mockResponse.status_code = statusCode
                mockResponse.reason = f"Reason for {statusCode}"
                mockResponse.text = f"Mocked response for status code {statusCode}"
                
                # Modify the return value to raise the appropriate exception
                srRequestMock.side_effect = exception(f"{statusCode} Error: Reason for {statusCode} - Mocked response for status code {statusCode}")

                try:
                    srRequest.makeRequest(self.baseURL + f'/status/{statusCode}')
                except exception:
                    # Log the successful raising of the expected exception
                    logging.info(f"[PASS] {exception.__name__} raised for status code {statusCode} with config: {config}")
                else:
                    # Log the failure if the exception was not raised
                    message = f"{exception.__name__} not raised for status code {statusCode}"
                    self.logFailure(self.test_mockStatusCodes.__name__, config, message)
                    raise AssertionError(message)

        self.test_config = config

if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner())
