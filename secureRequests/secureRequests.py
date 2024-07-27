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

Usage Examples
--------------
>>> from secureRequests import SecureRequests
>>> print(headers)

>>> sr = SecureRequests()
>>> headers = sr.headerGenerate(customHeaders={"Content-Type": "application/json"})
>>> sr.headerSetKey(HeaderKeys.AUTHORIZATION, "Bearer token123")
>>> sr.cookieUpdate(CookieKeys.SESSION_ID, {
...     CookieAttributeKeys.DOMAIN: 'example.com',
...     CookieAttributeKeys.PATH: '/',
...     CookieAttributeKeys.EXPIRES: datetime.now() + timedelta(days=7),
...     CookieAttributeKeys.SECURE: True
... })
>>> response = sr.makeRequest("https://httpbin.org/get")
>>> print(response.status_code)

Returns
-------
>>>     makeRequest: requests.Response
>>>     headerGenerate: Dict[str, str]
>>>     headerSetKey: None
>>>     headerRemoveKey: None
>>>     headerUpdateMultiple: None
>>>     headerRemoveMultiple: None
>>>     cookieUpdate: None
>>>     cookieGet: Optional[Dict[CookieAttributeKeys, Union[str, bool, int, datetime]]]
>>>     cookieRemove: None
>>>     cookieUpdateMultiple: None
>>>     cookieGetAll: Dict[CookieKeys, Dict[CookieAttributeKeys, Union[str, bool, int, datetime]]]

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki

# Created: 15.07.2024
# Last edited: 17.07.2024
"""

import requests
from os.path import exists as PathExists
from os.path import join as PathJoin
import ssl
import warnings
import logging
import random
from datetime import datetime
from typing import Dict, Any, Optional, List, Union
from .secureRequestsConfig import config
from .secureRequestsDecorators import handleResponse
from .secureRequestsEnums import HeaderKeys, CookieKeys, CookieAttributeKeys
from urllib3.exceptions import InsecureRequestWarning

class TLSAdapter(requests.adapters.HTTPAdapter):
    """
    A custom Transport Adapter for using a specified SSL context with requests.

    Parameters
    ----------
    sslContext : ssl.SSLContext, optional
        SSL context to be used for the HTTPS connection. Defaults to `None`.

    Methods
    -------
    initPoolmanager(*args: Any, **kwargs: Any) -> None
        Initializes and configures the connection pool manager with the specified SSL context.
    _createSSLCOntext() -> ssl.SSLContext
        Creates a default SSL context with specific cipher settings.

    """

    def __init__(
        self, sslContext: Optional[ssl.SSLContext] = None, **kwargs: Any
    ) -> None:
        """
        Initializes the TLSAdapter with the specified SSL context.

        Parameters
        ----------
        sslContext : ssl.SSLContext, optional
            SSL context to be used for the HTTPS connection. Defaults to `None`.
        kwargs : Any
            Additional arguments passed to the parent `HTTPAdapter`.

        Returns
        -------
        None
        """
        self.ssl_context = sslContext
        super().__init__(**kwargs)

    def initPoolmanager(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes and configures the connection pool manager with the specified SSL context.

        Parameters
        ----------
        args : Any
            Positional arguments passed to the parent `init_poolmanager`.
        kwargs : Any
            Keyword arguments passed to the parent `init_poolmanager`.

        Returns
        -------
        None
        """
        context = self.ssl_context or self._createSSLCOntext()
        kwargs["ssl_context"] = context
        super().init_poolmanager(*args, **kwargs)

    def _createSSLCOntext(self) -> ssl.SSLContext:
        """
        Creates a default SSL context with specific cipher settings.

        Returns
        -------
        ssl.SSLContext
            Configured SSL context.
        """
        context = ssl.create_default_context()
        context.set_ciphers("HIGH:!DH:!aNULL")
        return context

