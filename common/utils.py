#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import requests

# Common use utils function

def url_status(url, base_auth = False):
    if not url:
        return False
    url = url_remove_duplicate_slash(url)
    res = requests.head(url, auth = ('hdguest', 'MLP@2017')) if base_auth else requests.head(url, allow_redirects=True)
    # fixed 405 issue. https://stackoverflow.com/questions/27763431/getting-http-header-with-python-getting-405
    if res.status_code == requests.codes.method_not_allowed:
        res = requests.get(url)
    return res.status_code == requests.codes.ok

def url_remove_duplicate_slash(url):
    """
    refer to : https://stackoverflow.com/questions/24381480/remove-duplicate-forward-slashes-from-the-url?lq=1
    """
    if not url:
        return url
    return re.sub(r'([^:]\/)\/+', r'\1', url)