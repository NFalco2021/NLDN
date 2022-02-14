import requests
import json
import string
import base64

import config as c

auth_response = requests.request("POST",
                                 c.auth_url,
                                 auth=requests.auth.HTTPBasicAuth(c.username, c.password),
                                 data=c.payload,
                                 headers=c.headers
                                 ).json()

# print(json.dumps(auth_response, indent=4))

access = auth_response["access_token"]
refresh = auth_response["refresh_token"]

# access and refresh tokens are not standard b64
# access_decoded = base64.b64decode(access)
# refresh_decoded = base64.b64decode(refresh)

access_b64diff = set()
refresh_b64diff = set()

for letter in access:
    if letter not in string.ascii_letters:
        if letter not in string.digits:
            access_b64diff.add(letter)

for letter in refresh:
    if letter not in string.ascii_letters:
        if letter not in string.digits:
            refresh_b64diff.add(letter)

print(access_b64diff)
print(refresh_b64diff)

# {'.', '_', '-'} are the results.
# Typical B64 encoding does not use those characters
# I believe they are a replacement for '+', '/', and '=' but not in that order
# Some trial and error is needed to figure out which is which.