class SecureRequests:
    """
    This class provides methods to make HTTP requests with enhanced security features, including
    SSL/TLS configuration, certificate management, and custom headers and cookies powered with enums.

    Attributes
    ----------
    session : requests.Session
        The `requests.Session` object used for making HTTP requests.
    headers : dict
        The headers to include in the requests.
    cookies : dict
        The cookies to include in the requests.

    Methods
    -------
    makeRequest(url: str, method: str = "GET", payload: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response
        Makes an HTTP request with the specified parameters.
    headerGenerate(referer: str = "https://httpbin.org/", ...) -> Dict[str, str]
        Generates default headers with optional custom values.
    headerSetKey(key: HeaderKeys, value: str) -> None
        Sets a specific header key to a given value.
    headerRemoveKey(key: HeaderKeys) -> None
        Removes a specific header key.
    headerUpdateMultiple(newHeaders: Dict[HeaderKeys, str]) -> None
        Updates multiple headers based on the provided dictionary.
    headerRemoveMultiple(keys: List[HeaderKeys]) -> None
        Removes multiple header keys at once.
    _serializeCookieInfo(self, cookieInfo: Dict[CookieAttributeKeys, Union[str, bool, int, datetime]]) -> str:
        Serializes the cookie attributes into a string.
    _deserializeCookieInfo(self, cookieInfoStr: str) -> Dict[CookieAttributeKeys, Union[str, bool, int, datetime]]:
        Deserializes the string back into a dictionary of cookie attributes.
    cookieUpdate(key: CookieKeys, cookieInfo: Dict[CookieKeys, str]) -> None
        Sets or updates a single cookie with specified attributes.
    cookieGet(key: CookieKeys) -> Optional[Dict[CookieKeys, str]]
        Retrieves the attributes of a single cookie.
    cookieRemove(key: CookieKeys) -> None
        Removes a single cookie.
    cookieUpdateMultiple(cookies: Dict[CookieKeys, Dict[CookieKeys, str]]) -> None
        Adds or updates multiple cookies at once.
    cookieGetAll() -> Dict[str, Dict[CookieKeys, str]]
        Retrieves all cookies with their attributes.
    """
    def __init__(
            self,
            requests: requests = requests,
            pathExists: PathExists = PathExists,
            pathJoin: PathJoin = PathJoin,
            datetime: datetime = datetime,
            useEnv: bool = False,
            customEnvVars: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None,
            useTLS: Optional[bool] = None,
            unsafe: Optional[bool] = None,
            certificateNeedFetch: Optional[bool] = None,
            certificateURL: Optional[str] = None,
            certificatePath: Optional[str] = None,
            logToFile: Optional[bool] = None,
            logLevel: int = logging.INFO,
            logPath: str = None,
            logExtensive: bool = None,
            silent: Optional[bool] = None,
            suppressWarnings: Optional[bool] = None,
            session: requests.Session = None) -> None:
        """
        Initializes the SecureRequests object with the specified parameters and defaults to the configuration settings from the config module.
        """
        
        # ------------------------------------------------- Initialize Modules -------------------------------------------------
        self.pathJoin = pathJoin
        self.pathExists = pathExists
        self.requests = requests
        self.datetime = datetime 

        # ---------------------------------------- Initialize Security Related Variables ----------------------------------------
        self.verify = False
        self.unsafe = unsafe if unsafe is not None else config.getUnsafe()
        self.useTLS = useTLS if useTLS is not None else config.getUseTLS()
        self.session = session if session else self.requests.session()
        if self.useTLS and not self.unsafe:
            self.session.mount("https://", TLSAdapter())

        self.headers = self.headerGenerate(headers) or self.headerGenerate()
        self.certificateURL = certificateURL if certificateURL else config.getCertificateURL()
        self.certificatePath = certificatePath if certificatePath else config.getCertificatePath()

        # ------------------------------------------ Initialize Config Related Variables ------------------------------------------
        if useEnv:
            config.EVarSetMode(True)
            if customEnvVars:
                config.EVarSet(customEnvVars)

        # Initialize attributes, falling back to config if not provided
        self.logToFile = logToFile if logToFile is not None else config.getLogToFile()
        self.logLevel = logLevel if logLevel is not None else config.getLogLevel()
        self.logPath = logPath if logPath is not None else config.getLogPath()
        self.logExtensive = logExtensive if logExtensive is not None else config.getLogExtensive()
        self.silent = silent if silent is not None else config.getSilent()
        self.suppressWarnings = suppressWarnings if suppressWarnings is not None else config.getSuppressWarnings()

        if self.logToFile:
            handler = logging.FileHandler(self.logPath)
            self.logger = logging.getLogger("SecureRequests")
            self.logger.setLevel(self.logLevel)
            self.logger.addHandler(handler)

        if self.silent:
            logging.disable(logging.CRITICAL)

        if self.suppressWarnings:
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)

        self.fetchCertificate = certificateNeedFetch if certificateNeedFetch is not None else config.getCertificateNeedFetch()
        if self.fetchCertificate:
            self._certificateFetch()
        self.verify = self._certificateSet()

    # ***********************************************************************************************************************
    # *                                            Certificate Related Stuff                                                *
    # ***********************************************************************************************************************

    def _certificateFetch(self, force=False) -> None:
        """
        Fetches a certificate from the configured URL and saves it to the local file system.

        Parameters
        ----------
        None
            This method does not take any parameters.

        Returns
        -------
        None
            This method does not return any value.

        Example
        -------
        >>> self._certificateFetch()
        INFO:root:Successfully fetched certificate and saved.
        """
        if self.pathExists(self.certificatePath):
            self.verify = self.certificatePath
            if not force:
                return

        response = self.makeRequest(self.certificateURL, method="GET")
        if response.status_code == 200:
            with open(self.certificatePath, "wb") as f:
                f.write(response.content)
            if hasattr(self, "logger"):
                self.logger.info("Successfully fetched certificate and saved.")
            self.verify = self.certificatePath
        else:
            if hasattr(self, "logger"):
                self.logger.error(
                    f"Failed to fetch certificate. Status code: {response.status_code}. Cannot use SSL but the program might work."
                )
            self.verify = False

    def _certificateSet(self) -> bool:
        """
        Sets the certificate path if not in unsafe mode and the certificate file exists.

        Parameters
        ----------
        None
            This method does not take any parameters.

        Returns
        -------
        bool
            Path to the certificate if not in unsafe mode and the file exists; otherwise, False.

        Example
        -------
        >>> self._certificateSet()
        '/path/to/certificate.pem'  # if certificate is set
        False                        # if certificate is not set or in unsafe mode
        """
        return (
            self.certificatePath
            if not self.unsafe and self.pathExists(self.certificatePath)
            else False
        )

    # ***********************************************************************************************************************
    # *                                                       Request Logic                                                 *
    # ***********************************************************************************************************************

    @handleResponse
    def makeRequest(
        self,
        url: str,
        method: str = "GET",
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> requests.Response:
        """
        Makes an HTTP request with the specified parameters.

        Parameters
        ----------
        url : str
            The URL for the request.
        method : str, optional
            The HTTP method to use (e.g., 'GET', 'POST'). Defaults to 'GET'.
        payload : dict, optional
            The payload to send with the request. Defaults to None.
        headers : dict, optional
            Custom headers to include with the request. Defaults to None.

        Returns
        -------
        requests.Response
            The HTTP response.

        **kwargs
        --------
        **kwargs from requests  are allowed here aswell.

        Raises
        ------
        Any exception matching to a status code.
        """
        srMethods = {
            "GET": self.session.get,
            "POST": self.session.post,
            "PUT": self.session.put,
            "DELETE": self.session.delete,
            "PATCH": self.session.patch,
        }

        if method not in srMethods:
            raise ValueError(f"Unsupported HTTP method: {method}")

        headers = headers or self.headers
        response = srMethods[method](
            url, data=payload, headers=headers, verify=self.verify, **kwargs
        )
        self._logRequest(method, url, response=response, data=payload, headers=headers)
        return response

    def _logRequest(self, method: str, url: str, response: requests.Response, **kwargs: Any) -> None:
        """
        Logs the details of the HTTP request if logging is enabled.

        Parameters
        ----------
        method : str
            The HTTP method used for the request (e.g., 'GET', 'POST').
        url : str
            The URL of the request.
        response : requests.Response
            The HTTP response object.
        kwargs : Any
            Additional keyword arguments passed to the request, such as headers or parameters.

        Returns
        -------
        None
            This method does not return any value.

        Example
        -------
        >>> self._logRequest('GET', 'https://example.com/api/data', response, headers={'Authorization': 'Bearer token'}, params={'key': 'value'})
        INFO:root:GET request to https://example.com/api/data with headers {'Authorization': 'Bearer token'} and params {'headers': {'Authorization': 'Bearer token'}, 'params': {'key': 'value'}} with Status Code 200
        """
        if hasattr(self, "logger"):
            timestamp = self.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            safetyStatus = "[UNSAFE]" if self.unsafe else "[SAFE]"
            tlsStatus = "[TLS]" if self.useTLS else "[NO TLS]"
            logExtra = f' with headers {kwargs.get("headers")} and params {kwargs}' if self.logExtensive else ''
            logDefaults = f' with Status Code {response.status_code} - {response.reason}'
            logBase = f'[{timestamp}]{safetyStatus}{tlsStatus} {method} request to {url}{logExtra}{logDefaults}'
            self.logger.info(logBase)

    # ***********************************************************************************************************************
    # *                                                 Header Related Stuff                                                *
    # ***********************************************************************************************************************

    @staticmethod
    def headerGenerate(customHeaders: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
        """
        Generates headers for the session with optional custom values.

        Parameters
        ----------
        customHeaders : Optional[Dict[str, Any]], optional
            A dictionary of headers to include or override the default headers. By default, None.

        Returns
        -------
        Dict[str, str]
            A dictionary of the generated headers, including both default headers and any custom headers provided.

        Default Header Generation
        -------------------------
        >>> chromeMajors = list(range(110, 126))
        >>> SecCHUAPlatform = ["Windows", "Macintosh", "X11"]
        >>> platforms = [
        ...     "Windows NT 10.0; Win64; x64",
        ...     "Windows NT 6.1; Win64; x64",
        ...     "Macintosh; Intel Mac OS X 10_15_7",
        ...     "Macintosh; Intel Mac OS X 11_2_3",
        ...     "X11; Linux x86_64",
        ...     "X11; Ubuntu; Linux x86_64",
        ... ]

        >>> randPlatform = random.choice(platforms)
        >>> randSecCHUAPlatform = random.choice(SecCHUAPlatform)
        >>> randChromeMajors = random.choice(chromeMajors)

        >>> if not customHeaders:
        >>>     customHeaders = {}

        Default Header
        --------------
        >>> defaultHeader = {
        ...     HeaderKeys.ACCEPT.value: "application/x-www-form-urlencoded",
        ...     HeaderKeys.CONTENT_TYPE.value: "application/x-www-form-urlencoded",
        ...     HeaderKeys.SEC_CH_UA.value: f'"Google Chrome";v="{randChromeMajors}", "Chromium";v="{randChromeMajors}", "Not.A/Brand";v="24"',
        ...     HeaderKeys.SEC_CH_UA_MOBILE.value: "?0",
        ...     HeaderKeys.SEC_CH_UA_PLATFORM.value: f'"{randSecCHUAPlatform}"',
        ...     HeaderKeys.SEC_FETCH_DEST.value: "empty",
        ...     HeaderKeys.SEC_FETCH_MODE.value: "cors",
        ...     HeaderKeys.SEC_FETCH_SITE.value: "same-site",
        ...     HeaderKeys.USER_AGENT.value: f"Mozilla/5.0 ({randPlatform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{randChromeMajors}.0.0.0 Safari/537.36"
        ... }

        Example
        -------
        >>> from secureRequests import HeaderKeys
        >>> from secureRequests import SecureRequests
        >>> customHeaders = {HeaderKeys.CONTENT_TYPE.value: "application/json", HeaderKeys.AUTHORIZATION.value: "Bearer Token"}
        >>> # Directly genereate them on creation
        >>> sr = SecureRequests(headers=customHeaders)
        >>> # Regenerate a needed one works aswell
        >>> headers = secureRequests.headerGenerate(customHeaders=customHeaders)
        >>> print(sr.headers)
        >>> {
        ... 'Accept': 'application/x-www-form-urlencoded', 
        ... 'Authorization': 'Bearer Token',
        ... 'Content-Type': 'application/json', 
        ... 'Sec-CH-UA': '"Google Chrome";v="120", "Chromium";v="120", "Not.A/Brand";v="24"', 
        ... 'Sec-CH-UA-Mobile': '?0', 
        ... 'Sec-CH-UA-Platform': '"Windows"', 
        ... 'Sec-Fetch-Dest': 'empty', 
        ... 'Sec-Fetch-Mode': 'cors', 
        ... 'Sec-Fetch-Site': 'same-site', 
        ... 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        """
        chromeMajors = list(range(110, 126))
        SecCHUAPlatform = ["Windows", "Macintosh", "X11"]
        platforms = [
            "Windows NT 10.0; Win64; x64",
            "Windows NT 6.1; Win64; x64",
            "Macintosh; Intel Mac OS X 10_15_7",
            "Macintosh; Intel Mac OS X 11_2_3",
            "X11; Linux x86_64",
            "X11; Ubuntu; Linux x86_64",
        ]

        randPlatform = random.choice(platforms)
        randSecCHUAPlatform = random.choice(SecCHUAPlatform)
        randChromeMajors = random.choice(chromeMajors)

        if not customHeaders:
            customHeaders = {}

        defaultHeader = {
            HeaderKeys.ACCEPT.value: "application/x-www-form-urlencoded",
            HeaderKeys.CONTENT_TYPE.value: "application/x-www-form-urlencoded",
            HeaderKeys.SEC_CH_UA.value: f'"Google Chrome";v="{randChromeMajors}", "Chromium";v="{randChromeMajors}", "Not.A/Brand";v="24"',
            HeaderKeys.SEC_CH_UA_MOBILE.value: "?0",
            HeaderKeys.SEC_CH_UA_PLATFORM.value: f'"{randSecCHUAPlatform}"',
            HeaderKeys.SEC_FETCH_DEST.value: "empty",
            HeaderKeys.SEC_FETCH_MODE.value: "cors",
            HeaderKeys.SEC_FETCH_SITE.value: "same-site",
            HeaderKeys.USER_AGENT.value: f"Mozilla/5.0 ({randPlatform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{randChromeMajors}.0.0.0 Safari/537.36"
        }
        headers = {key: customHeaders.get(key, defaultValue) for key, defaultValue in defaultHeader.items()}

        # Add any custom headers that are not in the default set
        for key, value in customHeaders.items():
            if key not in headers:
                headers[key] = value

        return headers

    def headerSetKey(self, key: HeaderKeys, value: str) -> None:
        """
        Sets a specific header key to a given value.

        Parameters
        ----------
        key : HeaderKeys
            The header key to set.
        value : str
            The value to set for the header key.

        Returns
        -------
        None

        Example
        -------
        >>> headers = {"Content-Type": "application/json"}
        >>> MyClass.headerSetKey(HeaderKeys.AUTHORIZATION, "Bearer token123")
        >>> print(headers)
        {'Content-Type': 'application/json', 'Authorization': 'Bearer token123'}
        """
        self.headers[key.value] = value

    def headerRemoveKey(self, key: HeaderKeys) -> None:
        """
        Removes a specific header key.

        Parameters
        ----------
        key : HeaderKeys
            The header key to remove.

        Returns
        -------
        None

        Example
        -------
        >>> headers = {"Content-Type": "application/json", "Authorization": "Bearer token123"}
        >>> MyClass.headerRemoveKey(HeaderKeys.AUTHORIZATION)
        >>> print(headers)
        {'Content-Type': 'application/json'}
        """
        if key.value in self.headers:
            del self.headers[key.value]

    def headerUpdateMultiple(self, newHeader: Dict[HeaderKeys, str]) -> None:
        """
        Updates specific headers based on the provided dictionary.

        Parameters
        ----------
        newHeader : Dict[HeaderKeys, str]
            The new headers to update, where keys are of type HeaderKeys.

        Returns
        -------
        None

        Example
        -------
        >>> headers = {"Content-Type": "application/json"}
        >>> MyClass.headerUpdateMultiple({HeaderKeys.AUTHORIZATION: "Bearer token123", HeaderKeys.ACCEPT: "application/xml"})
        >>> print(headers)
        {'Content-Type': 'application/json', 'Authorization': 'Bearer token123', 'Accept': 'application/xml'}
        """
        for key, value in newHeader.items():
            self.headers[key.value] = value

    def headerRemoveMultiple(self, keys: List[HeaderKeys]) -> None:
        """
        Removes multiple header keys at once.

        Parameters
        ----------
        keys : List[HeaderKeys]
            The list of header keys to remove.

        Returns
        -------
        None

        Example
        -------
        >>> headers = {"Content-Type": "application/json", "Authorization": "Bearer token123", "Accept": "application/xml"}
        >>> MyClass.headerRemoveMultiple([HeaderKeys.AUTHORIZATION, HeaderKeys.ACCEPT])
        >>> print(headers)
        {'Content-Type': 'application/json'}
        """
        for key in keys:
            if key.value in self.headers:
                del self.headers[key.value]


    # ***********************************************************************************************************************
    # *                                                 Cookie Related Stuff                                                *
    # ***********************************************************************************************************************

    def _serializeCookieInfo(self, cookieInfo: Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]) -> str:
        """
        Serializes the cookie attributes into a string.

        Args:
            cookieInfo (Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]): 
                A dictionary containing cookie attributes.

        Returns:
            str: A serialized string of cookie attributes.
        """
        return '|'.join(f'{str(key)}={value}' for key, value in cookieInfo.items())

    def _deserializeCookieInfo(self, cookieInfoStr: str) -> Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]:
        """
        Deserializes the string back into a dictionary of cookie attributes.

        Args:
            cookieInfoStr (str): A serialized string of cookie attributes.

        Returns:
            Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]: 
                A dictionary containing cookie attributes.
        """
        items = cookieInfoStr.split('|')
        cookieInfo = {}
        for item in items:
            if '=' in item:
                key, value = item.split('=', 1)
                try:
                    key = CookieAttributeKeys(key)
                except ValueError:
                    pass
                cookieInfo[key] = value
            else:
                logging.warning(f"Skipping invalid cookie attribute '{item}'")
        return cookieInfo

    def cookieUpdate(self, key: CookieKeys, cookieInfo: Union[str, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None:
        """
        Sets or updates a single cookie with specified attributes.

        Args:
            key (CookieKeys): The key of the cookie to update.
            cookieInfo (Union[str, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]): 
                The cookie attributes to set or update.
        """
        if isinstance(cookieInfo, str):
            cookieInfo = self._deserializeCookieInfo(cookieInfo)
        
        cookieValue = self._serializeCookieInfo(cookieInfo)
        self.session.cookies.set(str(key), cookieValue)

    def cookieGet(self, key: CookieKeys) -> Optional[Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]:
        """
        Retrieves the attributes of a single cookie.

        Args:
            key (CookieKeys): The key of the cookie to retrieve.

        Returns:
            Optional[Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]: 
                A dictionary containing the cookie attributes, or None if the cookie does not exist.
        """
        cookieValue = self.session.cookies.get(str(key))
        if cookieValue:
            return self._deserializeCookieInfo(cookieValue)
        return None

    def cookieRemove(self, key: CookieKeys) -> None:
        """
        Removes a single cookie.

        Args:
            key (CookieKeys): The key of the cookie to remove.
        """
        self.session.cookies.pop(str(key), None)

    def cookieUpdateMultiple(self, cookies: Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None:
        """
        Adds or updates multiple cookies at once.

        Args:
            cookies (Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]): 
                A dictionary containing multiple cookies and their attributes.
        """
        for key, cookieInfo in cookies.items():
            self.cookieUpdate(key, cookieInfo)

    def cookieGetAll(self) -> Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]:
        """
        Retrieves all cookies with their attributes.

        Returns:
            Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]: 
                A dictionary containing all cookies and their attributes.
        """
        allCookies = {}
        for cookie in self.session.cookies:
            key = CookieKeys(cookie.name)
            cookieInfo = self._deserializeCookieInfo(cookie.value)
            allCookies[key] = cookieInfo
        return allCookies