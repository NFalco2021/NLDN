# TODO write all logging outside this file to only raise exceptions
#  and let vaisala.py handle the logging

# TODO add check for datetime of license expiration to notify user
#  in log of expiration and increase log level if it is expired.


import json
import logging
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import requests

import config as c
import data_storage as d
import time_functions as t


def posting(req):
    return '\t{}\n\t{}\n\t{}'.format(
        req.method + ' ' + req.url,
        '\n\t'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body
    )


# This will check the existence of the file
if os.path.exists(c.log_file):
    # If the file exists, this keeps the log file size down to the defined size
    if os.path.getsize(c.log_file) > c.log_size:
        os.rename(c.log_file,
                  c.log_archive + t.return_formatted_time() + '.log'
                  )
else:
    Path(c.log_file).touch(exist_ok=True)

# This is used to keep the NLDN folder down to the defined size
get_size = subprocess.run(['du', '-s', '-B1', c.nldn_data],
                          capture_output=True
                          )

dir_size = int(get_size.stdout.split()[0].decode())

formatted_time = t.return_formatted_time()
archive_name = 'NLDN_' + formatted_time

# TODO add exception handling
if dir_size > c.nldn_size:
    shutil.make_archive(c.nldn_archive + archive_name,
                        'zip',
                        c.nldn_data
                        )
    # This removes all old files from the data directory after it has been archived.
    # TODO this could be implemented better to ensure all files in the archive are the only files being deleted.
    with os.scandir(c.nldn_data) as directory:
        for entry in directory:
            if entry.name.endswith('.csv') and entry.is_file():
                os.remove(entry.path)

logging.basicConfig(level=logging.INFO,
                    filename=c.log_file,
                    filemode='a',
                    format=c.log_format,
                    datefmt=c.time_format
                    )

# Must run t.set_times() before the t.start/stop_iso times will resolve
t.set_times()

# logging.info("Start Time:\t" + str(t.start_time_iso))
logging.info("Stop Time:\t" + str(t.stop_time_iso))

querystring = {"startTime": t.start_time_iso,
               "endTime": t.stop_time_iso,
               "lowerLatitude": c.lower_lat,
               "lowerLongitude": c.lower_lon,
               "upperLatitude": c.upper_lat,
               "upperLongitude": c.upper_lon
               }


auth = requests.request("POST",
                        c.auth_url,
                        auth=requests.auth.HTTPBasicAuth(c.username, c.password),
                        data=c.payload,
                        headers=c.headers
                        )

auth_response = auth.json()

time.sleep(1)
c.headers.update({"Authorization": "Bearer " + auth_response['access_token']})

get_response = requests.request("GET",
                                c.bbox_url,
                                headers=c.headers,
                                params=querystring
                                )

try:
    d.write_csv(get_response.json())
except KeyError:
    logging.exception(f"KeyError occurred - No CSV data\n"
                      f"Auth: {json.dumps(auth_response, indent=4)}\n"
                      f"AuthRequest: {{\n{posting(auth.request)}\n}}\n"
                      f"Response: {json.dumps(get_response.json(), indent=4)}\n"
                      f"ResponseHeaders: {json.dumps(dict(get_response.headers), indent=4)}\n"
                      )
    sys.exit(1)
except IndexError:
    logging.warning(f"IndexError occurred - No Data")
    t.write_time()
except Exception as ex:
    logging.exception(f"Exception {ex} occurred\n"
                      f"Auth: {json.dumps(auth_response, indent=4)}\n"
                      f"GetResponse: {json.dumps(get_response.json(), indent=4)}\n"
                      )
else:
    # Data is copied to the staging directory before it is moved to the ftp.
    # If a problem exists, the .csv files that failed will be in the staging directory.
    shutil.copy2(c.nldn_data + d.filename, c.stage_directory)
    try:
        move_results = subprocess.run(['mv',
                                       c.stage_directory + d.filename,
                                       c.data_destination + d.filename
                                       ],
                                      capture_output=True
                                      )
        
        if c.move_failed in move_results.__str__():
            ftp_test = False
        else:
            ftp_test = True
        
        if c.move_worked in move_results.__str__():
            move_success = True
        else:
            move_success = False
        
        if not (ftp_test or move_success):
            # TODO Consider removing this logging function later.
            logging.info(f"Contents of move_results: "
                         f"FTP_TEST = {ftp_test} "
                         f"MOVE_SUCCESS = {move_success} "
                         f"Results = {(ftp_test or move_success)}"
                         )
            raise BrokenPipeError
    
    except BrokenPipeError as bpe:
        logging.exception(f"FTP (ftp://ftp.aftac.gov) is not mounted. "
                          f"Either mount it manually or change NiFi destination folder"
                          )
        sys.exit(2)
    
    except Exception as ex:
        logging.exception(f"Exception {ex} occurred\n"
                          f"Auth: {json.dumps(auth_response, indent=4)}\n"
                          f"GetResponse: {json.dumps(get_response.json(), indent=4)}\n"
                          )
        sys.exit(3)
    
    else:
        t.write_time()

# logging.info("Time to execute:\t" + str(t.return_current_time() - t.time_started)[0:6] + " Seconds.")
