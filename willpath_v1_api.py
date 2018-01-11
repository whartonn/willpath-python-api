#!/usr/bin/env python
# encoding: utf-8
"""
Simple Willpath Python API
Created by Nathaniel Wharton on 2012-02-14.
nat.wharton@willpath.com
wharton.n@gmail.com

This sends gzip-encoded API requests to Willpath and decodes the result into Python dictionaries.
Tested under python 2.6.1, but later 2.x versions should work fine.

1. Please read the api documentation. Please don't go over the rate-lmits!
2. Install these dependencies (e.g.: using pip):
pip install urllib3
pip install git+ssh://git@github.com/shazow/apiclient.git
3. Update USER and PW constants below.
4. Copy/paste/save this code into a file called "willpath_v1_api.py"
(or you can clone this file/project into its own folder using:
  git clone git://github.com/nat/willpath-python-api.git 
 )
5. In your own file you can then write code such as this:
from willpath_v1_api import WillpathV1API
api = WillpathV1API()
r = api.call('/api/v1/people.json', updated_since='2012-02-10T12:36:42Z')
print r
6. hooray!

"""
from apiclient import APIClient
import urllib3
import json

class WillpathV1API(APIClient):
    BASE_URL = 'https://willpath.com'
    USER = 'yourusername'
    PW = 'yourpassword'

    def _request(self, method, path, params=None):
        url = self._compose_url(path, params)
        self.rate_limit_lock and self.rate_limit_lock.acquire()
        auth_string = self.USER + ":" + self.PW
        headers = urllib3.make_headers(basic_auth=auth_string,accept_encoding=True)
        r = self.connection_pool.urlopen(method.upper(), url, headers=headers)
        return self._handle_response(r)

      

if __name__ == '__main__':
    api = WillpathV1API()
    r = api.call('/api/v1/people.json', updated_since='2012-02-10T12:36:42Z')
    print r

