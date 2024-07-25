"""
This file holds custom exceptions for various HTTP status codes.

Classes:
- SecureRequestsException - Base class for custom exceptions.
- ContinueException - Raised when a 100 Continue response is received.
- SwitchingProtocolsException - Raised when a 101 Switching Protocols response is received.
- ProcessingException - Raised when a 102 Processing response is received.
- EarlyHintsException - Raised when a 103 Early Hints response is received.
- BadRequestException - Raised when a 400 Bad Request response is received.
- UnauthorizedException - Raised when a 401 Unauthorized response is received.
- PaymentRequiredException - Raised when a 402 Payment Required response is received.
- ForbiddenException - Raised when a 403 Forbidden response is received.
- NotFoundException - Raised when a 404 Not Found response is received.
- MethodNotAllowedException - Raised when a 405 Method Not Allowed response is received.
- NotAcceptableException - Raised when a 406 Not Acceptable response is received.
- ProxyAuthenticationRequiredException - Raised when a 407 Proxy Authentication Required response is received.
- RequestTimeoutException - Raised when a 408 Request Timeout response is received.
- ConflictException - Raised when a 409 Conflict response is received.
- GoneException - Raised when a 410 Gone response is received.
- LengthRequiredException - Raised when a 411 Length Required response is received.
- PreconditionFailedException - Raised when a 412 Precondition Failed response is received.
- PayloadTooLargeException - Raised when a 413 Payload Too Large response is received.
- URITooLongException - Raised when a 414 URI Too Long response is received.
- UnsupportedMediaTypeException - Raised when a 415 Unsupported Media Type response is received.
- RangeNotSatisfiableException - Raised when a 416 Range Not Satisfiable response is received.
- ExpectationFailedException - Raised when a 417 Expectation Failed response is received.
- MisdirectedRequestException - Raised when a 421 Misdirected Request response is received.
- UnprocessableEntityException - Raised when a 422 Unprocessable Entity response is received.
- LockedException - Raised when a 423 Locked response is received.
- FailedDependencyException - Raised when a 424 Failed Dependency response is received.
- TooEarlyException - Raised when a 425 Too Early response is received.
- UpgradeRequiredException - Raised when a 426 Upgrade Required response is received.
- PreconditionRequiredException - Raised when a 428 Precondition Required response is received.
- TooManyRequestsException - Raised when a 429 Too Many Requests response is received.
- RequestHeaderFieldsTooLargeException - Raised when a 431 Request Header Fields Too Large response is received.
- UnavailableForLegalReasonsException - Raised when a 451 Unavailable For Legal Reasons response is received.
- InternalServerErrorException - Raised when a 500 Internal Server Error response is received.
- NotImplementedException - Raised when a 501 Not Implemented response is received.
- BadGatewayException - Raised when a 502 Bad Gateway response is received.
- ServiceUnavailableException - Raised when a 503 Service Unavailable response is received.
- GatewayTimeoutException - Raised when a 504 Gateway Timeout response is received.
- HTTPVersionNotSupportedException - Raised when a 505 HTTP Version Not Supported response is received.
- VariantAlsoNegotiatesException - Raised when a 506 Variant Also Negotiates response is received.
- InsufficientStorageException - Raised when a 507 Insufficient Storage response is received.
- LoopDetectedException - Raised when a 508 Loop Detected response is received.
- NotExtendedException - Raised when a 510 Not Extended response is received.
- NetworkAuthenticationRequiredException - Raised when a 511 Network Authentication Required response is received.
- UnknownErrorException - Raised when a 520 Unknown Error response is received.
- WebServerDownException - Raised when a 521 Web Server Is Down response is received.
- ConnectionTimedOutException - Raised when a 522 Connection Timed Out response is received.
- OriginUnreachableException - Raised when a 523 Origin Is Unreachable response is received.
- TimeoutOccurredException - Raised when a 524 A Timeout Occurred response is received.
- NetworkReadTimeoutException - Raised when a 598 Network Read Timeout response is received.
- NetworkConnectTimeoutException - Raised when a 599 Network Connect Timeout response is received.

# Author: Julian Stiebler
# GitHub Repository: https://github.com/JulianStiebler/secureRequests
# GitHub Issues: https://github.com/JulianStiebler/secureRequests/issues
# GitHub Wiki: https://github.com/JulianStiebler/secureRequests/wiki

# Created: 15.07.2024
# Last edited: 17.07.2024
"""

class SecureRequestsException(Exception):
    """Base class for other exceptions"""
    pass

class ContinueException(SecureRequestsException):
    """Exception for HTTP status 100: Continue"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/100
    pass

class SwitchingProtocolsException(SecureRequestsException):
    """Exception for HTTP status 101: Switching Protocols"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/101
    pass

class ProcessingException(SecureRequestsException):
    """Exception for HTTP status 102: Processing"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/102
    pass

class EarlyHintsException(SecureRequestsException):
    """Exception for HTTP status 103: Early Hints"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/103
    pass

class BadRequestException(SecureRequestsException):
    """Exception for HTTP status 400: Bad Request"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
    pass

class UnauthorizedException(SecureRequestsException):
    """Exception for HTTP status 401: Unauthorized"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
    pass

class PaymentRequiredException(SecureRequestsException):
    """Exception for HTTP status 402: Payment Required"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/402
    pass

class ForbiddenException(SecureRequestsException):
    """Exception for HTTP status 403: Forbidden"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
    pass

