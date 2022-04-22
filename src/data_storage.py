import csv
import json
import logging
import sys


class DataStorage:
    def __init__(self, formatted_time):
        self.filename = f'NLDN_{formatted_time}.csv'

    # Writes csv_data to the specified filename in the nldn_data directory
    def write_csv(self, csv_data, nldn_data):
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
                with open(nldn_data + self.filename, mode='w+') as f:
                    try:
                        writer = csv.writer(f)
                        writer.writerow(csv_header)
                        for i in csv_data:
                            writer.writerow(i.values())
                    except Exception as ex:
                        logging.exception(f"Exception {ex} occurred")
            except Exception as ex:
                logging.exception(f"Exception {ex} occurred")

    # Reads json file 'path' and returns it's data
    def read_json(self, path):
        with open(path, 'r+') as f:
            try:
                return json.load(f)
            except Exception as ex:
                logging.exception(f"Exception {ex} occurred")

    # Writes 'data' to the specified 'path'
    def write_json(self, path, data):
        with open(path, 'w+') as f:
            try:
                json.dump(data, f)
            except Exception as ex:
                logging.exception(f"Exception {ex} occurred")

    # Getter Methods
    # Returns the filename the data is written to (ie. NLDN_formattedTime)
    def get_filename(self):
        return self.filename
