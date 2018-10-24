#!/usr/bin/env python

import json
import urllib2

def load_json(source):
    """
    get the json data either from URL or from file
    """
    if source.startswith('http'):
        data = json.load(urllib2.urlopen(source))
    else:
        data = json.load(open(source))
    return data

