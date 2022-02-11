#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23, 2019

@author: Nick Falco
"""

# Run this file to get data caught up for long outages

import sys
import logging
import os

import time_functions as t
import config as c

# logging.basicConfig(level = logging.INFO,
#                     filename = c.log_file,
#                     filemode = 'a',
#                     format = c.log_format,
#                     datefmt = c.log_time_format
#                     )

if __name__ == '__main__':
    time_diff = t.current_utc_time.timestamp() - t.return_run_time()
    while time_diff > 7200:
        try:
            os.system("python " + c.root_directory + "vaisala.py")
        except Exception as ex:
            logging.exception(f"Exception {ex} occurred")
            time_diff = 0
            sys.exit(3)
        else:
            time_diff = t.current_utc_time.timestamp() - t.return_run_time()
