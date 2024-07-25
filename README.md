# SecureRequests

![Stars](https://img.shields.io/github/stars/JulianStiebler/secureRequests?style=social) ![Watchers](https://img.shields.io/github/watchers/JulianStiebler/secureRequests?style=social) ![GitHub Forks](https://img.shields.io/github/forks/JulianStiebler/secureRequests?style=social) 

![Downloads](https://img.shields.io/github/downloads/JulianStiebler/secureRequests/total) [![Security Policy](https://img.shields.io/badge/Security-Policy-red.svg)](https://github.com/JulianStiebler/secureRequests/security/policy) ![Last Commit](https://img.shields.io/github/last-commit/JulianStiebler/secureRequests)
![License](https://img.shields.io/github/license/JulianStiebler/secureRequests) ![Open Issues](https://img.shields.io/github/issues-raw/JulianStiebler/secureRequests)
![Open Pull Requests](https://img.shields.io/github/issues-pr-raw/JulianStiebler/secureRequests) ![Contributors](https://img.shields.io/github/contributors/JulianStiebler/secureRequests)


![TypeCheck Ubuntu](https://github.com/JulianStiebler/secureRequests/actions/workflows/typecheck.yml/badge.svg?branch=main&os=ubuntu-latest) ![TypeCheck macOS](https://github.com/JulianStiebler/secureRequests/actions/workflows/typecheck.yml/badge.svg?branch=main&os=macos-latest) ![TypeCheck Windows](https://github.com/JulianStiebler/secureRequests/actions/workflows/typecheck.yml/badge.svg?branch=main&os=windows-latest)

![UnitTest Ubuntu](https://github.com/JulianStiebler/secureRequests/actions/workflows/unittest.yml/badge.svg?branch=main&os=ubuntu-latest) ![UnitTest macOS](https://github.com/JulianStiebler/secureRequests/actions/workflows/unittest.yml/badge.svg?branch=main&os=macos-latest) ![UnitTest Windows](https://github.com/JulianStiebler/secureRequests/actions/workflows/unittest.yml/badge.svg?branch=main&os=windows-latest)

![CodeQL Status](https://github.com/JulianStiebler/secureRequests/actions/workflows/codeql.yml/badge.svg)  ![Ruff Status](https://github.com/JulianStiebler/secureRequests/actions/workflows/ruff.yml/badge.svg) ![Version](https://img.shields.io/github/v/release/JulianStiebler/secureRequests) ![Release Date](https://img.shields.io/github/release-date/JulianStiebler/secureRequests) ![Code Size](https://img.shields.io/github/languages/code-size/JulianStiebler/secureRequests)  

A simple library designed to make secure HTTP requests more widespread with flexibility in SSL certificate management. Requests use a TSL Adapter and allow easy request execution and configuration with SSLContext and Certificates. Also wraps good practice around the general use of requests.

## Table of Contents

- [Wiki & Documentation](https://github.com/JulianStiebler/secureRequests/wiki)
- [Unit Test Markdown](https://github.com/JulianStiebler/secureRequests/blob/main/unitTest/unitTestResults.md)
- [General Information](#general-information)
  - [Example](#example)
  - [Features](#features)
  - [Configuration Optionss](#configuration-options)
- [Installation](#installation)
  - [Install Locally from Source](#install-locally-from-source)
  - [Install From PyPi](#install-from-pypi)
- [License](#license)
- [Acknowledgments](#acknowledgments)
8. [Changelog](#changelog)

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


# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
> Built with love by Julian Stiebler

### Refer to our [Wiki](https://github.com/JulianStiebler/secureRequests/wiki)
