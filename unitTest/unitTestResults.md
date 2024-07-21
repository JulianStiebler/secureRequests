# unitTest

## Table of Contents

- [Failing](#failing)
- [Passing](#passing)
  - [test_HTTPMethods_Cookies_SAFE](#test_httpmethods_cookies_safe)
  - [test_HTTPMethods_Cookies_UNSAFE](#test_httpmethods_cookies_unsafe)
  - [test_HTTPMethods_SAFE](#test_httpmethods_safe)
  - [test_HTTPMethods_UNSAFE](#test_httpmethods_unsafe)
  - [test_fetchCertOnInit_SAFE](#test_fetchcertoninit_safe)
  - [test_fetchCertOnInit_UNSAFE](#test_fetchcertoninit_unsafe)
  - [test_mockStatusCodes](#test_mockstatuscodes)

## Failing

## Passing
### test_HTTPMethods_Cookies_SAFE

<a name="test_httpmethods_cookies_safe"></a>

#### Configurations

- certificateNeedFetch: False

- unsafe: False

- useTLS: True

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 200.


>>> Testing Status Code 400
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.352537, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="118", "Chromium";v="118", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 200.


>>> Testing Status Code 400
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.352537, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="118", "Chromium";v="118", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 200.


>>> Testing Status Code 400
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.352537, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="118", "Chromium";v="118", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 200.


>>> Testing Status Code 400
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.352537, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="118", "Chromium";v="118", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 200.


>>> Testing Status Code 400
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.352537, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="118", "Chromium";v="118", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36


```

---
### test_HTTPMethods_Cookies_UNSAFE

<a name="test_httpmethods_cookies_unsafe"></a>

#### Configurations

- certificateNeedFetch: False

- unsafe: True

- useTLS: False

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.357658, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="117", "Chromium";v="117", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.357658, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="117", "Chromium";v="117", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.357658, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="117", "Chromium";v="117", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.357658, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="117", "Chromium";v="117", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 400.

- Used Cookies:  > CookieKeys.SESSION_ID: {PATH: /, EXPIRES: 2024-07-28 02:04:07.357658, SECURE: True}.
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="117", "Chromium";v="117", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Macintosh"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36


```

---
### test_HTTPMethods_SAFE

<a name="test_httpmethods_safe"></a>

#### Configurations

- certificateNeedFetch: False

- unsafe: False

- useTLS: True

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 200.

>>> Testing Status Code 400 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="124", "Chromium";v="124", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "X11"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 200.

>>> Testing Status Code 400 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="124", "Chromium";v="124", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "X11"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 200.

>>> Testing Status Code 400 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="124", "Chromium";v="124", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "X11"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 200.

>>> Testing Status Code 400 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="124", "Chromium";v="124", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "X11"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 200.

>>> Testing Status Code 400 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="124", "Chromium";v="124", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "X11"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36


```

---
### test_HTTPMethods_UNSAFE

<a name="test_httpmethods_unsafe"></a>

#### Configurations

- certificateNeedFetch: False

- unsafe: True

- useTLS: False

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] GET request to https://httpbin.org/GET with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="115", "Chromium";v="115", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Windows"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] POST request to https://httpbin.org/POST with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="115", "Chromium";v="115", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Windows"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] PUT request to https://httpbin.org/PUT with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="115", "Chromium";v="115", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Windows"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] DELETE request to https://httpbin.org/DELETE with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="115", "Chromium";v="115", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Windows"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36

------------------------------------------------------------
>>> Testing Status Code 200 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 200.
>>> Testing Status Code 400 <<<
[PASS][SAFE] PATCH request to https://httpbin.org/PATCH with status code 400.

- Used Cookies: ..
- Used Header:
 > Accept: application/x-www-form-urlencoded
 > Content-Type: application/x-www-form-urlencoded
 > Sec-Ch-Ua: "Google Chrome";v="115", "Chromium";v="115", "Not.A/Brand";v="24"
 > Sec-Ch-Ua-Mobile: ?0
 > Sec-Ch-Ua-Platform: "Windows"
 > Sec-Fetch-Dest: empty
 > Sec-Fetch-Mode: cors
 > Sec-Fetch-Site: same-site
 > User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36


```

---
### test_fetchCertOnInit_SAFE

<a name="test_fetchcertoninit_safe"></a>

#### Configurations

- certificateNeedFetch: True

- unsafe: False

- useTLS: False

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
[PASS][SAFE] Initialization with certificateNeedFetch: True

```

---
### test_fetchCertOnInit_UNSAFE

<a name="test_fetchcertoninit_unsafe"></a>

#### Configurations

- certificateNeedFetch: True

- unsafe: True

- useTLS: False

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
[PASS][UNSAFE] Initialization with certificateNeedFetch: True

```

---
### test_mockStatusCodes

<a name="test_mockstatuscodes"></a>

#### Configurations

- certificateNeedFetch: False

- unsafe: False

- useTLS: True

- logToFile: True

- logPath: unitTest/unitTest.log

- suppressWarnings: False

#### Result

- Log Output:

```
[PASS] ContinueException raised for status code 100 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] SwitchingProtocolsException raised for status code 101 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ProcessingException raised for status code 102 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] EarlyHintsException raised for status code 103 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] BadRequestException raised for status code 400 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] UnauthorizedException raised for status code 401 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] PaymentRequiredException raised for status code 402 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ForbiddenException raised for status code 403 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NotFoundException raised for status code 404 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] MethodNotAllowedException raised for status code 405 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NotAcceptableException raised for status code 406 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ProxyAuthenticationRequiredException raised for status code 407 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] RequestTimeoutException raised for status code 408 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ConflictException raised for status code 409 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] GoneException raised for status code 410 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] LengthRequiredException raised for status code 411 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] PreconditionFailedException raised for status code 412 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] PayloadTooLargeException raised for status code 413 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] URITooLongException raised for status code 414 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] UnsupportedMediaTypeException raised for status code 415 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] RangeNotSatisfiableException raised for status code 416 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ExpectationFailedException raised for status code 417 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] MisdirectedRequestException raised for status code 421 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] UnprocessableEntityException raised for status code 422 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] LockedException raised for status code 423 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] FailedDependencyException raised for status code 424 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] TooEarlyException raised for status code 425 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] UpgradeRequiredException raised for status code 426 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] PreconditionRequiredException raised for status code 428 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] TooManyRequestsException raised for status code 429 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] RequestHeaderFieldsTooLargeException raised for status code 431 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] UnavailableForLegalReasonsException raised for status code 451 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] InternalServerErrorException raised for status code 500 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NotImplementedException raised for status code 501 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] BadGatewayException raised for status code 502 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ServiceUnavailableException raised for status code 503 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] GatewayTimeoutException raised for status code 504 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] HTTPVersionNotSupportedException raised for status code 505 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] VariantAlsoNegotiatesException raised for status code 506 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] InsufficientStorageException raised for status code 507 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] LoopDetectedException raised for status code 508 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NotExtendedException raised for status code 510 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NetworkAuthenticationRequiredException raised for status code 511 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] UnknownErrorException raised for status code 520 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] WebServerDownException raised for status code 521 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] ConnectionTimedOutException raised for status code 522 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] OriginUnreachableException raised for status code 523 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] TimeoutOccurredException raised for status code 524 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NetworkReadTimeoutException raised for status code 598 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}
[PASS] NetworkConnectTimeoutException raised for status code 599 with config: {'certificateNeedFetch': False, 'unsafe': False, 'useTLS': True, 'logToFile': True, 'logPath': 'unitTest/unitTest.log', 'suppressWarnings': False}

```

---
