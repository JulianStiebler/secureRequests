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

class Serializer():
    """Serves as a base class for all enumeration-operations in this module."""
    def __str__(self):
        """Returns the string representation of the enum value."""
        return self.value

class HeaderKeys(Serializer, Enum):
    """
    This enum holds available enumeration keys for standard HTTP headers.
        ACCEPT, ACCEPT_ENCODING, ACCEPT_LANGUAGE, ACCESS_CONTROL_ALLOW_HEADERS,
        ACCESS_CONTROL_ALLOW_METHODS, ACCESS_CONTROL_ALLOW_ORIGIN, ACCESS_CONTROL_EXPOSE_HEADERS,
        AUTHORIZATION, CACHE_CONTROL, CONNECTION, CONTENT_TYPE, COOKIE, DNT, ETAG, FEATURE_POLICY,
        FORWARDED_FOR, FORWARDED_HOST, FORWARDED_PROTO, FORWARDED_SERVER, FRAME_OPTIONS,
        HTTP_METHOD_OVERRIDE, IF_MODIFIED_SINCE, IF_NONE_MATCH, LAST_MODIFIED, LOCATION, ORIGIN,
        PREFER, POWERED_BY, PROXY_AUTHORIZATION, REAL_IP, RATELIMIT_LIMIT, RATELIMIT_REMAINING,
        RATELIMIT_RESET, REFERER, REQUEST_ID, REQUESTED_WITH, SEC_CH_UA, SEC_CH_UA_MOBILE,
        SEC_CH_UA_PLATFORM, SEC_FETCH_DEST, SEC_FETCH_MODE, SEC_FETCH_SITE, USER_AGENT, WEBKIT_CSP,
        X_AUTH_TOKEN, X_CONTENT_DURATION, X_CONTENT_SECURITY_POLICY, X_CONTENT_TYPE_OPTIONS,
        X_CORRELATION_ID, X_CUSTOM_HEADER, X_DOWNLOAD_OPTIONS, X_FEATURE_POLICY, X_FORWARDED_FOR,
        X_PINGBACK, X_PERMITTED_CROSS_DOMAIN_POLICIES, X_REQUEST_ID, X_RATELIMIT_LIMIT,
        X_RATELIMIT_REMAINING, X_RATELIMIT_RESET, X_XSS_PROTECTION
    """
    ACCEPT = "Accept"  # Specifies media types accepted by the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept

    ACCEPT_ENCODING = "Accept-Encoding"  # Specifies encoding types accepted by the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding

    ACCEPT_LANGUAGE = "Accept-Language"  # Specifies preferred languages for response.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language

    ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"  # Specifies which headers can be used.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers

    ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"  # Specifies allowed HTTP methods.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods

    ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"  # Specifies allowed origins for requests.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin

    ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"  # Specifies which headers are exposed.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers

    AUTHORIZATION = "Authorization"  # Contains credentials for authentication.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization

    CACHE_CONTROL = "Cache-Control"  # Controls caching mechanisms.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control

    CONNECTION = "Connection"  # Controls whether the connection should be kept alive.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection

    CONTENT_TYPE = "Content-Type"  # Indicates the media type of the resource.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type

    COOKIE = "Cookie"  # Contains stored cookies from the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie

    DNT = "DNT"  # Indicates the user's tracking preference.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT

    ETAG = "ETag"  # A unique identifier for a specific version of a resource.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag

    FEATURE_POLICY = "X-Feature-Policy"  # Controls which features can be used.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy

    FORWARDED_FOR = "X-Forwarded-For"  # Indicates the original IP address of the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For

    FORWARDED_HOST = "X-Forwarded-Host"  # Indicates the original host requested by the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host

    FORWARDED_PROTO = "X-Forwarded-Proto"  # Indicates the protocol used by the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Proto

    FORWARDED_SERVER = "X-Forwarded-Server"  # Specifies the original server address.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Server

    FRAME_OPTIONS = "X-Frame-Options"  # Controls whether the page can be displayed in a frame.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options

    HTTP_METHOD_OVERRIDE = "X-HTTP-Method-Override"  # Allows overriding the HTTP method.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-HTTP-Method-Override

    IF_MODIFIED_SINCE = "If-Modified-Since"  # Allows caching mechanisms to check if the resource has changed.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since

    IF_NONE_MATCH = "If-None-Match"  # Allows caching mechanisms to validate resource ETag.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match

    LAST_MODIFIED = "Last-Modified"  # Indicates the last modification date of the resource.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified

    LOCATION = "Location"  # Used in redirection, indicates the URL to redirect to.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Location

    ORIGIN = "Origin"  # Specifies the origin of the request for Cross-Origin Resource Sharing (CORS).
    # More Info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin

    PREFER = "Prefer"  # Allows clients to specify preferred behavior.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Prefer

    POWERED_BY = "X-Powered-By"  # Provides information about the server technology.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Powered-By

    PROXY_AUTHORIZATION = "Proxy-Authorization"  # Contains credentials for proxy authentication.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Proxy-Authorization

    REAL_IP = "X-Real-IP"  # Contains the IP address of the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Real-IP

    RATELIMIT_LIMIT = "X-RateLimit-Limit"  # Specifies the maximum rate limit.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-RateLimit-Limit

    RATELIMIT_REMAINING = "X-RateLimit-Remaining"  # Specifies the remaining rate limit.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-RateLimit-Remaining

    RATELIMIT_RESET = "X-RateLimit-Reset"  # Indicates when the rate limit will reset.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-RateLimit-Reset

    REFERER = "Referer"  # Indicates the URL of the referring page that led to the current request.
    # More Info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer
    
    REQUEST_ID = "X-Request-ID"  # Unique identifier for the request.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Request-ID

    REQUESTED_WITH = "X-Requested-With"  # Used to identify Ajax requests.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Requested-With

    SEC_CH_UA = "Sec-Ch-Ua"  # Provides information about the user agent.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA

    SEC_CH_UA_MOBILE = "Sec-Ch-Ua-Mobile"  # Indicates if the user agent is mobile.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Mobile

    SEC_CH_UA_PLATFORM = "Sec-Ch-Ua-Platform"  # Provides the platform information.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA-Platform

    SEC_FETCH_DEST = "Sec-Fetch-Dest"  # Indicates the request destination.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest

    SEC_FETCH_MODE = "Sec-Fetch-Mode"  # Specifies the mode of the fetch request.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode

    SEC_FETCH_SITE = "Sec-Fetch-Site"  # Indicates the origin of the request.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site

    USER_AGENT = "User-Agent"  # Contains information about the user agent.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

    WEBKIT_CSP = "X-WebKit-CSP"  # Defines the Content Security Policy for WebKit browsers.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-WebKit-CSP

    X_AUTH_TOKEN = "X-Auth-Token"  # Used for authentication purposes.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Auth-Token

    X_CONTENT_DURATION = "X-Content-Duration"  # Indicates the duration of the content.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Duration

    X_CONTENT_SECURITY_POLICY = "X-Content-Security-Policy"  # Controls resources the user agent is allowed to load.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Security-Policy

    X_CONTENT_TYPE_OPTIONS = "X-Content-Type-Options"  # Controls MIME type sniffing.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options

    X_CORRELATION_ID = "X-Correlation-ID"  # Used for tracking requests across systems.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Correlation-ID

    X_CUSTOM_HEADER = "X-Custom-Header"  # Custom header for various uses.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Custom-Header

    X_DOWNLOAD_OPTIONS = "X-Download-Options"  # Controls file download options.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Download-Options

    X_FEATURE_POLICY = "X-Feature-Policy"  # Controls which features can be used.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Feature-Policy

    X_FORWARDED_FOR = "X-Forwarded-For"  # Identifies the originating IP address of a client connecting through a proxy or load balancer.
    # More Info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
    
    X_PINGBACK = "X-Pingback"  # Used in XML-RPC requests.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Pingback

    X_PERMITTED_CROSS_DOMAIN_POLICIES = "X-Permitted-Cross-Domain-Policies"  # Controls Flash cross-domain policy.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Permitted-Cross-Domain-Policies

    X_REQUEST_ID = "X-Request-ID"  # Unique ID for the request.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Request-ID

    X_RATELIMIT_LIMIT = "X-RateLimit-Limit"  # Maximum number of allowed requests.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-RateLimit-Limit

    X_RATELIMIT_REMAINING = "X-RateLimit-Remaining"  # Remaining number of requests.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-RateLimit-Remaining

    X_RATELIMIT_RESET = "X-RateLimit-Reset"  # Time when rate limit resets.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-RateLimit-Reset

    X_XSS_PROTECTION = "X-XSS-Protection"  # Controls browser XSS protection.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection

class CookieKeys(Serializer, Enum):
    """
    This enum holds available enumeration keys for standard cookie keys.
        SESSION_ID, USER_PREFERENCES, AUTH_TOKEN, CSRF_TOKEN, TRACKING_ID,
        REFERRER, LAST_VISIT, LANGUAGE, LOGIN_TIMESTAMP, SESSION_EXPIRES,
        REMEMBER_ME, PREF_LANGUAGE, LOCALE, COUNTRY, TIMEZONE,
        REFERRING_URL, DEVICE_ID, BROWSER_ID, CLIENT_ID, ANONYMOUS_ID,
        TRACKING_TOKEN, OPT_IN, SECURITY_TOKEN, AUTH_METHOD, SESSION_ID_HASH,
        USER_ID, REFRESH_TOKEN, API_KEY, CSRF_REFRESH_TOKEN, ENCRYPTION_KEY,
        ENCRYPTION_IV, DATA_KEY, DATA_IV, COOKIE_CONSENT, SESSION_TYPE,
        APP_VERSION, DEVICE_TYPE, FEATURE_FLAGS, EXPERIMENT_ID, USER_ROLE,
        LOGIN_METHOD
    """
    SESSION_ID = "session_id"  # Identifies the user session.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    USER_PREFERENCES = "user_preferences"  # Stores user preferences/settings.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    AUTH_TOKEN = "auth_token"  # Contains the authentication token.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    CSRF_TOKEN = "csrf_token"  # Protects against CSRF attacks.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    TRACKING_ID = "tracking_id"  # Tracks user activities.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    REFERRER = "referrer"  # Tracks the origin of traffic.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    LAST_VISIT = "last_visit"  # Timestamp of the last visit.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    LANGUAGE = "language"  # User language preference.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    LOGIN_TIMESTAMP = "login_timestamp"  # Timestamp of user login.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    SESSION_EXPIRES = "session_expires"  # Expiration time of the session.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    REMEMBER_ME = "remember_me"  # Indicates if the user is remembered.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    PREF_LANGUAGE = "pref_language"  # Preferred language setting.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    LOCALE = "locale"  # Locale information.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    COUNTRY = "country"  # Country code of the user.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    TIMEZONE = "timezone"  # Timezone of the user.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    REFERRING_URL = "referring_url"  # URL that referred the user.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    DEVICE_ID = "device_id"  # Unique identifier for the user's device.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    BROWSER_ID = "browser_id"  # Unique identifier for the user's browser.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    CLIENT_ID = "client_id"  # Unique identifier for the client.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    ANONYMOUS_ID = "anonymous_id"  # Identifier for anonymous users.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    TRACKING_TOKEN = "tracking_token"  # Token used for tracking.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    OPT_IN = "opt_in"  # Indicates user consent or preferences.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    SECURITY_TOKEN = "security_token"  # Security token for extra protection.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    AUTH_METHOD = "auth_method"  # Authentication method used.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    SESSION_ID_HASH = "session_id_hash"  # Hash of the session ID for security.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    USER_ID = "user_id"  # Unique identifier for the user.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    REFRESH_TOKEN = "refresh_token"  # Token used to refresh authentication.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    API_KEY = "api_key"  # API key for accessing services.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    CSRF_REFRESH_TOKEN = "csrf_refresh_token"  # Token for CSRF protection refresh.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    ENCRYPTION_KEY = "encryption_key"  # Key used for encrypting sensitive data.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    ENCRYPTION_IV = "encryption_iv"  # Initialization vector for encryption.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    DATA_KEY = "data_key"  # Key for encrypting user data.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    DATA_IV = "data_iv"  # IV for encrypting user data.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    COOKIE_CONSENT = "cookie_consent"  # Indicates consent for cookies.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    SESSION_TYPE = "session_type"  # Type of session (e.g., guest, authenticated).
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    APP_VERSION = "app_version"  # Version of the application.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    DEVICE_TYPE = "device_type"  # Type of device (e.g., mobile, desktop).
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    FEATURE_FLAGS = "feature_flags"  # Flags for enabling/disabling features.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    EXPERIMENT_ID = "experiment_id"  # ID for A/B testing or experiments.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    USER_ROLE = "user_role"  # Role of the user in the application.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

    LOGIN_METHOD = "login_method"  # Method used for logging in.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie

