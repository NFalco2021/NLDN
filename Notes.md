# Authentication
## Request

```bash
GET /api/v1/auth/token?application=ltg-api&username=username%40email.com&password=hunter2 HTTP/2
Host: ltg-auth.vaisala.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Accept: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ltg-auth.vaisala.com/swagger-ui/index.html
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## Response

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 02:10:46 GMT
Content-Type: application/json
Vary: origin,access-control-request-method,access-control-request-headers,accept-encoding
```
```json
{
	"access_token":"[access_token]",
	"expires_in":3600,
	"refresh_token":"[refresh_token]",
	"refresh_expires_in":7200,
	"token_type":"Bearer",
	"not-before-policy":0,
	"session_state":"db73b307-d77c-48c5-b42b-8818dc55a16d",
	"scope":"profile authz-info read"
}
```

# API call for NLDN data in JSON
## Request

```bash
GET /realtime/merge/api/v1/ltgs/bbox?start=2022-03-03T10%3A00%3A00Z&end=2022-03-03T16%3A00%3A00Z&left=-126&bottom=24&right=-65&top=50&amplitudeRanges=15..80&cloud=false&inclEllipse=80&fields=analysis&fields=research&fields=ldi_sdp&page=0&size=200 HTTP/2
Host: ltg.vaisala.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Accept: application/json
Authorization: Bearer [access_token]
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ltg.vaisala.com/realtime/merge/webjars/swagger-ui/index.html?configUrl=/realtime/merge/v3/api-docs/swagger-config
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## Response
### Original

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 02:24:55 GMT
Content-Type: application/json
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1 ; mode=block

[Data removed for brevity]
```

### Edited

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 02:24:55 GMT
Content-Type: application/json
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: *
Content-Length: 186282

[Data removed for brevity]
```

## Differences in response
### Removed from Original

```bash
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1 ; mode=block
```

### Added by me

```bash
Access-Control-Allow-Origin: *
```

### Added by Vaisala

```bash
Content-Length: 186282
```

# API call for NLDN data in csv

## Request
### Original

```bash
GET /realtime/merge/api/v1/ltgs/bbox?start=2022-03-03T10%3A00%3A00Z&end=2022-03-03T16%3A00%3A00Z&left=-126&bottom=24&right=-65&top=50&cloud=true&fields=&page=0&size=20 HTTP/2
Host: ltg.vaisala.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Accept: application/json
Authorization: Bearer [access_token]
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ltg.vaisala.com/realtime/merge/webjars/swagger-ui/index.html?configUrl=/realtime/merge/v3/api-docs/swagger-config
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

### Edited

```bash
GET /realtime/merge/api/v1/ltgs/bbox?start=2022-03-03T10%3A00%3A00Z&end=2022-03-03T16%3A00%3A00Z&left=-126&bottom=24&right=-65&top=50&cloud=true&fields=&page=0&size=20 HTTP/2
Host: ltg.vaisala.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Accept: text/csv
Authorization: Bearer [access_token]
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ltg.vaisala.com/realtime/merge/webjars/swagger-ui/index.html?configUrl=/realtime/merge/v3/api-docs/swagger-config
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

## Response
### Original

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 04:15:19 GMT
Content-Type: text/csv
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1 ; mode=block

time,longitude,latitude,signalStrengthKA,cloud
2022-03-03T10:20:43.371Z,-70.7718,38.4996,-19.9,true
2022-03-03T10:35:45.999Z,-79.7965,38.9488,-6.4,true
2022-03-03T10:38:18.736Z,-70.5188,38.5607,-36.2,true
2022-03-03T10:45:18.688Z,-69.9791,38.8759,-26.1,true
2022-03-03T10:45:18.688Z,-70.0716,38.8726,-14.4,true
2022-03-03T10:46:59.872Z,-69.9375,38.877,-31.7,true
2022-03-03T10:51:40.827Z,-70.5223,38.4187,-29.8,true
2022-03-03T10:53:26.300Z,-70.4625,38.4362,-28.2,true
2022-03-03T10:53:26.300Z,-70.4563,38.4336,-35.3,true
2022-03-03T10:53:50.562Z,-70.2816,38.6502,-18.7,true
2022-03-03T10:55:12.914Z,-70.2528,38.6523,-15.8,true
2022-03-03T10:56:35.614Z,-70.697,38.3949,-14.2,true
2022-03-03T10:56:35.614Z,-70.7094,38.3919,-18.0,true
2022-03-03T10:56:35.614Z,-70.6961,38.3985,-21.9,true
2022-03-03T10:56:39.403Z,-70.0609,38.9246,87.1,false
2022-03-03T10:56:39.762Z,-70.0109,38.8947,-14.3,false
2022-03-03T11:04:02.784Z,-69.7481,38.9429,-15.6,true
2022-03-03T11:05:37.005Z,-70.5732,38.106,-15.3,true
2022-03-03T11:06:06.814Z,-70.4754,38.1836,-15.1,true
2022-03-03T11:06:06.814Z,-70.4155,38.1854,-16.5,true
```

### Edited

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 04:15:19 GMT
Content-Type: text/csv
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: *
Content-Length: 1104

