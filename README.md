# secureRequests

![Stars][Badge Stars] ![Watcher][Badge Watchers] ![Forks][Badge Forks]

The `secureRequests.py` module is designed to enhance the security of HTTP requests made in Python applications by using TLS (Transport Layer Security) adapters and certificates. It aims to help with best practices for certificates, cookie and header management. 
Also provides a easy way to verify requests that gather files with checksums.

![Release Version][Badge Release Version]  ![Release Date][Badge Release Date] ![CodeSize][Badge Code Size]
![Docstring Coverage][Badge Docstring Coverage]

| **Ubuntu** | ![TypeCheck Ubuntu][Badge TypeCheck Ubuntu]              | ![UnitTest Ubuntu][Badge UnitTest Ubuntu]             |
|------------|----------------------------------------------------------|-------------------------------------------------------|
| **Mac**    | ![TypeCheck macOS][Badge TypeCheck macOS]                | ![UnitTest macOS][Badge UnitTest macOS]               |
| **Windows**| ![TypeCheck Windows][Badge TypeCheck Windows]            | ![UnitTest Windows][Badge UnitTest Windows]           |
| **All**    | ![CodeQL Status][Badge CodeQL]                           | ![Ruff Status][Badge Ruff]                            |

![Badge Last Commit][Badge Last Commit] ![Badge Security Policy][Badge Security Policy] ![Badge Open Issues][Badge Open Issues] ![Badge Open Pull Requests][Badge Open Pull Requests] ![Badge Contributors][Badge Contributors]

---

## Resources
- [Why you should use secureRequests - or TSL and Certificates in general - VERY IMPORTANT!][MD Security]
- [Wiki & Documentation][Resource Wiki]
- [Unit Test Results][MD UnitTestResult]
- [Roadmap][MD Roadmap]

