import datetime
import json
import logging
import sys
import time
import pytz


class TimeFunctions:
    def __init__(self):
        # Used for timing of program running
        # time_started = time.time()

        # Can define to limit search to a given year instead of constantly seeking a new time.
        self.current_utc_time = datetime.datetime.utcnow()

        self.start_time_iso = ''
        self.stop_time_iso = ''

        # Time delta between data collects after an outage to get caught back up
        # Changed to make files smaller while requesting back-fill.
        # Increase to 20 when finished.
        self.outage_delta = datetime.timedelta(minutes=20)
        # Overlap between collects
        self.start_delta = datetime.timedelta(seconds=1)
        # Normal collection time
        self.stop_delta = datetime.timedelta(minutes=5)

    # Reads and returns json data from 'path'
    def read_json(self, path):
        with open(path, 'r+') as f:
            try:
                return json.load(f)
            except Exception as ex:
                logging.exception(f"Exception {ex} occurred")

    # Writes json 'data' to 'path'
    def write_json(self, path, data):
        with open(path, 'w+') as f:
            try:
                json.dump(data, f, indent=4)
            except Exception as ex:
                logging.exception(f"Exception {ex} occurred")

    # Writes time the program stopped to the status_file as json data
    def write_time(self, status_file):
        time_data = {'Time Last Ran': time_stopped.timestamp()}
        self.write_json(status_file, time_data)

    # Setter Methods
    def set_iso_time(self, start, stop):
        global time_stopped
        self.start_time_iso = self.get_iso_time(start)
        self.stop_time_iso = self.get_iso_time(stop)
        time_stopped = stop

    def set_times(self, status_file):
        # Controls how much time must pass from time_last_ran before script will execute
        delay = int(self.stop_delta.total_seconds()) * 4

        # Used to be an intermediate timedelta between big_outage and stop_delta
        # Ensures requested data doesn't exceed the delay by more than one stop_delta
        small_outage = int(self.stop_delta.total_seconds()) * 6

        # Adjust to fine tune how fast script will get caught up after outage
        big_outage = int(self.outage_delta.total_seconds()) + small_outage

        # Calculate time difference since script last ran successfully
        self.get_last_run_time(status_file)
        time_diff = self.current_utc_time.timestamp() - time_last_ran.timestamp()

        # Added for debugging and tracking how long data has left.
        # difference = str(int(time_diff))
        # files_left = str(int(time_diff // 1200))
        # logging.info(f'TimeDiff: {time_diff:.2f}\tFiles left: {time_diff // 1200}')

        # Adds the start_delta overlap at the beginning of the search
        start_time = time_last_ran - self.start_delta

        # Determines if outage_delta should be used or not.
        # Will slowly catch up until time_diff < small_outage
        # Currently only retrieving data older than 15 minutes (delay(20) - stop_delta(5) = 15 minutes)
        if time_diff > big_outage:
            stop_time = time_last_ran + self.outage_delta
        elif time_diff > small_outage:
            stop_time = time_last_ran + (self.stop_delta * 2)
        elif time_diff > delay:
            stop_time = time_last_ran + self.stop_delta
        else:
            logging.warning(f'Program running too often\tTimeDiff:\t{time_diff}')
            sys.exit()
        self.set_iso_time(start_time, stop_time)

    # Getter Methods
    # Use this to get UTC timestamp
    def get_utc_timestamp(self, day=1, month=1, year=2022):
        return datetime.datetime(year=year,
                                 month=month,
                                 day=day,
                                 tzinfo=pytz.UTC
                                 ).timestamp()

    # Returns the current time
    def get_current_time(self):
        return time.time()

    # Function returns time with '.' to delimit between hours/minutes/seconds
    def get_formatted_time(self, filename_format):
        try:
            return datetime.datetime.utcnow().strftime(filename_format)
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")

    # Function returns time with ':' to delimit between hours/minutes/seconds with 'Z' appended to the end
    # Could combine with return_formatted_time in future refactor
    def get_iso_time(self, date):
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

    # Returns last successful runtime of the program, read from the status file
    def get_last_run_time(self, status_file):
        global time_last_ran
        time_data = self.read_json(status_file)
        try:
            time_last_ran = datetime.datetime.fromtimestamp(float("%.6f" % time_data['Time Last Ran']))
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")

    # For Testing
    def get_run_time(self, status_file):
        time_data = self.read_json(status_file)
        return datetime.datetime.fromtimestamp(time_data['Time Last Ran']).timestamp()

    def get_start_time_iso(self):
        return self.start_time_iso

    def get_stop_time_iso(self):
        return self.stop_time_iso
        
    def get_current_utc_time(self):
        return self.current_utc_time
