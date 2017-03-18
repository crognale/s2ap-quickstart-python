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

SERVICE_ACCOUNT_EMAIL_ADDRESS = 'ServiceAccountEmail@developer.gserviceaccount.com'
ISSUER_ID = 'IssuerId'
SERVICE_ACCOUNT_PRIVATE_KEY = 'wobs-privatekey.pem'
APPLICATION_NAME = 'ApplicationName'
DISCOVERY_JSON = 'wobs-discovery.json'
LOYALTY_CLASS_ID = 'LoyaltyClass'
LOYALTY_OBJECT_ID = 'LoyaltyObject'
OFFER_CLASS_ID = 'OfferClass'
OFFER_OBJECT_ID = 'OfferObject'
# List of origins for save to wallet button
ORIGINS = [
    'http://localhost:8080']

# Constants that are application agnostic.
AUDIENCE = 'google'
BAD_REQUEST = 400
LOYALTY_WEB = 'loyaltywebservice'
SAVE_TO_WALLET = 'savetowallet'
SCOPES = 'https://www.googleapis.com/auth/wallet_object.issuer'