---
## Table of Contents
- [General Information](#general-information)
  - [Features](#features)
  - [Configuration Optionss](#configuration-options)
- [Installation](#installation)
  - [Install Locally from Source](#install-locally-from-source)
  - [Install From PyPi](#install-from-pypi)
- [Example Log](#example-log)
- [Acknowledgments](#acknowledgments)

# General Information

> Depends only on `requests`, `os.path.exists`, `os.path.join` and `datetime` (for header & cookie values).

## Features

- **Flexible SSL Certificate Management:** Can automatically fetch and manage SSL certificates or allows manual configuration.
- **Custom Exceptions:** Uses custom exceptions to print out responses so you can try/catch/finalize your responses very easily.
- **Easy Headers:** Generates valid HTTP header to mimic different browsers and platforms for enhanced security or accept custom ones powered with enums.
- **Easy Cookies:** Generates cookies as needed/specified powered by enums.
- **Extensive Logging:** Optional logging to file for tracking request details and responses.
- **Secure and Easy Request Method:** Supports standard HTTP methods (GET, POST, PUT, DELETE, PATCH) with customizable payloads and headers.
- **Verify checksum of certificate**: Verifys the certificate from a given online source or a given string.

## Configuration Options
The SecureRequests class constructor accepts the following optional parameters, they can also be set via the config module.
```
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
```

# Installation

## Install Locally from Source
```bash
git clone https://github.com/JulianStiebler/SecureRequests.git
cd SecureRequests
pip install requests
pip install .
```

## Install from PyPi

> Work in progress

# Example Log

```
[2024-07-28 02:54:20][CRITICAL][Certificate] Certificate does not exist. Fetching it.
[2024-07-28 02:54:20][REQUEST][UNSAFE][TLS] GET request to https://curl.se/ca/cacert.pem with Status Code 200 - OK
[2024-07-28 02:54:20][INFO][Certificate] Verifying checksum of the fetched certificate.
[2024-07-28 02:54:20][INFO][Certificate] Fetching checksum of the certificate.
[2024-07-28 02:54:20][REQUEST][UNSAFE][TLS] GET request to https://curl.se/ca/cacert.pem.sha256 with Status Code 200 - OK
[2024-07-28 02:54:20][INFO][Certificate] Calculated checksum: 1bf458412568e134a4514f5e170a328d11091e071c7110955c9884ed87972ac9
[2024-07-28 02:54:20][INFO][Certificate] Expected checksum: 1bf458412568e134a4514f5e170a328d11091e071c7110955c9884ed87972ac9
[2024-07-28 02:54:20][INFO][Certificate] Checksum verification successful.
[2024-07-28 02:54:20][INFO][Certificate] Successfully fetched certificate and saved.
[2024-07-28 02:54:20][DEBUG][Certificate] Setting certificate. Status: /resources/cacert.pem
[2024-07-28 02:54:22][REQUEST][SAFE][TLS] GET request to https://api.github.com/repos/julianstiebler/secureRequests/releases/latest with Status Code 200 - OK
```

# Acknowledgments
> Built with love by Julian Stiebler

### Refer to our [Wiki](https://github.com/JulianStiebler/secureRequests/wiki)


<!-- Define URL aliases for badges -->
[Badge Stars]: https://img.shields.io/github/stars/JulianStiebler/secureRequests?style=social
[Badge Watchers]: https://img.shields.io/github/watchers/JulianStiebler/secureRequests?style=social
[Badge Forks]: https://img.shields.io/github/forks/JulianStiebler/secureRequests?style=social

[Badge UnitTest Ubuntu]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/unittest.yml?branch=main&os=ubuntu-latest&label=UnitTest&logo=ubuntu&logoColor=white&style=for-the-badge
[Badge UnitTest macOS]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/unittest.yml?branch=main&os=mac-latest&label=UnitTest&logo=apple&logoColor=white&style=for-the-badge
[Badge UnitTest Windows]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/unittest.yml?branch=main&os=windows-latest&label=Win%20UnitTest&logo=windows&logoColor=white&style=for-the-badge

[Badge TypeCheck Ubuntu]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/typecheck.yml?branch=main&os=ubuntu-latest&label=TypeCheck&logo=ubuntu&logoColor=white&style=for-the-badge
[Badge TypeCheck macOS]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/typecheck.yml?branch=main&os=mac-latest&label=TypeCheck&logo=apple&logoColor=white&style=for-the-badge
[Badge TypeCheck Windows]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/typecheck.yml?branch=main&os=windows-latest&label=Win%20TypeCheck&logo=windows&logoColor=white&style=for-the-badge
[Badge CodeQL]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/codeql.yml?branch=main&label=CodeQL&logo=github&logoColor=white&style=for-the-badge
[Badge Ruff]: https://img.shields.io/github/actions/workflow/status/JulianStiebler/secureRequests/codeql.yml?branch=main&label=Ruff%20Lint&logo=ruff&logoColor=white&style=for-the-badge

[Badge Release Version]: https://img.shields.io/github/v/release/JulianStiebler/secureRequests?style=for-the-badge&logo=empty
[Badge Release Date]: https://img.shields.io/github/release-date/JulianStiebler/secureRequests?style=for-the-badge&logo=empty
[Badge Code Size]: https://img.shields.io/github/languages/code-size/JulianStiebler/secureRequests?style=for-the-badge&logo=empty

[Badge Last Commit]: https://img.shields.io/github/last-commit/JulianStiebler/secureRequests?style=for-the-badge&logo=empty
[Badge Security Policy]: https://img.shields.io/badge/Security-Policy-red.svg?style=for-the-badge&logo=empty
[Badge Open Issues]: https://img.shields.io/github/issues-raw/JulianStiebler/secureRequests?style=for-the-badge&logo=empty
[Badge Open Pull Requests]: https://img.shields.io/github/issues-pr-raw/JulianStiebler/secureRequests?style=for-the-badge&logo=empty
[Badge Contributors]: https://img.shields.io/github/contributors/JulianStiebler/secureRequests?style=for-the-badge&logo=empty
[Badge Docstring Coverage]: https://img.shields.io/badge/docstr%20coverage-90%25-blue?style=for-the-badge&logo=empty

[Badge Downloads]: https://img.shields.io/github/downloads/JulianStiebler/secureRequests/total?style=for-the-badge&logo=empty
[Badge License]: https://img.shields.io/github/license/JulianStiebler/secureRequests?style=for-the-badge&logo=empty

<!-- Aliases for Files -->
[MD Security]: ./SECURITY.md
[MD UnitTestResult]: ./unitTest/unitTestResults.md
[MD Roadmap]: ./ROADMAP.md
[MD Contributing]: ./CONTRIBUTING.md


<!-- Other Aliases -->
[Resource Wiki]: https://github.com/JulianStiebler/secureRequests/wiki
