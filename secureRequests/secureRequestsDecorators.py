"""
This library provides a decorator to handle HTTP responses and raise custom exceptions for various HTTP status codes.
It is designed to simplify error handling in HTTP requests by mapping status codes to custom exceptions.

Usage
-----
1. Decorate your HTTP request functions with @handleResponse to automatically raise exceptions for error status codes.
2. Use the exceptions defined in secureRequestsExceptions for custom handling of different HTTP errors.

Example
-------
>>> @handleResponse
... def get_data(url: str) -> requests.Response:
...     return requests.get(url)
>>> response = get_data("https://example.com/api/data")
>>> response.json()
{
    "key": "value"
}

MIT License
-----------
Copyright (c) 2024 Julian Stiebler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# Created: 15.07.2024
# Last edited: 17.07.2024
"""

from functools import wraps
from . import secureRequestsExceptions as srExceptions

STATUS_CODE_EXCEPTION_MAP = {
    100: srExceptions.ContinueException,
    101: srExceptions.SwitchingProtocolsException,
    102: srExceptions.ProcessingException,
    103: srExceptions.EarlyHintsException,
    400: srExceptions.BadRequestException,
    401: srExceptions.UnauthorizedException,
    402: srExceptions.PaymentRequiredException,
    403: srExceptions.ForbiddenException,
    404: srExceptions.NotFoundException,
    405: srExceptions.MethodNotAllowedException,
    406: srExceptions.NotAcceptableException,
    407: srExceptions.ProxyAuthenticationRequiredException,
    408: srExceptions.RequestTimeoutException,
    409: srExceptions.ConflictException,
    410: srExceptions.GoneException,
    411: srExceptions.LengthRequiredException,
    412: srExceptions.PreconditionFailedException,
    413: srExceptions.PayloadTooLargeException,
    414: srExceptions.URITooLongException,
    415: srExceptions.UnsupportedMediaTypeException,
    416: srExceptions.RangeNotSatisfiableException,
    417: srExceptions.ExpectationFailedException,
    421: srExceptions.MisdirectedRequestException,
    422: srExceptions.UnprocessableEntityException,
    423: srExceptions.LockedException,
    424: srExceptions.FailedDependencyException,
    425: srExceptions.TooEarlyException,
    426: srExceptions.UpgradeRequiredException,
    428: srExceptions.PreconditionRequiredException,
    429: srExceptions.TooManyRequestsException,
    431: srExceptions.RequestHeaderFieldsTooLargeException,
    451: srExceptions.UnavailableForLegalReasonsException,
    500: srExceptions.InternalServerErrorException,
    501: srExceptions.NotImplementedException,
    502: srExceptions.BadGatewayException,
    503: srExceptions.ServiceUnavailableException,
    504: srExceptions.GatewayTimeoutException,
    505: srExceptions.HTTPVersionNotSupportedException,
    506: srExceptions.VariantAlsoNegotiatesException,
    507: srExceptions.InsufficientStorageException,
    508: srExceptions.LoopDetectedException,
    510: srExceptions.NotExtendedException,
    511: srExceptions.NetworkAuthenticationRequiredException,
    520: srExceptions.UnknownErrorException,
    521: srExceptions.WebServerDownException,
    522: srExceptions.ConnectionTimedOutException,
    523: srExceptions.OriginUnreachableException,
    524: srExceptions.TimeoutOccurredException,
    598: srExceptions.NetworkReadTimeoutException,  # Note: unofficial
    599: srExceptions.NetworkConnectTimeoutException,  # Note: unofficial
}

def handleResponse(func):
    """
    Decorator to handle HTTP responses and raise custom exceptions for error status codes.

    Parameters
    ----------
    func : Callable[..., requests.Response]
        The function making an HTTP request that returns a `requests.Response` object.

    Returns
    -------
    Callable[..., requests.Response]
        A wrapped function that raises custom exceptions based on the status code of the response.

    Raises
    ------
    BadRequestException
        If the response status code is 400.
    UnauthorizedException
        If the response status code is 401.
    ForbiddenException
        If the response status code is 403.
    NotFoundException
        If the response status code is 404.
    MethodNotAllowedException
        If the response status code is 405.
    NotAcceptableException
        If the response status code is 406.
    ProxyAuthenticationRequiredException
        If the response status code is 407.
    RequestTimeoutException
        If the response status code is 408.
    PayloadTooLargeException
        If the response status code is 413.
    TooManyRequestsException
        If the response status code is 429.
    InternalServerErrorException
        If the response status code is 500.
    BadGatewayException
        If the response status code is 502.
    ServiceUnavailableException
        If the response status code is 503.
    GatewayTimeoutException
        If the response status code is 504.
    UnknownErrorException
        If the response status code is 520.
    WebServerDownException
        If the response status code is 521.
    ConnectionTimedOutException
        If the response status code is 522.
    OriginUnreachableException
        If the response status code is 523.
    TimeoutOccurredException
        If the response status code is 524.

    Example
    -------
    >>> @handleResponse
    ... def get_data(url: str) -> requests.Response:
    ...     return requests.get(url)
    >>> response = get_data("https://example.com/api/data")
    >>> response.json()
    {
        "key": "value"
    }

    Example Output
    --------------
    >>> response = get_data("https://example.com/api/data")
    200 OK: {
        "key": "value"
    }
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        exception = STATUS_CODE_EXCEPTION_MAP.get(response.status_code)
        if exception:
            raise exception(f"{response.status_code} Error: {response.reason} - {response.text}")
        response.raise_for_status()
        return response
    return wrapper
