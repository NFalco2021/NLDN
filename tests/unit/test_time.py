import unittest
import pytest
import config as c
import time_functions as t
import time
import datetime
import logging

logging.basicConfig(level=logging.CRITICAL,
                    filename=c.log_file,
                    filemode='a',
                    format=c.log_format,
                    datefmt=c.time_format
                    )


class TestTimeMethods(unittest.TestCase):
    def test_current_time(self):
        self.assertIsInstance(t.return_current_time(), float)
    
    def test_return_formatted_time(self):
        returned_time = t.return_formatted_time()
        self.assertIsInstance(returned_time, str)
        time.sleep(1)
        self.assertNotEqual(returned_time, t.return_formatted_time())
    
    def test_return_iso_time(self):
        test_date = datetime.datetime(year=2022,
                                      month=1,
                                      day=1,
                                      hour=1,
                                      minute=1,
                                      second=1
                                      )
        self.assertEqual(t.return_iso_time(test_date), test_date.isoformat() + 'Z')
        self.assertLogs()

