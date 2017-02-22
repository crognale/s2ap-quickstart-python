"""
Copyright 2013 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import config

import webapp2
from paste import httpserver
import jinja2
import os

import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import crypt
import time
import json
from urlparse import urlparse
import urllib


JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

scopes = ['https://www.googleapis.com/auth/wallet_object.issuer']
credentials = ServiceAccountCredentials.from_json_keyfile_name(config.KEYFILE, scopes)
http = httplib2.Http()
http = credentials.authorize(http)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {}
        self.response.write(template.render(template_values))

class InsertClass(webapp2.RequestHandler):
    def get(self):

        headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=UTF-8'
        }
        uri = 'https://www.googleapis.com/walletobjects/v1'

        path = '/loyaltyClass'
        method='POST'
        params = ''

        body = {
            'id': '3160309091166180250.quickstart_loyalty_test', 
            'issuerName': 'Test Hero Image 0 ',
            'programLogo': {
                'kind': 'walletobjects#image',
                'sourceUri': {
                    'kind': 'walletobjects#uri',
                    'uri': 'http://farm8.staticflickr.com/7340/11177041185_a61a7f2139_o.jpg'
                }
            },
            'programName': 'Program Name',
            'renderSpecs': [
                {
                    'templateFamily': '1.loyalty_list',
                    'viewName': 'g_list'
                },
                {
                    'templateFamily': '1.loyalty_expanded',
                    'viewName': 'g_expanded'
                }
            ],
            'reviewStatus': 'underReview'
        }

        target = urlparse(uri+path+'?'+params)

        response, content = http.request(
                target.geturl(),
                method,
                json.dumps(body),
                headers)

        data = json.loads(content)

        self.response.write(json.dumps(data, indent=4))

class AppJs(webapp2.RequestHandler):
    def get(self):
        with open('js/app.js') as f:
            data = f.read()
        self.response.headers['Content-Type'] = 'application/javascript'
        self.response.out.write(data)


routes = [
	('/', MainPage),
        ('/insertClass', InsertClass),
        ('/app.js', AppJs)
]

app = webapp2.WSGIApplication(routes, debug=True)
httpserver.serve(app, host=config.HTTP_HOST, port=config.HTTP_PORT)
