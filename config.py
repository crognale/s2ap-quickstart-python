"""
Copyright 2017 Google Inc. All Rights Reserved.

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

SERVICE_ACCOUNT = '<YOUR SERVICE ACCOUNT HERE>'
ISSUER_ID = '<YOUR ISSUER ID HERE>'


# IDs for Class and Object insertion. A Class with a given Class ID can only be
# inserted once. 
LOYALTY_CLASS_ID = 'quickstart_loyalty_test'
LOYALTY_OBJECT_ID = 'quickstart_loyalty_test_obj0'

GIFTCARD_CLASS_ID = 'quickstart_giftcard_test'
GIFTCARD_OBJECT_ID = 'quickstart_giftcard_test_obj0'

OFFER_CLASS_ID = 'quickstart_offer_test'
OFFER_OBJECT_ID = 'quickstart_offer_test_obj0'


# Origins from which the Save to Android Pay web button will be allowed to serve.
# In production, this will be the hostname of your public-facing site.
# 'localhost' and '0.0.0.0' are typical values for testing.
ORIGINS = ['<YOUR ORIGINS HERE>']

#Keyfile path
KEYFILE = 'keys/keyFile.json'

# Hostname and port for serving the web app.
# 'HTTP_HOST:HTTP_PORT' should also be included in the above ORIGINS array.
HTTP_HOST = '0.0.0.0'
HTTP_PORT = '8080'
