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
        setCertificateVerifyChecksum: Set the certificateVerifyChecksum configuration.
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
        getCertificateVerifyChecksum: Get the certificateVerifyChecksum configuration.
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
            - certificateVerifyChecksum
            - logToFile
            - logLevel
            - logPath
            - logExtensive
            - silent
            - suppressWarnings
        """
        self.useEVar: bool = False  # Default mode is direct configuration
        self.envVars: Dict[str, str] = {
            "useTLS": "SECURE_REQUESTS_USE_TLS",
            "unsafe": "SECURE_REQUESTS_UNSAFE",
            "certificateNeedFetch": "SECURE_REQUESTS_CERTIFICATE_NEED_FETCH",
            "certificateURL": "SECURE_REQUESTS_CERTIFICATE_URL",
            "certificatePath": "SECURE_REQUESTS_CERTIFICATE_PATH",
            "certificateVerifyChecksum": "SECURE_REQUESTS_CERTIFICATE_VERIFY_CHECKSUM",
            "logToFile": "SECURE_REQUESTS_LOG_TO_FILE",
            "logLevel": "SECURE_REQUESTS_LOG_LEVEL",
            "logPath": "SECURE_REQUESTS_LOG_PATH",
            "logExtensive": "SECURE_REQUESTS_LOGEXTENSIVE",
            "silent": "SECURE_REQUESTS_SILENT",
            "suppressWarnings": "SECURE_REQUESTS_SUPPRESS_WARNINGS",
        }

        self.useTLS: bool = (
            True if not self.useEVar else self.__getEnvBool("useTLS", True)
        )
        self.unsafe: bool = (
            False if not self.useEVar else self.__getEnvBool("unsafe", False)
        )
        self.certificateNeedFetch: bool = (
            True
            if not self.useEVar
            else self.__getEnvBool("certificateNeedFetch", True)
        )
        self.certificateURL: str = (
            "https://curl.se/ca/cacert.pem"
            if not self.useEVar
            else os.getenv(
                self.envVars["certificateURL"], "https://curl.se/ca/cacert.pem"
            )
        )
        self.certificatePath: str = (
            "cacert.pem"
            if not self.useEVar
            else os.getenv(self.envVars["certificatePath"], "cacert.pem")
        )
        self.certificateVerifyChecksum: bool = (
            False
            if not self.useEVar
            else self.__getEnvBool("certificateVerifyChecksum", False)
        )
        self.logToFile: bool = (
            False if not self.useEVar else self.__getEnvBool("logToFile", False)
        )
        self.logLevel: Union[int, str] = (
            logging.DEBUG
            if not self.useEVar
            else os.getenv(self.envVars["logLevel"], logging.DEBUG)
        )
        self.logPath: str = (
            "secureRequests.log"
            if not self.useEVar
            else os.getenv(self.envVars["logPath"], "secureRequests.log")
        )
        self.logExtensive: bool = (
            False if not self.useEVar else self.__getEnvBool("logExtensive", False)
        )
        self.silent: bool = (
            False if not self.useEVar else self.__getEnvBool("silent", False)
        )
        self.suppressWarnings: bool = (
            False if not self.useEVar else self.__getEnvBool("suppressWarnings", False)
        )
        self.certificateRedactURL: bool = (
            True if not self.useEVar else self.__getEnvBool("certificateRedactURL", True)
        )

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
        return env_value.lower() in ("true", "1", "t", "y", "yes")

        # Setter methods for direct configuration

    def setUseTLS(self, value: bool):
        """Specifies if TLS should be used for requests."""
        self.useTLS = value

    def setUnsafe(self, value: bool):
        """Specifies if requests should be using the certificate."""
        self.unsafe = value

    def setCertificateNeedFetch(self, value: bool):
        """Specifies if the certificate should be fetched."""
        self.certificateNeedFetch = value

    def setCertificateURL(self, value: str):
        """Specifies the URL from which the certificate should be fetched."""
        self.certificateURL = value

    def setCertificatePath(self, value: str):
        """Specifies the path where the certificate should be stored."""
        self.certificatePath = value

    def setCertificateVerifyChecksum(self, value: bool):
        """Specifies if the certificate checksum should be verified."""
        self.certificateVerifyChecksum = value

    def setCeritificateRedactURL(self, value: bool):
        """Specifies if the certificate URL should be redacted in logs."""
        self.certificateRedactURL = value

    def setLogToFile(self, value: bool):
        """Specifies if logs should be written to a file."""
        self.logToFile = value

    def setLogLevel(self, value: Union[int, str]):
        """Specifies the log level for the logger."""
        self.logLevel = value

    def setLogPath(self, value: str):
        """Specifies the path where logs should be stored."""
        self.logPath = value

    def setLogExtensive(self, value: bool):
        """Specifies if extensive logs should be written."""
        self.logExtensive = value

    def setSilent(self, value: bool):
        """Specifies if logs should be suppressed."""
        self.silent = value

    def setSuppressWarnings(self, value: bool):
        """Specifies if warnings should be suppressed."""
        self.suppressWarnings = value

    # -----------------------------------------------------------------------------------------------

    # Getter methods
    def getUseTLS(self) -> bool:
        """Returns the current value of the useTLS configuration."""
        return self.useTLS

    def getUnsafe(self) -> bool:
        """Returns the current value of the unsafe configuration."""
        return self.unsafe

    def getCertificateNeedFetch(self) -> bool:
        """Returns the current value of the certificateNeedFetch configuration."""
        return self.certificateNeedFetch

    def getCertificateURL(self) -> str:
        """Returns the current value of the certificateURL configuration."""
        return self.certificateURL

    def getCertificatePath(self) -> str:
        """Returns the current value of the certificatePath configuration."""
        return self.certificatePath

    def getCertificateVerifyChecksum(self) -> bool:
        """Returns the current value of the certificateVerifyChecksum configuration."""
        return self.certificateVerifyChecksum
    
    def getCertificateRedactURL(self) -> bool:
        """Returns the current value of the certificateRedactURL configuration."""
        return self.certificateRedactURL

    def getLogToFile(self) -> bool:
        """Returns the current value of the logToFile configuration."""
        return self.logToFile

    def getLogLevel(self) -> Union[int, str]:
        """Returns the current value of the logLevel configuration."""
        return self.logLevel

    def getLogPath(self) -> str:
        """Returns the current value of the logPath configuration."""
        return self.logPath

    def getLogExtensive(self) -> bool:
        """Returns the current value of the logExtensive configuration."""
        return self.logExtensive

    def getSilent(self) -> bool:
        """Returns the current value of the silent configuration."""
        return self.silent

    def getSuppressWarnings(self) -> bool:
        """Returns the current value of the suppressWarnings configuration."""
        return self.suppressWarnings

config = Config()
