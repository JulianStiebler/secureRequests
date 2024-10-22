"""
This module defines enumerations for HTTP header keys, cookie keys, and cookie attribute keys. 
These enumerations are used to standardize and manage the various HTTP headers and cookies commonly 
used in web applications.

- HeaderKeys: Contains standard HTTP header fields.
- CookieKeys: Contains common cookie names used for storing various user-related information.
- CookieAttributeKeys: Contains attributes used to define properties of cookies.

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki

# Created: 15.07.2024
# Last edited: 17.07.2024
"""

from enum import Enum
from datetime import datetime

class HeaderKeys(Enum):
    ACCEPT: str
    ACCEPT_ENCODING: str
    ACCEPT_LANGUAGE: str
    ACCESS_CONTROL_ALLOW_HEADERS: str
    ACCESS_CONTROL_ALLOW_METHODS: str
    ACCESS_CONTROL_ALLOW_ORIGIN: str
    ACCESS_CONTROL_EXPOSE_HEADERS: str
    AUTHORIZATION: str
    CACHE_CONTROL: str
    CONNECTION: str
    CONTENT_TYPE: str
    COOKIE: str
    DNT: str
    ETAG: str
    FEATURE_POLICY: str
    FORWARDED_FOR: str
    FORWARDED_HOST: str
    FORWARDED_PROTO: str
    FORWARDED_SERVER: str
    FRAME_OPTIONS: str
    HTTP_METHOD_OVERRIDE: str
    IF_MODIFIED_SINCE: str
    IF_NONE_MATCH: str
    LAST_MODIFIED: str
    LOCATION: str
    ORIGIN: str
    PREFER: str
    POWERED_BY: str
    PROXY_AUTHORIZATION: str
    REAL_IP: str
    RATELIMIT_LIMIT: str
    RATELIMIT_REMAINING: str
    RATELIMIT_RESET: str
    REFERER: str
    REQUEST_ID: str
    REQUESTED_WITH: str
    SEC_CH_UA: str
    SEC_CH_UA_MOBILE: str
    SEC_CH_UA_PLATFORM: str
    SEC_FETCH_DEST: str
    SEC_FETCH_MODE: str
    SEC_FETCH_SITE: str
    USER_AGENT: str
    WEBKIT_CSP: str
    X_AUTH_TOKEN: str
    X_CONTENT_DURATION: str
    X_CONTENT_SECURITY_POLICY: str
    X_CONTENT_TYPE_OPTIONS: str
    X_CORRELATION_ID: str
    X_CUSTOM_HEADER: str
    X_DOWNLOAD_OPTIONS: str
    X_FEATURE_POLICY: str
    X_FORWARDED_FOR: str
    X_PINGBACK: str
    X_PERMITTED_CROSS_DOMAIN_POLICIES: str
    X_REQUEST_ID: str
    X_RATELIMIT_LIMIT: str
    X_RATELIMIT_REMAINING: str
    X_RATELIMIT_RESET: str
    X_XSS_PROTECTION: str

class CookieKeys(Enum):
    SESSION_ID: str
    USER_PREFERENCES: str
    AUTH_TOKEN: str
    CSRF_TOKEN: str
    TRACKING_ID: str
    REFERRER: str
    LAST_VISIT: datetime
    LANGUAGE: str
    LOGIN_TIMESTAMP: datetime
    SESSION_EXPIRES: datetime
    REMEMBER_ME: bool
    PREF_LANGUAGE: str
    LOCALE: str
    COUNTRY: str
    TIMEZONE: str
    REFERRING_URL: str
    DEVICE_ID: str
    BROWSER_ID: str
    CLIENT_ID: str
    ANONYMOUS_ID: str
    TRACKING_TOKEN: str
    OPT_IN: bool
    SECURITY_TOKEN: str
    AUTH_METHOD: str
    SESSION_ID_HASH: str
    USER_ID: str
    REFRESH_TOKEN: str
    API_KEY: str
    CSRF_REFRESH_TOKEN: str
    ENCRYPTION_KEY: str
    ENCRYPTION_IV: str
    DATA_KEY: str
    DATA_IV: str
    COOKIE_CONSENT: bool
    SESSION_TYPE: str
    APP_VERSION: str
    DEVICE_TYPE: str
    FEATURE_FLAGS: str
    EXPERIMENT_ID: str
    USER_ROLE: str
    LOGIN_METHOD: str

class CookieAttributeKeys(Enum):
    DOMAIN: str
    PATH: str
    EXPIRES: datetime
    SECURE: bool
    HTTP_ONLY: bool
    SAME_SITE: str
    MAX_AGE: int
    PRIORITY: str
    SAME_PARTY: bool
    PARTITIONED: bool
    EXTENSION: str