class CookieAttributeKeys(Serializer, Enum):
    """
    This enum holds available enumeration keys for cookie attributes used in HTTP headers.
        DOMAIN, PATH, EXPIRES, SECURE, HTTP_ONLY, SAME_SITE, MAX_AGE, PRIORITY, SAME_PARTY, PARTITIONED, EXTENSION
    """
    DOMAIN = 'domain'  # The domain for which the cookie is valid.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#domain

    PATH = 'path'  # The path within the domain for which the cookie is valid.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#path

    EXPIRES = 'expires'  # The expiration date and time of the cookie.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#expires

    SECURE = 'secure'  # Indicates if the cookie should only be transmitted over secure protocols.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#secure

    HTTP_ONLY = 'httponly'  # Indicates if the cookie is accessible only through HTTP(S) requests and not by client-side scripts.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#httponly

    SAME_SITE = 'samesite'  # The SameSite attribute to prevent CSRF (Cross-Site Request Forgery) attacks.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#samesite

    MAX_AGE = 'max_age'  # The maximum age of the cookie in seconds.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#max-age

    PRIORITY = 'priority'  # The priority of the cookie.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#priority

    SAME_PARTY = 'sameparty'  # Indicates that the cookie is set by the same party.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#sameparty

    PARTITIONED = 'partitioned'  # Indicates that the cookie is partitioned.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#partitioned

    EXTENSION = 'extension'  # Any other extension attributes for the cookie.
    # More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#extension
