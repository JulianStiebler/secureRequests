"""
This module provides the `Config` class for managing configuration settings for secure requests. 

The `Config` class allows for both direct configuration and environment variable-based configuration. 
It includes settings for:
- Enabling or disabling TLS
- Marking requests as unsafe
- Fetching certificates
- Logging configurations
- Suppressing warnings
- Setting custom certificate paths

Classes:
- Config: Manages configuration settings and provides methods to set and get these settings.

Usage:
The `Config` class can be instantiated and used to set or get various configuration options.
By default, configurations are set directly, but environment variables can be used by enabling `useEVar`.

Example:
    config = Config()
    config.setUseTLS(True)
    config.setLogLevel('DEBUG')

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki
# Created: 15.07.2024
# Last edited: 17.07.2024
"""
import os
import logging
from typing import Dict, Union

class Config:
    """
    Manages configuration settings for secure requests.

    This class supports both direct configuration and environment variable-based configuration.
    It includes settings for enabling/disabling TLS, marking requests as unsafe, fetching certificates,
    logging configurations, suppressing warnings, and setting custom certificate paths.

    Methods:
        __init__: Initializes the configuration settings with default values or environment variables.
        __getEnvBool: Retrieve an environment variable and convert it to a boolean.
        setUseTLS: Set the useTLS configuration.
        setUnsafe: Set the unsafe configuration.
        setCertificateNeedFetch: Set the certificateNeedFetch configuration.
        setCertificateURL: Set the certificateURL configuration.
        setCertificatePath: Set the certificatePath configuration.
        setLogToFile: Set the logToFile configuration.
        setLogLevel: Set the logLevel configuration.
        setLogPath: Set the logPath configuration.
        setLogExtensive: Set the logExtensive configuration.
        setSilent: Set the silent configuration.
        setSuppressWarnings: Set the suppressWarnings configuration.
        getUseTLS: Get the useTLS configuration.
        getUnsafe: Get the unsafe configuration.
        getCertificateNeedFetch: Get the certificateNeedFetch configuration.
        getCertificateURL: Get the certificateURL configuration.
        getCertificatePath: Get the certificatePath configuration.
        getLogToFile: Get the logToFile configuration.
        getLogLevel: Get the logLevel configuration.
        getLogPath: Get the logPath configuration.
        getLogExtensive: Get the logExtensive configuration.
        getSilent: Get the silent configuration.
        getSuppressWarnings: Get the suppressWarnings configuration.
    """
    def __init__(self) -> None:
        """
        Initializes the configuration settings with default values or environment variables.

        By default, the configurations are set directly. If `useEVar` is True, environment variables
        are used to set the configuration values.

        Attributes initialized:
            - useTLS
            - unsafe
            - certificateNeedFetch
            - certificateURL
            - certificatePath
            - logToFile
            - logLevel
            - logPath
            - logExtensive
            - silent
            - suppressWarnings
        """
        self.useEVar: bool = False  # Default mode is direct configuration
        self.envVars: Dict[str, str] = {
            'useTLS': 'SECURE_REQUESTS_USE_TLS',
            'unsafe': 'SECURE_REQUESTS_UNSAFE',
            'certificateNeedFetch': 'SECURE_REQUESTS_CERTIFICATE_NEED_FETCH',
            'certificateURL': 'SECURE_REQUESTS_CERTIFICATE_URL',
            'certificatePath': 'SECURE_REQUESTS_CERTIFICATE_PATH',
            'logToFile': 'SECURE_REQUESTS_LOG_TO_FILE',
            'logLevel': 'SECURE_REQUESTS_LOG_LEVEL',
            'logPath': 'SECURE_REQUESTS_LOG_PATH',
            'logExtensive': 'SECURE_REQUESTS_LOGEXTENSIVE',
            'silent': 'SECURE_REQUESTS_SILENT',
            'suppressWarnings': 'SECURE_REQUESTS_SUPPRESS_WARNINGS',
            'customCert': 'SECURE_REQUESTS_CUSTOM_CERT_PATH'
        }

        self.useTLS: bool = True if not self.useEVar else self.__getEnvBool('useTLS', True)
        self.unsafe: bool = False if not self.useEVar else self.__getEnvBool('unsafe', False)
        self.certificateNeedFetch: bool = True if not self.useEVar else self.__getEnvBool('certificateNeedFetch', True)
        self.certificateURL: str = "https://curl.se/ca/cacert.pem" if not self.useEVar else os.getenv(self.envVars['certificateURL'], "https://curl.se/ca/cacert.pem")
        self.certificatePath: str = "cacert.pem" if not self.useEVar else os.getenv(self.envVars['certificatePath'], "cacert.pem")
        self.logToFile: bool = False if not self.useEVar else self.__getEnvBool('logToFile', False)
        self.logLevel: Union[int, str] = logging.INFO if not self.useEVar else os.getenv(self.envVars['logLevel'], logging.INFO)
        self.logPath: str = "secureRequests.log" if not self.useEVar else os.getenv(self.envVars['logPath'], "secureRequests.log")
        self.logExtensive: bool = False if not self.useEVar else self.__getEnvBool('logExtensive', False)
        self.silent: bool = False if not self.useEVar else self.__getEnvBool('silent', False)
        self.suppressWarnings: bool = False if not self.useEVar else self.__getEnvBool('suppressWarnings', False)

    def __getEnvBool(self, key: str, default: bool) -> bool:
        """
        Retrieve an environment variable and convert it to a boolean.

        This method fetches the value of an environment variable using the provided key.
        If the environment variable is not set, it returns the provided default value.
        If the environment variable is set, it converts its value to True checking common indicators
            Common true indicators: ('true', '1', 't', 'y', 'yes').

        Args:
            key (str): The key in the `envVars` dictionary to lookup the environment variable.
            default (bool): The default value to return if the environment variable is not set.

        Returns:
            bool: The boolean value of the environment variable or the default value as bool.
        """
        env_key = self.envVars.get(key)
        if env_key is None:
            return default
        env_value = os.getenv(env_key)
        if env_value is None:
            return default
        return env_value.lower() in ('true', '1', 't', 'y', 'yes')
    
        # Setter methods for direct configuration
    def setUseTLS(self, value: bool):
        """
        Set the useTLS configuration.

        Args:
            value (bool): The value to set for useTLS.
        """
        self.useTLS = value

    def setUnsafe(self, value: bool):
        """
        Set the unsafe configuration.

        Args:
            value (bool): The value to set for unsafe.
        """
        self.unsafe = value

    def setCertificateNeedFetch(self, value: bool):
        """
        Set the certificateNeedFetch configuration.

        Args:
            value (bool): The value to set for certificateNeedFetch.
        """
        self.certificateNeedFetch = value

    def setCertificateURL(self, value: str):
        """
        Set the certificateURL configuration.

        Args:
            value (str): The value to set for certificateURL.
        """
        self.certificateURL = value

    def setCertificatePath(self, value: str):
        """
        Set the certificatePath configuration.

        Args:
            value (str): The value to set for certificatePath.
        """
        self.certificatePath = value

    def setLogToFile(self, value: bool):
        """
        Set the logToFile configuration.

        Args:
            value (bool): The value to set for logToFile.
        """
        self.logToFile = value

    def setLogLevel(self, value: Union[int, str]):
        """
        Set the logLevel configuration.

        Args:
            value (Union[int, str]): The value to set for logLevel.
        """
        self.logLevel = value

    def setLogPath(self, value: str):
        """
        Set the logPath configuration.

        Args:
            value (str): The value to set for logPath.
        """
        self.logPath = value

    def setLogExtensive(self, value: bool):
        """
        Set the logExtensive configuration.

        Args:
            value (bool): The value to set for logExtensive.
        """
        self.logExtensive = value

    def setSilent(self, value: bool):
        """
        Set the silent configuration.

        Args:
            value (bool): The value to set for silent.
        """
        self.silent = value

    def setSuppressWarnings(self, value: bool):
        """
        Set the suppressWarnings configuration.

        Args:
            value (bool): The value to set for suppressWarnings.
        """
        self.suppressWarnings = value

    # Getter methods
    def getUseTLS(self) -> bool:
        """
        Get the useTLS configuration.

        Returns:
            bool: The current value of useTLS.
        """
        return self.useTLS

    def getUnsafe(self) -> bool:
        """
        Get the unsafe configuration.

        Returns:
            bool: The current value of unsafe.
        """
        return self.unsafe

    def getCertificateNeedFetch(self) -> bool:
        """
        Get the certificateNeedFetch configuration.

        Returns:
            bool: The current value of certificateNeedFetch.
        """
        return self.certificateNeedFetch

    def getCertificateURL(self) -> str:
        """
        Get the certificateURL configuration.

        Returns:
            str: The current value of certificateURL.
        """
        return self.certificateURL

    def getCertificatePath(self) -> str:
        """
        Get the certificatePath configuration.

        Returns:
            str: The current value of certificatePath.
        """
        return self.certificatePath

    def getLogToFile(self) -> bool:
        """
        Get the logToFile configuration.

        Returns:
            bool: The current value of logToFile.
        """
        return self.logToFile

    def getLogLevel(self) -> Union[int, str]:
        """
        Get the logLevel configuration.

        Returns:
            Union[int, str]: The current value of logLevel.
        """
        return self.logLevel

    def getLogPath(self) -> str:
        """
        Get the logPath configuration.

        Returns:
            str: The current value of logPath.
        """
        return self.logPath

    def getLogExtensive(self) -> bool:
        """
        Get the logExtensive configuration.

        Returns:
            bool: The current value of logExtensive.
        """
        return self.logExtensive

    def getSilent(self) -> bool:
        """
        Get the silent configuration.

        Returns:
            bool: The current value of silent.
        """
        return self.silent

    def getSuppressWarnings(self) -> bool:
        """
        Get the suppressWarnings configuration.

        Returns:
            bool: The current value of suppressWarnings.
        """
        return self.suppressWarnings

config = Config()