time,longitude,latitude,signalStrengthKA,cloud
2022-03-03T10:20:43.371Z,-70.7718,38.4996,-19.9,true
2022-03-03T10:35:45.999Z,-79.7965,38.9488,-6.4,true
2022-03-03T10:38:18.736Z,-70.5188,38.5607,-36.2,true
2022-03-03T10:45:18.688Z,-69.9791,38.8759,-26.1,true
2022-03-03T10:45:18.688Z,-70.0716,38.8726,-14.4,true
2022-03-03T10:46:59.872Z,-69.9375,38.877,-31.7,true
2022-03-03T10:51:40.827Z,-70.5223,38.4187,-29.8,true
2022-03-03T10:53:26.300Z,-70.4625,38.4362,-28.2,true
2022-03-03T10:53:26.300Z,-70.4563,38.4336,-35.3,true
2022-03-03T10:53:50.562Z,-70.2816,38.6502,-18.7,true
2022-03-03T10:55:12.914Z,-70.2528,38.6523,-15.8,true
2022-03-03T10:56:35.614Z,-70.697,38.3949,-14.2,true
2022-03-03T10:56:35.614Z,-70.7094,38.3919,-18.0,true
2022-03-03T10:56:35.614Z,-70.6961,38.3985,-21.9,true
2022-03-03T10:56:39.403Z,-70.0609,38.9246,87.1,false
2022-03-03T10:56:39.762Z,-70.0109,38.8947,-14.3,false
2022-03-03T11:04:02.784Z,-69.7481,38.9429,-15.6,true
2022-03-03T11:05:37.005Z,-70.5732,38.106,-15.3,true
2022-03-03T11:06:06.814Z,-70.4754,38.1836,-15.1,true
2022-03-03T11:06:06.814Z,-70.4155,38.1854,-16.5,true
```

## Differences in response
### Removed from Original

```bash
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Xss-Protection: 1 ; mode=block
```

### Added by me

```bash
Access-Control-Allow-Origin: *
```

### Added by Vaisala

```bash
Content-Length: 1104
```

# Information
## API won't return every column in requests
Note the infomation in the get request

### Edited Request

```bash
GET /realtime/merge/api/v1/ltgs/bbox?start=2022-03-03T10%3A00%3A00Z&end=2022-03-03T16%3A00%3A00Z&left=-126&bottom=24&right=-65&top=50&amplitudeRanges=15..80&cloud=true&inclEllipse=80&fields=analysis&fields=research&fields=ldi_sdp&page=0&size=250000 HTTP/2
Host: ltg.vaisala.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Accept: text/csv
```

### Edited Response

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 04:28:41 GMT
Content-Type: text/csv
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: *
Content-Length: 54768

time,longitude,latitude,signalStrengthKA,cloud,ellSemiMajM,ellSemiMinM,ellAngleDeg
2022-03-03T11:10:22.645Z,-70.262,38.4607,15.0,true,2477,288,86
2022-03-03T11:13:55.691Z,-69.8689,38.8931,41.0,false,229,200,128
2022-03-03T11:17:12.038Z,-69.8083,38.9219,35.3,false,206,200,125
2022-03-03T11:18:50.584Z,-69.5287,38.9834,25.8,false,225,200,125
2022-03-03T11:19:08.171Z,-70.1267,40.5835,18.6,false,310,200,109
2022-03-03T11:33:13.670Z,-69.5586,40.2468,74.0,false,338,200,111
2022-03-03T11:35:20.021Z,-69.619,38.7184,21.1,true,827,200,91
...
2022-03-03T15:59:58.879Z,-66.9259,38.044,21.0,true,1482,779,3
```

## Other types data could be returned as

GeoJSON: application/geo+json
Streaming JSON: application/x-ndjson
Streaming CSV: text/event-stream

## Max output
The output of this API is limited to 250000 rows per page.

## Reaching the end
### text/csv
If there is no more data to return that matches the parameters given the next page will just contain the column names with no data.
Two ways to check you received all the data:
1. Check the next page until Python throws an ```IndexError``` when you write the received data to a file.
2. Check the number of lines returned against the ```size``` argument you pass in your API call

#### Edited Request - Abriged

```bash
GET /realtime/merge/api/v1/ltgs/bbox?start=2022-03-03T10%3A00%3A00Z&end=2022-03-03T16%3A00%3A00Z&left=-126&bottom=24&right=-65&top=50&amplitudeRanges=15..80&cloud=true&inclEllipse=80&fields=analysis&fields=research&fields=ldi_sdp&page=1&size=250000 HTTP/2
Host: ltg.vaisala.com
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="92"
Accept: text/csv
```

#### Edited Response

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 04:36:56 GMT
Content-Type: text/csv
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: *
Content-Length: 85


time,longitude,latitude,signalStrengthKA,cloud,ellSemiMajM,ellSemiMinM,ellAngleDeg
```

### application/json
The body of the Response will be empty

#### Edited Response if Request above accepted JSON data instead

```bash
HTTP/2 200 OK
Date: Wed, 13 Apr 2022 04:47:17 GMT
Content-Type: application/json
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: 0
Pragma: no-cache
Referrer-Policy: no-referrer
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: *
Content-Length: 4


[]
```