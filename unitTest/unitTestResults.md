# unitTest

> **Note:** This report was generated automatically by the unit test suite.Log output with timestamps resemble the logging of the real request as it would go down in the .log file.
---
## Table of Contents

- [Failing](#failing)
- [Passing](#passing)
  - [test_CookiesLogics](#test_cookieslogics)
  - [test_HTTPMethods_integration](#test_httpmethods_integration)
  - [test_HeaderLogics](#test_headerlogics)
  - [test_HeadersBasicAuth](#test_headersbasicauth)
  - [test_fetchCertOnInit](#test_fetchcertoninit)
  - [test_mockStatusCodes](#test_mockstatuscodes)

## Failing

## Passing
### test_CookiesLogics

<a name="test_cookieslogics"></a>

#### Result

- Log Output:

```
[PASS] cookieUpdate added the cookie.
[PASS] cookieGet retrieved the correct cookie info.
[PASS] cookieRemove removed the cookie.
[PASS] cookieUpdateMultiple added multiple cookies.

```

---
### test_HTTPMethods_integration

<a name="test_httpmethods_integration"></a>

#### Result

- Log Output:

```
------------------------------------------------------------
>>> Testing HTTP Methods with Config <<<
 > certificateNeedFetch: True
 > unsafe: False
 > useTLS: True

[2024-07-27 02:17:12][SAFE][TLS] GET request to https://httpbin.org/get with Status Code 200 - OK
[PASS][SAFE][USE TLS] GET request to https://httpbin.org/get with status code 200.
[2024-07-27 02:17:12][SAFE][TLS] POST request to https://httpbin.org/post with Status Code 200 - OK
[PASS][SAFE][USE TLS] POST request to https://httpbin.org/post with status code 200.
[2024-07-27 02:17:13][SAFE][TLS] PUT request to https://httpbin.org/put with Status Code 200 - OK
[PASS][SAFE][USE TLS] PUT request to https://httpbin.org/put with status code 200.
[2024-07-27 02:17:13][SAFE][TLS] DELETE request to https://httpbin.org/delete with Status Code 200 - OK
[PASS][SAFE][USE TLS] DELETE request to https://httpbin.org/delete with status code 200.
[2024-07-27 02:17:13][SAFE][TLS] PATCH request to https://httpbin.org/patch with Status Code 200 - OK
[PASS][SAFE][USE TLS] PATCH request to https://httpbin.org/patch with status code 200.

- Used Cookies: No cookies used..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="122", "Chromium";v="122", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing HTTP Methods with Config <<<
 > certificateNeedFetch: False
 > unsafe: True
 > useTLS: False

[2024-07-27 02:17:13][UNSAFE][NO TLS] GET request to https://httpbin.org/get with Status Code 200 - OK
[PASS][UNSAFE][NO TLS] GET request to https://httpbin.org/get with status code 200.
[2024-07-27 02:17:13][UNSAFE][NO TLS] POST request to https://httpbin.org/post with Status Code 200 - OK
[PASS][UNSAFE][NO TLS] POST request to https://httpbin.org/post with status code 200.
[2024-07-27 02:17:14][UNSAFE][NO TLS] PUT request to https://httpbin.org/put with Status Code 200 - OK
[PASS][UNSAFE][NO TLS] PUT request to https://httpbin.org/put with status code 200.
[2024-07-27 02:17:14][UNSAFE][NO TLS] DELETE request to https://httpbin.org/delete with Status Code 200 - OK
[PASS][UNSAFE][NO TLS] DELETE request to https://httpbin.org/delete with status code 200.
[2024-07-27 02:17:14][UNSAFE][NO TLS] PATCH request to https://httpbin.org/patch with Status Code 200 - OK
[PASS][UNSAFE][NO TLS] PATCH request to https://httpbin.org/patch with status code 200.

- Used Cookies: No cookies used..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="117", "Chromium";v="117", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36


```

---
### test_HeaderLogics

<a name="test_headerlogics"></a>

#### Result

- Log Output:

```
[PASS] Initialization without headers matches default headers.
[PASS] Initialization with custom headers.
[PASS] headerSetKey added the key.
[PASS] headerGenerate with customHeaders.
[PASS] headerRemoveKey removed the key.
[PASS] headerRemoveMultiple removed the keys.

```

---
### test_HeadersBasicAuth

<a name="test_headersbasicauth"></a>

#### Result

- Log Output:

```
------------------------------------------------------------
>>> Testing Basic Auth with Config <<<
 > certificateNeedFetch: True
 > unsafe: False
 > useTLS: True

[2024-07-27 02:17:16][SAFE][TLS] GET request to https://postman-echo.com/basic-auth with Status Code 200 - OK
[PASS][SAFE][USE TLS] Request to https://postman-echo.com/basic-auth with status code 200.
------------------------------------------------------------
>>> Testing Basic Auth with Config <<<
 > certificateNeedFetch: False
 > unsafe: True
 > useTLS: False

[2024-07-27 02:17:16][UNSAFE][NO TLS] GET request to https://postman-echo.com/basic-auth with Status Code 200 - OK
[PASS][UNSAFE][NO TLS] Request to https://postman-echo.com/basic-auth with status code 200.

- Used Cookies: None.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="118", "Chromium";v="118", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Windows"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
 > Authorization: Basic cG9zdG1hbjpwYXNzd29yZA==


```

---
### test_fetchCertOnInit

<a name="test_fetchcertoninit"></a>

#### Result

- Log Output:

```
[2024-07-27 02:17:16][SAFE][TLS] GET request to https://curl.se/ca/cacert.pem with Status Code 200 - OK
Successfully fetched certificate and saved.
[PASS][SAFE] Fetched certificate on initialization with certificateNeedFetch: True
[PASS][SAFE] Verified path exists.
[PASS][SAFE] Verified we are using it.
[PASS][SAFE] Verified its not empty.
[PASS][UNSAFE] Fetched certificate on initialization with certificateNeedFetch: True
[PASS][UNSAFE] Verified path exists.
[PASS][UNSAFE] Verified we are not using it.


```

---
### test_mockStatusCodes

<a name="test_mockstatuscodes"></a>

#### Result

- Log Output:

```
[PASS] ContinueException raised for status code 100.
[PASS] SwitchingProtocolsException raised for status code 101.
[PASS] ProcessingException raised for status code 102.
[PASS] EarlyHintsException raised for status code 103.
[PASS] BadRequestException raised for status code 400.
[PASS] UnauthorizedException raised for status code 401.
[PASS] PaymentRequiredException raised for status code 402.
[PASS] ForbiddenException raised for status code 403.
[PASS] NotFoundException raised for status code 404.
[PASS] MethodNotAllowedException raised for status code 405.
[PASS] NotAcceptableException raised for status code 406.
[PASS] ProxyAuthenticationRequiredException raised for status code 407.
[PASS] RequestTimeoutException raised for status code 408.
[PASS] ConflictException raised for status code 409.
[PASS] GoneException raised for status code 410.
[PASS] LengthRequiredException raised for status code 411.
[PASS] PreconditionFailedException raised for status code 412.
[PASS] PayloadTooLargeException raised for status code 413.
[PASS] URITooLongException raised for status code 414.
[PASS] UnsupportedMediaTypeException raised for status code 415.
[PASS] RangeNotSatisfiableException raised for status code 416.
[PASS] ExpectationFailedException raised for status code 417.
[PASS] MisdirectedRequestException raised for status code 421.
[PASS] UnprocessableEntityException raised for status code 422.
[PASS] LockedException raised for status code 423.
[PASS] FailedDependencyException raised for status code 424.
[PASS] TooEarlyException raised for status code 425.
[PASS] UpgradeRequiredException raised for status code 426.
[PASS] PreconditionRequiredException raised for status code 428.
[PASS] TooManyRequestsException raised for status code 429.
[PASS] RequestHeaderFieldsTooLargeException raised for status code 431.
[PASS] UnavailableForLegalReasonsException raised for status code 451.
[PASS] InternalServerErrorException raised for status code 500.
[PASS] NotImplementedException raised for status code 501.
[PASS] BadGatewayException raised for status code 502.
[PASS] ServiceUnavailableException raised for status code 503.
[PASS] GatewayTimeoutException raised for status code 504.
[PASS] HTTPVersionNotSupportedException raised for status code 505.
[PASS] VariantAlsoNegotiatesException raised for status code 506.
[PASS] InsufficientStorageException raised for status code 507.
[PASS] LoopDetectedException raised for status code 508.
[PASS] NotExtendedException raised for status code 510.
[PASS] NetworkAuthenticationRequiredException raised for status code 511.
[PASS] UnknownErrorException raised for status code 520.
[PASS] WebServerDownException raised for status code 521.
[PASS] ConnectionTimedOutException raised for status code 522.
[PASS] OriginUnreachableException raised for status code 523.
[PASS] TimeoutOccurredException raised for status code 524.
[PASS] NetworkReadTimeoutException raised for status code 598.
[PASS] NetworkConnectTimeoutException raised for status code 599.

```

---
