import sys
import csv
import json
import logging

import config as c
import time_functions as t

filename = f'NLDN_{t.return_formatted_time()}.csv'


def write_csv(csv_data):
    # Use this to troubleshoot index problem
    # print(csv_data)
    try:
        csv_header = csv_data[0]
    except IndexError:
        raise IndexError
    except KeyError:
        raise KeyError
    except Exception as ex:
        logging.exception(f"Exception {ex} occurred\nData:\t{csv_data}")
        sys.exit(1)
    else:
        try:
            with open(c.nldn_data + filename, mode='w+') as f:
                try:
                    writer = csv.writer(f)
                    writer.writerow(csv_header)
                    for i in csv_data:
                        writer.writerow(i.values())
                except Exception as ex:
                    logging.exception(f"Exception {ex} occurred")
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")


def read_json(path):
    with open(path, 'r+') as f:
        try:
            return json.load(f)
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")


def write_json(path, data):
    with open(path, 'w+') as f:
        try:
            json.dump(data, f)
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")
