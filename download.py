#!/usr/bin/python

import json
import urllib

import os
import requests


def downloadfile(url, filePath):
    try:
        urllib.urlretrieve(url, filePath)
    except:
        print '\t url is error', filePath


url = 'http://api-app.smartisan.com/app/index.php?r=paperapi/index/list&client_version=2&limit=100&paper_id=0'
result = requests.get(url).content
jsonStr = json.loads(result)

fileRoot = 'D:/sos/'
if not os.path.exists(fileRoot):
    os.makedirs(fileRoot)

for item in jsonStr['data']:
    download = item['url']
    filePath = fileRoot + item['id'] + '.jpg'
    downloadfile(download, filePath)
    print 'down ' + download
