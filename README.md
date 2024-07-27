# secureRequests

![Stars][Badge Stars] ![Watcher][Badge Watchers] ![Forks][Badge Forks]

A simple library designed to make secure HTTPs requests more widespread with flexibility in SSL certificate management. 
This library wraps a TSL Adapter around the session.request-methods and helps with certificate, cookie and header management. 

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
- [Wiki & Documentation][Resource Wiki]
- [Unit Test Results][MD UnitTestResult]
- [Roadmap][MD Roadmap]

---
## Table of Contents
- [General Information](#general-information)
  - [Example](#example)
  - [Features](#features)
  - [Configuration Optionss](#configuration-options)
- [Installation](#installation)
  - [Install Locally from Source](#install-locally-from-source)
  - [Install From PyPi](#install-from-pypi)
- [Acknowledgments](#acknowledgments)

# General Information

> Depends only on `requests`, `os.path.exists`, `os.path.join` and `datetime` (for header & cookie values).

## Example

```python
from datetime import datetime, timedelta
# Import library
from secureRequests import SecureRequests
from secureRequests import HeaderKeys, CookieKeys, CookieAttributeKeys


# Initialize secureRequests with a custom header value
sr = SecureRequests(headers={HeaderKeys.CONTENT_TYPE.value: "application/json"})
# Set another key extra, couldve done earlier but to demonstrate
sr.headerSetKey(HeaderKeys.AUTHORIZATION, "Bearer token123")
# Add cookies
sr.cookieUpdate(CookieKeys.SESSION_ID, {
    CookieAttributeKeys.PATH: '/',
    CookieAttributeKeys.EXPIRES: datetime.now() + timedelta(days=7),
    CookieAttributeKeys.SECURE: True
})
# Print our example data
print(sr.headers)
print(sr.cookieGetAll())

# Make the request
response = sr.makeRequest("https://httpbin.org/get")
print(response.status_code)

# This was an SSL encrypted, with TSL adapter mounted request. How easy right!
```

## Features

- **Flexible SSL Certificate Management:** Can automatically fetch and manage SSL certificates or allows manual configuration.
- **Custom Exceptions:** Uses custom exceptions to print out responses so you can try/catch/finalize your responses very easily.
- **Easy Headers:** Generates valid HTTP header to mimic different browsers and platforms for enhanced security or accept custom ones powered with enums.
- **Easy Cookies:** Generates cookies as needed/specified powered by enums.
- **Request Logging:** Optional logging to file for tracking request details and responses.
- **Secure and Easy Request Method:** Supports standard HTTP methods (GET, POST, PUT, DELETE, PATCH) with customizable payloads and headers.

## Configuration Options
The SecureRequests class constructor accepts the following optional parameters, they can also be set via the config module.
```python
- requests: Either uses passed in or imports it itself
- os: Either uses passed in or imports it itself
- useEnv: If True uses environment variables for the certificate and config # Not yet
- customEnvVars: If True uses custom specified Environment Variables # Not yet
- headers: If not specified generates one, otherwise accepts a valid header
- useTLS: Enables or disables TLS/SSL.
- unsafe: Allows unsafe requests (use with caution).
- fetchCert: Automatically fetches SSL certificates.
- logToFile: Enables logging of requests to a file.
- silent: Disables all logging if set to True.
- logLevel: Specifies the log level.
- supressWarnings: Supresses warnings like unsafeRequest # Not yet
- customCert: If specified fetches the custom CERT or uses it from source # Not yet
- session: Can pass in a custom session
- referer: specify a referer which also serves as origin

What not specified will be loaded from config.py, there you can see or set defaults.
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
[MD Security]: ./security.md
[MD UnitTestResult]: ./unitTest/unitTestResults.md
[MD Roadmap]: ./ROADMAP.md
[MD Contributing]: ./CONTRIBUTING.md


<!-- Other Aliases -->
[Resource Wiki]: https://github.com/JulianStiebler/secureRequests/wiki