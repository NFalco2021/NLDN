import datetime
import json
import logging
import sys
import time
import pytz

import config as c


# Use this to get UTC timestamp
def get_utc_timestamp(day=1, month=1, year=2022):
    return datetime.datetime(year=year,
                             month=month,
                             day=day,
                             tzinfo=pytz.UTC
                             ).timestamp()


# Used for timing of program running
# time_started = time.time()

# Can define to limit search to a given year instead of constantly seeking a new time.
current_utc_time = datetime.datetime.utcnow()

start_time_iso = ''
stop_time_iso = ''

# Time delta between data collects after an outage to get caught back up
# Changed to make files smaller while requesting back-fill.
# Increase to 20 when finished.
outage_delta = datetime.timedelta(minutes=20)
# Overlap between collects
start_delta = datetime.timedelta(seconds=1)
# Normal collection time
stop_delta = datetime.timedelta(minutes=5)


def return_current_time():
    return time.time()


# Function returns time with '.' to delimit between hours/minutes/seconds
def return_formatted_time():
    try:
        return datetime.datetime.utcnow().strftime(c.filename_format)
    except Exception as ex:
        logging.exception(f"Exception {ex} occurred")


# Function returns time with ':' to delimit between hours/minutes/seconds with 'Z' appended to the end
# Could combine with return_formatted_time in future refactor
def return_iso_time(date):
    try:
        iso_date = datetime.datetime(year=date.year,
                                     month=date.month,
                                     day=date.day,
                                     hour=date.hour,
                                     minute=date.minute,
                                     second=date.second
                                     )
    except Exception as ex:
        logging.exception(f"Exception {ex} occurred")
    else:
        return iso_date.isoformat() + 'Z'


def assign_iso_time(start, stop):
    global start_time_iso, stop_time_iso, time_stopped
    start_time_iso = return_iso_time(start)
    stop_time_iso = return_iso_time(stop)
    time_stopped = stop


def read_json(path):
    with open(path, 'r+') as f:
        try:
            return json.load(f)
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")


def write_json(path, data):
    with open(path, 'w+') as f:
        try:
            json.dump(data, f, indent=4)
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")


def write_time():
    time_data = {'Time Last Ran': time_stopped.timestamp()}
    write_json(c.status_file, time_data)


def get_last_run_time():
    global time_last_ran
    time_data = read_json(c.status_file)
    try:
        time_last_ran = datetime.datetime.fromtimestamp(float("%.6f" % time_data['Time Last Ran']))
    except Exception as ex:
        logging.exception(f"Exception {ex} occurred")


# For Testing
def return_run_time():
    time_data = read_json(c.status_file)
    return datetime.datetime.fromtimestamp(time_data['Time Last Ran']).timestamp()


def set_times():
    # Controls how much time must pass from time_last_ran before script will execute
    delay = int(stop_delta.total_seconds()) * 4
    
    # Used to be an intermediate timedelta between big_outage and stop_delta
    # Ensures requested data doesn't exceed the delay by more than one stop_delta
    small_outage = int(stop_delta.total_seconds()) * 6
    
    # Adjust to fine tune how fast script will get caught up after outage
    big_outage = int(outage_delta.total_seconds()) + small_outage
    
    # Calculate time difference since script last ran successfully
    get_last_run_time()
    time_diff = current_utc_time.timestamp() - time_last_ran.timestamp()
    
    # Added for debugging and tracking how long data has left.
    # difference = str(int(time_diff))
    # files_left = str(int(time_diff // 1200))
    # logging.info(f'TimeDiff: {time_diff:.2f}\tFiles left: {time_diff // 1200}')
    
    # Adds the start_delta overlap at the beginning of the search
    start_time = time_last_ran - start_delta
    
    # Determines if outage_delta should be used or not.
    # Will slowly catch up until time_diff < small_outage
    # Currently only retrieving data older than 15 minutes (delay(20) - stop_delta(5) = 15 minutes)
    if time_diff > big_outage:
        stop_time = time_last_ran + outage_delta
    elif time_diff > small_outage:
        stop_time = time_last_ran + (stop_delta * 2)
    elif time_diff > delay:
        stop_time = time_last_ran + stop_delta
    else:
        logging.warning(f'Program running too often\tTimeDiff:\t{time_diff}')
        sys.exit()
    assign_iso_time(start_time, stop_time)
