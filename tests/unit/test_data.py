import unittest
import pytest
import config as c
import data_storage as d
import time_functions as t

from src.data_storage import write_csv
no_key_data = None

class MyTestCase(unittest.TestCase):
    def test_filename(self):
        time_formatted = t.return_formatted_time()
        filename_equivalent = f'NLDN_{time_formatted}.csv'
        self.assertEqual(d.filename, filename_equivalent)

    def test_csv_writer_index(self):
        self.assertRaises(IndexError, write_csv())

    def test_csv_writer_key(self):
        self.assertRaises(KeyError, write_csv(no_key_data))


if __name__ == '__main__':
    unittest.main()
