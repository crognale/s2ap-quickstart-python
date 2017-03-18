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

import loyalty
import giftcard
import offer

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

scopes = ['https://www.googleapis.com/auth/wallet_object.issuer']
credentials = ServiceAccountCredentials.from_json_keyfile_name(config.KEYFILE, scopes)
http = httplib2.Http()
http = credentials.authorize(http)

class MainPage(webapp2.RequestHandler):
    def jwt(self, obj, objType):
        loyaltyObjects = []
        giftcardObjects = []
        offerObjects = []

        if objType == 'loyalty':
            loyaltyObjects = [obj]
        elif objType == 'giftcard':
            giftcardObjects = [obj]
        elif objType == 'offer':
            offerObjects = [obj]

        jwt = {
                'iss': config.SERVICE_ACCOUNT,
                'aud': 'google',
                'typ': 'savetoandroidpay',
                'iat':  int(time.time()),
                'payload': {
                        'loyaltyClasses': [], 
                        'giftCardClasses': [],
                        'offerClasses': [],
                        'loyaltyObjects': loyaltyObjects,
                        'giftCardObjects': giftcardObjects,
                        'offerObjects': offerObjects
                },
                'origins' : config.ORIGINS
        }

        with open(config.KEYFILE, 'r') as file_obj:
                client_credentials = json.load(file_obj)
        private_key_pkcs8_pem = client_credentials['private_key']
        signer = crypt.Signer.from_string(private_key_pkcs8_pem)
        signed_jwt = crypt.make_signed_jwt(signer, jwt)
        response = webapp2.Response(signed_jwt)
        return signed_jwt

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        loyalty_jwt = self.jwt(loyalty.loyalty_object(), 'loyalty')
        giftcard_jwt = self.jwt(giftcard.giftcard_object(), 'giftcard')
        offer_jwt = self.jwt(offer.offer_object(), 'offer')
        template_values = {
                'loyalty_jwt': loyalty_jwt,
                'giftcard_jwt': giftcard_jwt,
                'offer_jwt': offer_jwt
                }
        self.response.write(template.render(template_values))

class InsertClass(webapp2.RequestHandler):
    def get(self):
        headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=UTF-8'
        }
        uri = 'https://www.googleapis.com/walletobjects/v1'

        classType = self.request.get('type')

        if classType == 'loyalty':
            path = '/loyaltyClass'
            body = loyalty.loyalty_class()
        elif classType == 'giftcard':
            path = '/giftCardClass'
            body = giftcard.giftcard_class()
        elif classType == 'offer':
            path = '/offerClass'
            body = offer.offer_class()

        method='POST'

        target = urlparse(uri+path)
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