class NotFoundException(SecureRequestsException):
    """Exception for HTTP status 404: Not Found"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
    pass

class MethodNotAllowedException(SecureRequestsException):
    """Exception for HTTP status 405: Method Not Allowed"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405
    pass

class NotAcceptableException(SecureRequestsException):
    """Exception for HTTP status 406: Not Acceptable"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406
    pass

class ProxyAuthenticationRequiredException(SecureRequestsException):
    """Exception for HTTP status 407: Proxy Authentication Required"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/407
    pass

class RequestTimeoutException(SecureRequestsException):
    """Exception for HTTP status 408: Request Timeout"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408
    pass

class ConflictException(SecureRequestsException):
    """Exception for HTTP status 409: Conflict"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409
    pass

class GoneException(SecureRequestsException):
    """Exception for HTTP status 410: Gone"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410
    pass

class LengthRequiredException(SecureRequestsException):
    """Exception for HTTP status 411: Length Required"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/411
    pass

class PreconditionFailedException(SecureRequestsException):
    """Exception for HTTP status 412: Precondition Failed"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/412
    pass

class PayloadTooLargeException(SecureRequestsException):
    """Exception for HTTP status 413: Payload Too Large"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/413
    pass

class URITooLongException(SecureRequestsException):
    """Exception for HTTP status 414: URI Too Long"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414
    pass

class UnsupportedMediaTypeException(SecureRequestsException):
    """Exception for HTTP status 415: Unsupported Media Type"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415
    pass

class RangeNotSatisfiableException(SecureRequestsException):
    """Exception for HTTP status 416: Range Not Satisfiable"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416
    pass

class ExpectationFailedException(SecureRequestsException):
    """Exception for HTTP status 417: Expectation Failed"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/417
    pass

class MisdirectedRequestException(SecureRequestsException):
    """Exception for HTTP status 421: Misdirected Request"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421
    pass

class UnprocessableEntityException(SecureRequestsException):
    """Exception for HTTP status 422: Unprocessable Entity"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422
    pass

class LockedException(SecureRequestsException):
    """Exception for HTTP status 423: Locked"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/423
    pass

class FailedDependencyException(SecureRequestsException):
    """Exception for HTTP status 424: Failed Dependency"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/424
    pass

class TooEarlyException(SecureRequestsException):
    """Exception for HTTP status 425: Too Early"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/425
    pass

class UpgradeRequiredException(SecureRequestsException):
    """Exception for HTTP status 426: Upgrade Required"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/426
    pass

class PreconditionRequiredException(SecureRequestsException):
    """Exception for HTTP status 428: Precondition Required"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/428
    pass

class TooManyRequestsException(SecureRequestsException):
    """Exception for HTTP status 429: Too Many Requests"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
    pass

class RequestHeaderFieldsTooLargeException(SecureRequestsException):
    """Exception for HTTP status 431: Request Header Fields Too Large"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/431
    pass

class UnavailableForLegalReasonsException(SecureRequestsException):
    """Exception for HTTP status 451: Unavailable For Legal Reasons"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/451
    pass

class InternalServerErrorException(SecureRequestsException):
    """Exception for HTTP status 500: Internal Server Error"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
    pass

class NotImplementedException(SecureRequestsException):
    """Exception for HTTP status 501: Not Implemented"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501
    pass

class BadGatewayException(SecureRequestsException):
    """Exception for HTTP status 502: Bad Gateway"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502
    pass

class ServiceUnavailableException(SecureRequestsException):
    """Exception for HTTP status 503: Service Unavailable"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503
    pass

class GatewayTimeoutException(SecureRequestsException):
    """Exception for HTTP status 504: Gateway Timeout"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504
    pass

class HTTPVersionNotSupportedException(SecureRequestsException):
    """Exception for HTTP status 505: HTTP Version Not Supported"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/505
    pass

class VariantAlsoNegotiatesException(SecureRequestsException):
    """Exception for HTTP status 506: Variant Also Negotiates"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/506
    pass

class InsufficientStorageException(SecureRequestsException):
    """Exception for HTTP status 507: Insufficient Storage"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/507
    pass

class LoopDetectedException(SecureRequestsException):
    """Exception for HTTP status 508: Loop Detected"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/508
    pass

class NotExtendedException(SecureRequestsException):
    """Exception for HTTP status 510: Not Extended"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/510
    pass

class NetworkAuthenticationRequiredException(SecureRequestsException):
    """Exception for HTTP status 511: Network Authentication Required"""
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/511
    pass

class UnknownErrorException(SecureRequestsException):
    """
    Exception for HTTP status code 520 Unknown Error.
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/520
    """
    pass

class WebServerDownException(SecureRequestsException):
    """
    Exception for HTTP status code 521 Web Server Is Down.
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/521
    """
    pass

class ConnectionTimedOutException(SecureRequestsException):
    """
    Exception for HTTP status code 522 Connection Timed Out.
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/522
    """
    pass

class OriginUnreachableException(SecureRequestsException):
    """
    Exception for HTTP status code 523 Origin Is Unreachable.
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/523
    """
    pass

class TimeoutOccurredException(SecureRequestsException):
    """
    Exception for HTTP status code 524 A Timeout Occurred.
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/524
    """
    pass

class NetworkReadTimeoutException(SecureRequestsException):
    """Exception for HTTP status 598: Network Read Timeout"""
    # Note: This is not an official HTTP status code.
    pass

class NetworkConnectTimeoutException(SecureRequestsException):
    """Exception for HTTP status 599: Network Connect Timeout"""
    # Note: This is not an official HTTP status code.
    pass