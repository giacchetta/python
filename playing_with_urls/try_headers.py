#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json, base64

url = 'https://gitlab.com/api/v4/groups/1/variables/A'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'PRIVATE-TOKEN': 'X'}

req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req).read()
values = json.loads(resp)
base = base64.b64decode(values['value'])
print(base)