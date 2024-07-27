"""
This module provides utilities for making secure HTTP requests using the `requests` library.
It includes custom transport adapters, certificate management, and header/cookie handling with enums.

Classes:
    TLSAdapter: A custom Transport Adapter for using a specified SSL context with requests.
        Methods:
            - __init__: Initializes the TLSAdapter with an optional SSL context.
            - initPoolmanager: Initializes the pool manager with the SSL context.
            - _createSSLContext: Creates and returns a default SSL context.

    SecureRequests: Provides methods to make HTTP requests with enhanced security features, including
                    SSL/TTLS configuration, certificate management, and custom headers and cookies.
        Methods:
            - __init__: Initializes the SecureRequests instance with various configuration options.
            - _certificateFetch: Fetches the SSL certificate if required.
            - _certificateSet: Sets the SSL certificate for the session.
            - makeRequest: Makes an HTTP request with the given method, URL, and optional payload and headers.
            - _logRequest: Logs the details of the HTTP request and response.
            - headerGenerate: Generates a dictionary of default headers for HTTP requests.
            - headerSetKey: Sets a specific header key to a given value.
            - headerRemoveKey: Removes a specific header key.
            - headerUpdateMultiple: Updates multiple header keys with the provided values.
            - headerRemoveMultiple: Removes multiple header keys.
            - _serializeCookieInfo: Serializes cookie information into a string.
            - _deserializeCookieInfo: Deserializes a cookie information string back into a dictionary.
            - cookieUpdate: Updates a specific cookie with the provided information.
            - cookieGet: Retrieves the information for a specific cookie.
            - cookieRemove: Removes a specific cookie.
            - cookieUpdateMultiple: Updates multiple cookies with the provided information.
            - cookieGetAll: Retrieves all cookies and their information.

Functions:
    headerGenerate: Generates a dictionary of default headers for HTTP requests.

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki

# Created: 15.07.2024
# Last edited: 17.07.2024
"""

from typing import Dict, Any, Optional, List, Union
import requests
import ssl
import logging
import os
from datetime import datetime

from .secureRequestsEnums import HeaderKeys, CookieKeys, CookieAttributeKeys

class TLSAdapter(requests.adapters.HTTPAdapter):
    ssl_context: Optional[ssl.SSLContext]

    def __init__(self, sslContext: Optional[ssl.SSLContext] = None, **kwargs: Any) -> None: ...
    def initPoolmanager(self, *args: Any, **kwargs: Any) -> None: ...
    def _createSSLContext(self) -> ssl.SSLContext: ...

class SecureRequests:
    session: requests.Session
    headers: Dict[str, str]
    cookies: Dict[str, Dict[CookieAttributeKeys, Union[str, bool, int, datetime]]]
    verify: Union[bool, str]

    def __init__(
        self,
        requests: Any = requests,
        os: Any = os,
        datetime: Any = datetime,
        useEnv: bool = False,
        customEnvVars: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        useTLS: Optional[bool] = None,
        unsafe: Optional[bool] = None,
        fetchCertificate: Optional[bool] = None,
        certificateURL: Optional[str] = None,
        certificatePath: Optional[str] = None,
        logToFile: Optional[bool] = None,
        logLevel: Union[int, str] = logging.INFO,
        logPath: Optional[str] = None,
        logExtensive: Optional[bool] = None,
        silent: Optional[bool] = None,
        suppressWarnings: Optional[bool] = None,
        session: Optional[requests.Session] = None
    ) -> None: ...

    # None is matched with the defaults in the config

    def _certificateFetch(self, force) -> None: ...
    def _certificateSet(self) -> bool: ...
    def makeRequest(
        self,
        url: str,
        method: str = "GET",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> requests.Response: ...
    def _logRequest(self, method: str, url: str, response: requests.Response, **kwargs: Any) -> None: ...
    @staticmethod
    def headerGenerate(customHeaders: Optional[Dict[str, Any]] = None) -> Dict[str, str]: ...
    def headerSetKey(self, key: HeaderKeys, value: str) -> None: ...
    def headerRemoveKey(self, key: HeaderKeys) -> None: ...
    def headerUpdateMultiple(self, newHeader: Dict[HeaderKeys, str]) -> None: ...
    def headerRemoveMultiple(self, keys: List[HeaderKeys]) -> None: ...
    def _serializeCookieInfo(self, cookieInfo: Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]) -> str: ...
    def _deserializeCookieInfo(self, cookieInfoStr: str) -> Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]: ...
    def cookieUpdate(self, key: CookieKeys, cookieInfo: Union[str, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None: ...
    def cookieGet(self, key: CookieKeys) -> Optional[Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]: ...
    def cookieRemove(self, key: CookieKeys) -> None: ...
    def cookieUpdateMultiple(self, cookies: Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None: ...
    def cookieGetAll(self) -> Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]: ...