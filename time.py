#!/usr/bin/env python

import calendar
from datetime import timedelta, datetime
from time import strptime, mktime


def timeconverter2seconds(timestring):
    """
    converts time from string with date in expected format to 
    seconds since epoch
    """
    # timestring = "2011-11-02 15:28:01"
    time_format1 = "%Y-%m-%d %H:%M:%S"
    # timestring = "2013-09-14T23:59:00"
    time_format2 = "%Y-%m-%dT%H:%M:%S"
    try:
        mytime = datetime.strptime(timestring, time_format1)
    except ValueError:
        mytime = datetime.strptime(timestring, time_format2)
    out = calendar.timegm(mytime.timetuple())
    return out


def timestamp_now():
    """
    returns a timestamp, in UTC, for this instant right now
    """
    out = datetime.utcnow().strftime("%F %H:%M UTC")
    return out
