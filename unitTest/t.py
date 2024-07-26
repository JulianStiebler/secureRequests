"""
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

from secureRequests import SecureRequests, srExceptions
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
        logging.basicConfig(stream=self.logStream, level=logging.DEBUG)

    def integrationConfig(self):
        """
        Returns a list of safe configuration dictionaries for SecureRequests.
        These configurations ensure that the requests are made securely.
        """
        return [
            {'certificateNeedFetch': True, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False},
            {'certificateNeedFetch': False, 'unsafe': True, 'useTLS': False, 'logToFile': True, 'logPath': "unitTest/unitTest.log", 'suppressWarnings': False}
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

if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner())