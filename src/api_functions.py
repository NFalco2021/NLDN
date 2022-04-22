import requests
import string
import json
import base64


class ApiFunctions:
    def __init__(self, auth_url, username, password, payload, headers):
        self.auth_response = self.set_auth_response(auth_url, username, password, payload, headers)
        # print(json.dumps(self.auth_response, indent=4))

        self.access = self.set_access()
        self.refresh = self.set_refresh()

        self.access_b64diff = set()
        self.refresh_b64diff = set()

        # access and refresh tokens are not standard b64
        # self.access_decoded = base64.b64decode(self.access)
        # self.refresh_decoded = base64.b64decode(self.refresh)
        self.set_access_b64diff()
        self.set_refresh_b64diff()

        self.print_access_b64diff()
        self.print_refresh_b64diff()
        # {'.', '_', '-'} are the results.
        # Typical B64 encoding does not use those characters
        # I believe they are a replacement for '+', '/', and '=' but not in that order
        # Some trial and error is needed to figure out which is which.

    def set_auth_response(self, auth_url, username, password, payload, headers):
        return requests.request("POST",
                                auth_url,
                                auth=requests.auth.HTTPBasicAuth(username, password),
                                data=payload,
                                headers=headers
                                ).json()

    def set_access(self):
        return self.auth_response["access_token"]

    def set_refresh(self):
        return self.auth_response["refresh_token"]

    def set_access_b64diff(self):
        for letter in self.access:
            if letter not in string.ascii_letters:
                if letter not in string.digits:
                    self.access_b64diff.add(letter)

    def set_refresh_b64diff(self):
        for letter in self.refresh:
            if letter not in string.ascii_letters:
                if letter not in string.digits:
                    self.refresh_b64diff.add(letter)

    def print_access_b64diff(self):
        print(self.access_b64diff)

    def print_refresh_b64diff(self):
        print(self.refresh_b64diff)
