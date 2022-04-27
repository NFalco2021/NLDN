#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Site:
    def __init__(self, name=None, upper_lat=None, upper_long=None, lower_lat=None, lower_long=None):
        self.name = name
        self.upper_lat = upper_lat
        self.upper_long = upper_long
        self.lower_lat = lower_lat
        self.lower_long = lower_long
