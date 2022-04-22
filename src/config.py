import json


class Config:
    def __init__(self):
        # Data destination folders.
        self.root_directory = '/home/cse4001/NLDN-New_API_Authentication/'
        self.nldn_data = self.root_directory + 'Data/'
        self.nldn_archive = self.root_directory + 'NLDN_Archive/'
        self.stage_directory = self.root_directory + 'Stage/'
        self.log_archive = self.root_directory + 'Log_Archive/'
        self.data_destination = self.root_directory + 'Destination/'

        # Time format
        self.time_format = '%Y-%m-%dT%H.%M.%S'
        # Decimal seconds used to make sure name is unique.
        self.filename_format = self.time_format + '.%f'

        # TODO put all configuration and tracked data (like NLDN.json) into a single file.
        # Location of file used to track the last time the program successfully ran.
        self.status_file = self.stage_directory + 'NLDN.json'

        # Log file parameters
        self.log_file = self.stage_directory + 'vaisala.log'
        self.log_format = '%(asctime)s %(levelname)s:\t%(module)s@%(lineno)d \t%(funcName)s - %(message)s'
        self.log_template = "An exception of type {0} occurred. Arguments:\n{1!r}"

        # 1048576 is one megabyte
        self.log_size = 1048576
        self.nldn_size = self.log_size * 1024

        # API connection parameters
        # self.auth_url = "https://lightning-exporter.vaisala.io/spring-security-oauth-server/oauth/token"
        # self.bbox_url = "https://lightning-exporter.vaisala.io/ltg-api/ltgs/bbox"
        self.auth_url = "https://ltg-auth.vaisala.com/auth/realms/vaisala-dig-ltg/protocol/openid-connect/token"
        self.bbox_url = "https://ltg.vaisala.com/realtime/merge/api/v1/ltgs/bbox"
        self.username = 'lightning-api'
        self.password = 'password'
        self.headers = {'Content-Type': "application/x-www-form-urlencoded",
                        'cache-control': "no-cache"
                        }

        # authentication.json needs to reflect actual URL encoded username and password
        # auth_file below is used for GitHub, the one below it is for testing as it has real authentication credentials.
        self.auth_file = self.stage_directory + 'authentication.json'
        # self.auth_file = '/home/falco/Desktop/authentication.json'
        # self.auth_file = '/home/falco/Desktop/NewAuthentication.json'

        self.payload = self.read_json(self.auth_file)["Password"]

        self.move_worked = 'Operation not supported'
        self.move_failed = 'No such file or directory'

        # CONUS bounding box GPS coordinates used for API search.
        self.lower_lat = '24'
        self.lower_lon = '-126'
        self.upper_lat = '50'
        self.upper_lon = '-65'

    # Reads and returns json data from 'path'
    def read_json(self, path):
        with open(path, 'r+') as f:
            try:
                return json.load(f)
            except Exception as ex:
                print(f"Exception {ex} occurred")

    # Updates headers with the new header information
    def update_headers(self, new_headers):
        self.headers.update(new_headers)

    # Getter Methods
    # Get methods for Data Destination Folders
    def get_root_directory(self):
        return self.root_directory

    def get_nldn_data(self):
        return self.nldn_data

    def get_nldn_archive(self):
        return self.nldn_archive

    def get_stage_directory(self):
        return self.stage_directory

    def get_log_archive(self):
        return self.log_archive

    def get_data_destination(self):
        return self.data_destination

    # Getter Methods for Time Format
    def get_filename_format(self):
        return self.filename_format

    def get_time_format(self):
        return self.time_format

    # Getter Methods for API Connection Parameters
    def get_auth_url(self):
        return self.auth_url

    def get_bbox_url(self):
        return self.bbox_url

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_payload(self):
        return self.payload

    def get_headers(self):
        return self.headers

    # Getter Method for Status File
    def get_status_file(self):
        return self.status_file

    # Getter Methods for Log File Parameters
    def get_log_file(self):
        return self.log_file

    def get_log_format(self):
        return self.log_format

    def get_log_size(self):
        return self.log_size
        
    def get_nldn_size(self):
        return self.nldn_size

    # Getter Methods for fail/work statements
    def get_move_failed(self):
        return self.move_failed

    def get_move_worked(self):
        return self.move_worked

    # Getter Methods for CONUS bounding box GPS coordinates
    def get_lower_lon(self):
        return self.lower_lon

    def get_lower_lat(self):
        return self.lower_lat

    def get_upper_lon(self):
        return self.upper_lon

    def get_upper_lat(self):
        return self.upper_lat

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

    # TODO Add a way to update the allowed range of data variables received when an API request is returned.
    #  Perhaps only once or twice a year. Think about storing it in last_ran file.
    #  If that's the route, update the name again.

    # Example of the limits of the API given back by Vaisala in their requests.
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
