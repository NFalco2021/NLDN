import json

# Data destination folders.
root_directory = '/home/falco/Desktop/NLDN/'
nldn_data = root_directory + 'Data/'
nldn_archive = root_directory + 'NLDN_Archive/'
stage_directory = root_directory + 'Stage/'
log_archive = root_directory + 'Log_Archive/'
data_destination = root_directory + 'Destination/'

# Time format
time_format = '%Y-%m-%dT%H.%M.%S'
# Decimal seconds used to make sure name is unique.
filename_format = time_format + '.%f'

# TODO put all configuration and tracked data (like NLDN.json) into a single file.
# Location of file used to track the last time the program successfully ran.
status_file = stage_directory + 'NLDN.json'

# Log file parameters
log_file = stage_directory + 'vaisala.log'
log_format = '%(asctime)s %(levelname)s:\t%(module)s@%(lineno)d \t%(funcName)s - %(message)s'
log_template = "An exception of type {0} occurred. Arguments:\n{1!r}"

# 1048576 is one megabyte
log_size = 1048576
nldn_size = log_size * 1024

# API connection parameters
# auth_url = "https://lightning-exporter.vaisala.io/spring-security-oauth-server/oauth/token"
auth_url = "https://ltg-auth.vaisala.com/auth/realms/vaisala-dig-ltg/protocol/openid-connect/token"
bbox_url = "https://lightning-exporter.vaisala.io/ltg-api/ltgs/bbox"
username = 'lightning-api'
password = 'password'
headers = {'Content-Type': "application/x-www-form-urlencoded",
           'cache-control': "no-cache"
           }

# authentication.json needs to reflect actual URL encoded username and password
# auth_file below is used for GitHub, the one below it is for testing as the file has real authentication credentials.
# auth_file = stage_directory + 'authentication.json'
# auth_file = '/home/falco/Desktop/authentication.json'
auth_file = '/home/falco/Desktop/NewAuthentication.json'


def read_json(path):
    with open(path, 'r+') as f:
        try:
            return json.load(f)
        except Exception as ex:
            print(f"Exception {ex} occurred")


payload = read_json(auth_file)["Password"]

# TODO Find a better way to do the swap between an example authentication file and the real one.

# Proxy server would be added like this if they are needed.
# Would have to add parameter to the requests.request method calls.
# Example: requests.request("GET", c.bbox_url, proxies=c.proxy, headers=c.headers, params=querystring)
#
# proxy_server = '10.150.206.21:8080'
#
# # Sets the proxy variable so that it can be used in requests.
# proxy = {'http': proxy_server,
#          'https': proxy_server,
#          'ftp': proxy_server
#          }

move_worked = 'Operation not supported'
move_failed = 'No such file or directory'

# CONUS bounding box GPS coordinates used for API search.
lower_lat = '24'
lower_lon = '-126'
upper_lat = '50'
upper_lon = '-65'

# TODO Add a way to update the allowed range of data variables received when an API request is returned.
#  Perhaps only once or twice a year. Think about storing it in last_ran file.
#  If that's the route, update the name again.

# Limits of the API given back by Vaisala in their requests.
'''
Entire Area Allowed by Vaisala
lower_lat = '0'
lower_lon = '-180'
upper_lat = '73'
upper_lon = '-50'

Date range of data allowed by Vaisala
Start Date: August 14, 2016 00:00:00Z
Start Epoch: 1471132800000
Stop Date: August 14, 2020 00:00:00Z
Stop Epoch: 1597363200000
'''
