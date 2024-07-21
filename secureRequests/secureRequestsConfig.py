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

MIT License
-----------
Copyright (c) 2024 Julian Stiebler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Created: 15.07.2024
# Last edited: 17.07.2024
"""
import os
import logging
from typing import Dict, Union

class Config:
    def __init__(self) -> None:
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
        # Default configurations
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
    def setUseTLS(self, value: bool): self.useTLS = value
    def setUnsafe(self, value: bool): self.unsafe = value
    def setCertificateNeedFetch(self, value: bool): self.certificateNeedFetch = value
    def setCertificateURL(self, value: str): self.certificateURL = value
    def setCertificatePath(self, value: str): self.certificatePath = value
    def setLogToFile(self, value: bool): self.logToFile = value
    def setLogLevel(self, value: int|str): self.logLevel = value
    def setLogPath(self, value: str): self.logPath = value
    def setLogExtensive(self, value: bool): self.logExtensive = value
    def setSilent(self, value: bool): self.silent = value
    def setSuppressWarnings(self, value: bool): self.suppressWarnings = value

    # Getter methods
    def getUseTLS(self): return self.useTLS
    def getUnsafe(self): return self.unsafe
    def getCerificateNeedFetch(self): return self.certificateNeedFetch
    def getCertificateURL(self): return self.certificateURL
    def getCertificatePath(self): return self.certificatePath
    def getLogToFile(self): return self.logToFile
    def getLogLevel(self): return self.logLevel
    def getLogPath(self): return self.logPath
    def getLogExtensive(self): return self.logExtensive
    def getSilent(self): return self.silent
    def getSuppressWarnings(self): return self.suppressWarnings

config = Config()
