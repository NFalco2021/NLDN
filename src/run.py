# Run this file to get data caught up for long outages

import logging
import os
import sys

from config import Config
from time_functions import TimeFunctions

# logging.basicConfig(level = logging.INFO,
#                     filename = c.get_log_file(),
#                     filemode = 'a',
#                     format = c.get_log_format(),
#                     datefmt = c.get_log_time_format()
#                     )

if __name__ == '__main__':
    c = Config()
    t = TimeFunctions()
    
    time_diff = t.get_current_utc_time().timestamp() - t.get_run_time(c.get_status_file())
    while time_diff > 7200:
        try:
            os.system("python " + c.get_root_directory() + "vaisala.py")
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")
            time_diff = 0
            sys.exit(3)
        else:
            time_diff = t.get_current_utc_time().timestamp() - t.get_run_time(c.get_status_file())
