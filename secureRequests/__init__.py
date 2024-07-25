"""
secureRequests Package

This package provides secureRequest handling utilities and configurations.
It includes the following modules and components:

Modules:
- secureRequests: Main class for making secureRequests.
- secureRequestsConfig: Configuration settings for secureRequests.
- secureRequestsDecorators: Decorators for handling HTTP responses.
- secureRequestsEnums: Enumerations for headers, cookies, and cookie attributes.
- secureRequestsExceptions: Custom exceptions used in the package.

Components:
- config: Configuration object for secureRequests.
- SecureRequests: Class for making secureRequests.
- handleResponse: Decorator for handling responses.
- HeaderKeys: Enumeration for header keys.
- CookieKeys: Enumeration for cookie keys.
- CookieAttributeKeys: Enumeration for cookie attribute keys.
- srExceptions: Module containing custom exceptions.

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki
# GitHub Usage Examples: https://github.com/JulianStiebler/secureRequests/wiki/6-%E2%80%90-Usage-Examples
"""

from .secureRequestsConfig import config
from .secureRequests import SecureRequests
from .secureRequestsDecorators import handleResponse
from .secureRequestsEnums import HeaderKeys, CookieKeys, CookieAttributeKeys
from . import secureRequestsExceptions as srExceptions

__all__ = [
    'SecureRequests', 'config', 'handleResponse',
    'srExceptions', 
    'CookieAttributeKeys', 'HeaderKeys', 'CookieKeys'
    ]
