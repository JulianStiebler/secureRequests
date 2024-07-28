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
        - _logMessage: Logs a message with a specified level and [category].
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


Usage Examples
--------------
>>> from secureRequests import SecureRequests
>>> print(headers)

>>> sr = SecureRequests(headers={"Content-Type": "application/json"})
>>> sr.headerSetKey(HeaderKeys.AUTHORIZATION, "Bearer token123")
>>> sr.cookieUpdate(CookieKeys.SESSION_ID, {
...     CookieAttributeKeys.DOMAIN: 'example.com',
...     CookieAttributeKeys.PATH: '/',
...     CookieAttributeKeys.EXPIRES: datetime.now() + timedelta(days=7),
...     CookieAttributeKeys.SECURE: True
... })
>>> response = sr.makeRequest("https://httpbin.org/get")
->> [15.07.2024 12:00:00][SAFE][TLS] GET request to https://httpbin.org/get with headers ...
>>> print(response.status_code)
>>> print(response.reason)
>>> print(response.text)

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki

# Created: 15.07.2024
# Last edited: 28.07.2024
"""

from os.path import exists as PathExists
from os.path import join as PathJoin
import requests
import ssl
import warnings
import logging
import random
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
from hashlib import sha256

from typing import Dict, Any, Optional, List, Union
from .secureRequestsConfig import config
from .secureRequestsDecorators import handleResponse
from .secureRequestsEnums import HeaderKeys, CookieKeys, CookieAttributeKeys

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
        self, SSLContext: Optional[ssl.SSLContext] = None, **kwargs: Any
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
        self.SSLContext = SSLContext
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
        context = self.SSLContext or self._createSSLCOntext()
        kwargs['ssl_context'] = context
        super().init_poolmanager(*args, **kwargs)

    def _createSSLCOntext(self) -> ssl.SSLContext:
        """
        Creates a default SSL context with specific cipher settings.

        Returns
        -------
        ssl.SSLContext
            The default SSL context with specific cipher settings.
        
        """
        context = ssl.create_default_context()
        context.set_ciphers('HIGH:!DH:!aNULL')
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
    logger : logging.Logger
        The logger object for logging messages. Only available if `logToFile` is set to True.
        Named 'SecureRequests'
    verify : Union[bool, str]
        The path to the SSL certificate file or False if not using SSL.

    Methods
    -------
    _certificateFetch(self, force:bool=False, verifyChecksum:Union[bool, str]=False) -> None:
        Fetches the SSL certificate if required. 
        Optionally verifies the checksum of the fetched certificate, given a string - or if True, fetches the checksum file from curl.se.
    makeRequest(url:str, method:str = "GET", headers:Optional[Dict[str, str]] = None, **kwargs) -> requests.Response:
        Makes an HTTP request with the specified parameters.
    _logRequest(method:str, url:str, response:requests.Response, **kwargs:Any) -> None:
        Logs an HTTP request and response details.
    _logMessage(message:str, level:Union[str, int]="DEBUG", category:str = ""):
        Logs a message with the specified logging level and category.
    headerGenerate(customHeaders: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
        Generates default headers with optional custom values.
    headerSetKey(key: HeaderKeys, value: str) -> None:
        Sets a specific header key to a given value.
    headerRemoveKey(key: HeaderKeys) -> None:
        Removes a specific header key.
    headerUpdateMultiple(newHeader: Dict[HeaderKeys, str]) -> None:
        Updates multiple headers based on the provided dictionary.
    headerRemoveMultiple(keys: List[HeaderKeys]) -> None:
        Removes multiple header keys at once.
    _serializeCookieInfo(cookieInfo: Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]) -> str:
        Serializes the cookie attributes into a string.
    _deserializeCookieInfo(cookieInfoStr: str) -> Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]:
        Deserializes the string back into a dictionary of cookie attributes.
    cookieUpdate(key: CookieKeys, cookieInfo: Union[str, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None:
        Sets or updates a single cookie with specified attributes.
    cookieGet(key: CookieKeys) -> Optional[Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]:
        Retrieves the attributes of a single cookie.
    cookieRemove(key: CookieKeys) -> None:
        Removes a single cookie.
    cookieUpdateMultiple(cookies: Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None:
        Adds or updates multiple cookies at once.
    cookieGetAll() -> Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]:
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
            certificateVerifyChecksum: Optional[Union[bool, str]] = None,
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

        # ----------------------------------------------- Certificate Related Stuff -----------------------------------------------
        self.certificateURL = certificateURL if certificateURL else config.getCertificateURL()
        self.certificatePath = certificatePath if certificatePath else config.getCertificatePath()
        self.certificateVerifyChecksum = certificateVerifyChecksum if certificateVerifyChecksum is not None else config.getCertificateVerifyChecksum()

        # ------------------------------------------ Initialize Config Related Variables ------------------------------------------

        # Initialize attributes, falling back to config if not provided
        self.logToFile = logToFile if logToFile is not None else config.getLogToFile()
        self.logLevel = logLevel if logLevel is not None else config.getLogLevel()
        self.logPath = logPath if logPath is not None else config.getLogPath()
        self.logExtensive = logExtensive if logExtensive is not None else config.getLogExtensive()
        self.silent = silent if silent is not None else config.getSilent()
        self.suppressWarnings = suppressWarnings if suppressWarnings is not None else config.getSuppressWarnings()
        
        self.headers = self.headerGenerate(headers)
        if useEnv:
            config.EVarSetMode(True)
            if customEnvVars:
                config.EVarSet(customEnvVars)

        if self.logToFile:
            handler = logging.FileHandler(self.logPath)
            self.logger = logging.getLogger('SecureRequests')
            self.logger.setLevel(self.logLevel)
            self.logger.addHandler(handler)

        if self.silent:
            logging.disable()

        if self.suppressWarnings:
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)

        self.fetchCertificate = certificateNeedFetch if certificateNeedFetch is not None else config.getCertificateNeedFetch()
        if self.fetchCertificate:
            self._certificateFetch(verifyChecksum=self.certificateVerifyChecksum)
        self.verify = self._certificateSet()

    def _logMessage(self, message:str, level:Union[str, int]="DEBUG", category:str = ""):
        """
        Logs a message using the instance's logger at the specified logging level.
        
        Parameters
        ----------
        level : str
            The logging level (e.g., 'debug', 'info', 'warning', 'error').
        message : str, optional
            The message to log. Defaults to "DEBUG"
        category : str, optional

        Output
        ------
        ->> [15.07.2024 12:00:00][DEBUG][Category] Message
        """
        if hasattr(self, 'logger'):
            timestamp = self.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logFunction = getattr(self.logger, level, None)
            category = f"[{category}]" if category else ""
            if callable(logFunction):
                logFunction(f"[{timestamp}][{level.upper()}]{category} {message}")

    # ***********************************************************************************************************************
    # *                                            Certificate Related Stuff                                                *
    # ***********************************************************************************************************************

    def _certificateFetch(self, force:bool=False, verifyChecksum:Union[bool, str]=False) -> None:
        """
        Fetches a certificate from the configured URL and saves it to the local file system.

        Parameters
        ----------
        force : bool, optional
            If True, forces fetching the certificate even if it already exists. 
            Default is False.
        verifyChecksum : Union[bool, str], optional
            If True, verifies the SHA-256 checksum of the fetched certificate. 
            Default is False.

        Helper Functions
        ----------------
        __fetchChecksum() -> str:
            Fetches the checksum of the certificate.
        __verifyCertificate(content:Any, expectedChecksum:str) -> bool:
            Verifies the checksum of the fetched certificate.

        Returns
        -------
        None

        Logs
        ----
        ->> [15.07.2024 12:00:00][INFO][Certificate] Fetching checksum of the certificate.
        ->> [15.07.2024 12:00:00][ERROR][Certificate] Unexpected checksum format.
        ->> [15.07.2024 12:00:00][INFO][Certificate] Verifying checksum of the fetched certificate.
        ->> [15.07.2024 12:00:00][INFO][Certificate] Calculated checksum: 1234567890
        ->> [15.07.2024 12:00:00][INFO][Certificate] Expected checksum: 1234567890
        ->> [15.07.2024 12:00:00][ERROR][Certificate] Checksum verification failed.
        ->> [15.07.2024 12:00:00][INFO][Certificate] Checksum verification successful.
        ->> [15.07.2024 12:00:00][ERROR][Certificate] Failed to obtain expected checksum.
        ->> [15.07.2024 12:00:00][ERROR][Certificate] Failed to fetch certificate. Cannot use SSL but the program might work.
        ->> [15.07.2024 12:00:00][DEBUG][Certificate] Certificate exists and setting it to use.
        ->> [15.07.2024 12:00:00][CRITICAL][Certificate] Certificate does not exist. Fetching it.
        ->> [15.07.2024 12:00:00][INFO][Certificate] Successfully fetched certificate and saved.
        ->> [15.07.2024 12:00:00][ERROR][Certificate] Fetched certificate is empty.
        """

        """Fetches the checksum of the certificate."""
        def __fetchChecksum():
            try:
                self._logMessage("Fetching checksum of the certificate.", "info", "Certificate")
                response = self.makeRequest('https://curl.se/ca/cacert.pem.sha256')
                if response.status_code == 200:
                    checksum = response.text.split()
                    if len(checksum) == 2:
                        return checksum[0]
                    self._logMessage("Unexpected checksum format.", "error", "Certificate")
            except Exception as e:
                self._logMessage(f"Exception occurred while fetching checksum: {e}", "error", "Certificate")
            return None

        """Verifies the checksum of the fetched certificate."""
        def __verifyCertificate(content:Any, expectedChecksum:str) -> bool:
            sha256Hash = sha256()
            sha256Hash.update(content)
            calculatedHash = sha256Hash.hexdigest()
            self._logMessage(f"Calculated checksum: {calculatedHash}", "info", "Certificate")
            self._logMessage(f"Expected checksum: {expectedChecksum}", "info", "Certificate")
            return calculatedHash == expectedChecksum


        if self.pathExists(self.certificatePath):
            self.verify = self.certificatePath
            self._logMessage("Certificate exists and setting it to use.", "debug", "Certificate")
            if not force:
                return
        else:
            self._logMessage("Certificate does not exist. Fetching it.", "critical", "Certificate")

        try:
            response = self.makeRequest(self.certificateURL, method="GET", redactURL=True)
            if response.status_code == 200:
                content = response.content
                # If checksum verification is enabled, fetch the checksum and verify it
                # If its a string or True
                if verifyChecksum:
                    self._logMessage("Verifying checksum of the fetched certificate.", "info", "Certificate")
                    # Use either the given string if its not a bool or fetch the checksum file
                    expectedChecksum = __fetchChecksum() if isinstance(verifyChecksum, bool) else verifyChecksum
                    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    if expectedChecksum:
                        verify = __verifyCertificate(content, expectedChecksum)
                        if not verify:
                            print(">>>>>>>>>>>>failed")
                            self._logMessage("Checksum verification failed.", "error", "Certificate")
                            return
                        else:
                            print(">>>>>>>>>>>worked")
                            self._logMessage("Checksum verification successful.", "info", "Certificate")
                    else:
                        self._logMessage("Failed to obtain expected checksum.", "error", "Certificate")
                        return
                    
                if not content:
                    self._logMessage("Fetched certificate is empty.", "error", "Certificate")
                    return
                
                with open(self.certificatePath, "wb") as f:
                    f.write(content)

                self._logMessage("Successfully fetched certificate and saved.", "info", "Certificate")
                self.verify = self.certificatePath
        except Exception as e:
            self._logMessage(
                f"Failed to fetch certificate. Cannot use SSL but the program might work.\n{e}", "critical", "Certificate"
            )
            self.verify = False

    def _certificateSet(self) -> Union[bool, str]:
        """
        Sets the certificate path if not in unsafe mode and the certificate file exists.

        Returns
        -------
        >>> self._certificateSet()
        ... '/path/to/certificate.pem'   # if certificate is set
        ... False                        # if certificate is not set or in unsafe mode

        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Certificate] Setting certificate. Status: /path/to/certificate.pem
        """
        certificateStatus = (
            self.certificatePath
            if not self.unsafe and self.pathExists(self.certificatePath)
            else False
        )
        self._logMessage(f"Setting certificate. Status: {certificateStatus}", "debug", "Certificate")
        return certificateStatus

    # ***********************************************************************************************************************
    # *                                                       Request Logic                                                 *
    # ***********************************************************************************************************************

    @handleResponse
    def makeRequest(
        self,
        url:str,
        method:str="GET",
        headers:Optional[Dict[str, str]]=None,
        redactURL=False,
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
        headers : dict, optional
            Custom headers to include with the request. Defaults to None.
        **kwargs : Any
            >>> METHOD: get
                *,
                data: _Data  = None,
                params: dict = None,
                cookies: dict = None,
                files: dict = None,
                auth: tuple = None,
                timeout: Union[float, tuple] = None,
                allow_redirects: bool = True,
                proxies: dict = None,
                hooks: dict = None,
                stream: bool = False,
                cert: Union[str, tuple]  = None,
                json: dict = None
            >>> METHOD: post
                *,
                data: _Data  = None,
                json: dict = None,
                params: dict = None,
                cookies: dict = None,
                files: dict = None,
                auth: tuple  = None,
                timeout: Union[float, tuple] = None,
                allow_redirects: bool = True,
                proxies: dict = None,
                hooks: dict = None,
                stream: bool = False,
                cert: Union[str, tuple] = None
            >>> METHOD: put
                *,
                params: dict = None,
                cookies: dict = None,
                files: dict = None,
                auth: tuple = None,
                timeout: Union[float, tuple] = None,
                allow_redirects: bool = True,
                proxies: dict = None,
                hooks: dict = None,
                stream: bool = False,
                cert: Union[str, tuple] = None,
                json: dict = None
            >>> METHOD: delete
                *,
                data: _Data = None,
                params: dict = None,
                headers: dict = None,
                cookies: dict = None,
                files: dict = None,
                auth: tuple = None,
                timeout: Union[float, tuple] = None,
                allow_redirects: bool = True,
                proxies: dict = None,
                hooks: dict = None,
                stream: bool = False,
                cert: Union[str, tuple] = None,
                json: dict = None
            >>> METHOD: patch
                *,
                data: _Data = None,
                params: _Params = None,
                cookies: Union[RequestsCookieJar, _TextMapping] = None,
                files: _Files = None,
                auth: _Auth = None,
                timeout: _Timeout = None,
                allow_redirects: bool = True,
                proxies: _TextMapping = None,
                hooks: _HooksInput = None
                stream: bool = None,
                cert: _Cert = None,
                json: Any = None

        Returns
        -------
        >>> requests.Response
        ... # The HTTP response.

        Logs
        ----
        ->> [15.07.2024 12:00:00][REQUEST][SAFE][TLS] GET request to https://httpbin.org/get with headers ...
        ->> [15.07.2024 12:00:00][REQUEST][UNSAFE][TLS] POST request to https://httpbin.org/post with headers ...
        ->> [15.07.2024 12:00:00][REQUEST][SAFE][NO TLS] PUT request to https://httpbin.org/put with headers ...
        ->> [15.07.2024 12:00:00][REQUEST][UNSAFE][NO TLS] DELETE request to https://httpbin.org/delete with headers ...

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
            url=url, headers=headers, verify=self.verify, **kwargs
        )
        if redactURL:
            url = "[REDACTED]"
        self._logRequest(method, url, response=response, headers=headers)
        return response

    def _logRequest(self, method:str, url:str, response:requests.Response, **kwargs:Any) -> None:
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
        ->> [15.07.2024 12:00:00][REQUEST][SAFE][TLS] GET request to https://example.com/api/data ...
        """
        if hasattr(self, "logger"):
            timestamp = self.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            safetyStatus = "[UNSAFE]" if not self.verify else "[SAFE]"
            tlsStatus = "[TLS]" if self.useTLS else "[NO TLS]"
            logExtra = f' with headers {kwargs.get("headers")} and params {kwargs}' if self.logExtensive else ''
            logDefaults = f' with Status Code {response.status_code} - {response.reason}'
            logBase = f'[{timestamp}][REQUEST]{safetyStatus}{tlsStatus} {method} request to {url}{logExtra}{logDefaults}'
            if response.status_code == 200:
                self.logger.info(logBase)
            else:
                self.logger.error(logBase)

    # ***********************************************************************************************************************
    # *                                                 Header Related Stuff                                                *
    # ***********************************************************************************************************************

    def headerGenerate(self, customHeaders:Optional[Dict[str, Any]]=None) -> Dict[str, str]:
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

        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Header] Added custom headers to the default set.
        ->> [15.07.2024 12:00:00][DEBUG][Header] Custom headers: {'Content-Type': 'application', ... }
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

        if self.logExtensive:
            self._logMessage("Added custom headers to the default set.", "debug", "Header")
            self._logMessage(f"Custom headers: {headers}", "debug", "Header")
        return headers
    

    def headerSetKey(self, key:HeaderKeys, value:str) -> None:
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

        Logs
        ->> [15.07.2024 12:00:00][DEBUG][Header] Set Authorization to Bearer token123
        """
        self.headers[key.value] = value
        self._logMessage(f"Set {key} to {value}", "debug", "Header")

    def headerRemoveKey(self, key:HeaderKeys) -> None:
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

        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Header] Removed key AUTHORIZATION from headers.
        """
        if key.value in self.headers:
            del self.headers[key.value]
            self._logMessage(f"Removed key {key} from headers.", "debug", "Header")

    def headerUpdateMultiple(self, newHeader:Dict[HeaderKeys, str]) -> None:
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

        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Header] Updated Key 'AUTHORIZATION' with Value 'Value'
        """
        for key, value in newHeader.items():
            self.headers[key.value] = value
            self._logMessage(f"Updated Key '{key}' with Value '{value}'", "debug", "Header")

    def headerRemoveMultiple(self, keys:List[HeaderKeys]) -> None:
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

        Logs
        ->> [15.07.2024 12:00:00][DEBUG][Header] Removed key AUTHORIZATION from headers.
        ->> [15.07.2024 12:00:00][DEBUG][Header] Removed key ACCEPT from headers.
        """
        for key in keys:
            if key.value in self.headers:
                del self.headers[key.value]
                self._logMessage(f"Removed key {key} from headers.", "debug", "Header")


    # ***********************************************************************************************************************
    # *                                                 Cookie Related Stuff                                                *
    # ***********************************************************************************************************************

    def _serializeCookieInfo(self, cookieInfo:Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]) -> str:
        """
        Serializes the cookie attributes into a string.

        Args
        ----
            cookieInfo (Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]): 
                A dictionary containing cookie attributes.

        Returns
        -------
            str: A serialized string of cookie attributes.
        """
        return '|'.join(f'{str(key)}={value}' for key, value in cookieInfo.items())

    def _deserializeCookieInfo(self, cookieInfoStr:str) -> Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]:
        """
        Deserializes the string back into a dictionary of cookie attributes.

        Args
        ----
            cookieInfoStr (str): A serialized string of cookie attributes.

        Returns
        -------
            Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]: 
                A dictionary containing cookie attributes.

        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Cookie] Invalid cookie attribute 'invalid'
        ->> [15.07.2024 12:00:00][DEBUG][Cookie] Skipping invalid cookie attribute 'invalid'
        """
        items = cookieInfoStr.split('|')
        cookieInfo = {}
        for item in items:
            if '=' in item:
                key, value = item.split('=', 1)
                try:
                    key = CookieAttributeKeys(key)
                except ValueError:
                    self._logMessage(f"Invalid cookie attribute '{item}'", "debug", "Cookie")
                cookieInfo[key] = value
            else:
                self._logMessage(f"Skipping invalid cookie attribute '{item}'", "debug", "Cookie")
        return cookieInfo

    def cookieUpdate(self, key:CookieKeys, cookieInfo:Union[str, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None:
        """
        Sets or updates a single cookie with specified attributes.

        Args
        ----
        key (CookieKeys): The key of the cookie to update.
        cookieInfo (Union[str, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]): 
                The cookie attributes to set or update.
        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Cookie] Set cookie 'key' to 'cookieInfo'
        """
        if isinstance(cookieInfo, str):
            cookieInfo = self._deserializeCookieInfo(cookieInfo)
        
        cookieValue = self._serializeCookieInfo(cookieInfo)
        self.session.cookies.set(str(key), cookieValue)
        self._logMessage(f"Set cookie {key} to {cookieInfo}", "debug", "Cookie")

    def cookieGet(self, key:CookieKeys) -> Optional[Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]:
        """
        Retrieves the attributes of a single cookie.

        Args
        ----
            key (CookieKeys): The key of the cookie to retrieve.

        Returns
        -------
        Optional[Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]: 
            A dictionary containing the cookie attributes, or None if the cookie does not exist.
        None if none
        """
        cookieValue = self.session.cookies.get(str(key))
        if cookieValue:
            return self._deserializeCookieInfo(cookieValue)
        return None

    def cookieRemove(self, key:CookieKeys) -> None:
        """
        Removes a single cookie.

        Args
        ----
            key (CookieKeys): The key of the cookie to remove.

        Logs
        ----
        ->> [15.07.2024 12:00:00][DEBUG][Cookie] Removed cookie 'key'
        """
        self.session.cookies.pop(str(key), None)
        self._logMessage(f"Removed cookie {key}", "debug", "Cookie")

    def cookieUpdateMultiple(self, cookies:Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]) -> None:
        """
        Adds or updates multiple cookies at once.

        Args
        ----
            cookies (Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]): 
                A dictionary containing multiple cookies and their attributes.
        """
        for key, cookieInfo in cookies.items():
            self.cookieUpdate(key, cookieInfo)

    def cookieGetAll(self) -> Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]:
        """
        Retrieves all cookies with their attributes.

        Returns
        -------
        Dict[CookieKeys, Dict[Union[CookieAttributeKeys, str], Union[str, bool, int, datetime]]]: 
            A dictionary containing all cookies and their attributes.
        """
        allCookies = {}
        for cookie in self.session.cookies:
            key = CookieKeys(cookie.name)
            cookieInfo = self._deserializeCookieInfo(cookie.value)
            allCookies[key] = cookieInfo
        return allCookies