'''
Copyright 2013 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

def generate_loyalty_class(issuer_id, class_id):
  loyalty_class = {
      'accountIdLabel': 'Member Id',
      'accountNameLabel': 'Member Name',
      'allowMultipleUsersPerObject': True,
      'id': '%s.%s' % (issuer_id, class_id),
      'issuerName': 'Baconrista',
      'kind': 'walletobjects#loyaltyClass',
      'locations': [{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.424015499999996,
          'longitude': -122.09259560000001
          },{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.424354,
          'longitude': -122.09508869999999
          },{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.7901435,
          'longitude': -122.39026709999997
          },{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 40.7406578,
          'longitude': -74.00208940000002
      }],
      'textModulesData': [{
        'header': 'Rewards details',
        'body': 'Welcome to Baconrista rewards.  For every 5 ' +
                'coffees purchased you\'ll receive a free '
                'bacon fat latte. '
      }],
      'linksModuleData': {
        'uris': [
          {
            'kind': 'walletobjects#uri',
            'uri': 'http://www.baconrista.com',
            'description': 'Baconrista'
          }]
      },
      'infoModuleData': {
        'hexFontColor': '#FF3300',
        'hexBackgroundColor': '#ABABAB'
      },
      'imageModulesData': [
        {
          'mainImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
              'kind': 'walletobjects#uri',
              'uri':  'http://farm8.staticflickr.com/7401/11177116434_d8e600bba6_o.jpg',
              'description': 'Coffee beans'
            }
          }
        }
      ],
      'messages': [{
          'actionUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://baconrista.com'
          },
          'header': 'Welcome to Banconrista Rewards!',
          'body': 'Featuring our new bacon donuts.',
          'image': {
              'kind': 'walletobjects#image',
              'sourceUri': {
                  'kind': 'walletobjects#uri',
                  'uri': 'http://farm8.staticflickr.com/7302/11177240353_115daa5729_o.jpg'
              }
          },
          'kind': 'walletobjects#walletObjectMessage'
      }],
      'programLogo': {
          'kind': 'walletobjects#image',
          'sourceUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://farm8.staticflickr.com/7340/11177041185_a61a7f2139_o.jpg'
          }
      },
      'programName': 'Baconrista Rewards',
      'renderSpecs': [{
          'templateFamily': '1.loyalty_list',
          'viewName': 'g_list'
          }, {
          'templateFamily': '1.loyalty_expanded',
          'viewName': 'g_expanded'
      }],
      'rewardsTier': 'Gold',
      'rewardsTierLabel': 'Tier',
      'reviewStatus': 'underReview',
      'version': '1'
  }
  return loyalty_class

def generate_loyalty_object(issuer_id, class_id, object_id):
  loyalty_object = {
      'accountId': '1234567890',
      'accountName': 'Jane Doe',
      'barcode': {
          'alternateText' : '12345',
          'label' : 'User Id',
          'type' : 'qrCode',
          'value' : '28343E3'
      },
      'classId' : '%s.%s' % (issuer_id, class_id),
      'id' : '%s.%s' % (issuer_id, object_id),
      'textModulesData': [{
        'header': 'Jane\'s Baconrista Rewards',
        'body': 'You are 5 coffees away from receiving a free ' +
                'bacon fat latte. '
      }],
      'linksModuleData': {
        'uris': [
          {
            'kind': 'walletobjects#uri',
            'uri': 'http://www.baconrista.com/myaccount?id=1234567890',
            'description': 'My Baconrista Account'
          }]
      },
      'infoModuleData': {
        'hexFontColor': '#FFFFFF',
        'hexBackgroundColor': '#FC058C',
        'labelValueRows': [{
            'hexFontColor': '#000000',
            'hexBackgroundColor': '#BBCCFC',
            'columns': [{
              'label': 'Member Name',
              'value': 'Jane Doe'
          }, {
            'label': 'Membership #',
            'value': '1234567890'
          }]
        }, {
            'hexFontColor': '#EDEDDD',
            'hexBackgroundColor': '#FFFB00',
            'columns': [{
              'label': 'Next Reward in',
              'value': '2 coffees'
            }, {
              'label': 'Member Since',
              'value': '01/15/2013'
            }]
        }],
        'showLastUpdateTime': 'true'
      },
      'messages': [{
          'actionUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://baconrista.com'
          },
          'header': 'Jane, welcome to Banconrista Rewards',
          'body': 'Thanks for joining our program. Show this message to ' +
                  'our barista for your first free coffee on us!',
          'image': {
              'kind': 'walletobjects#image',
              'sourceUri': {
                  'kind': 'walletobjects#uri',
                  'uri': 'http://farm4.staticflickr.com/3723/11177041115_6e6a3b6f49_o.jpg'
              }
          },
          'kind': 'walletobjects#walletObjectMessage'
      }],
      'loyaltyPoints': {
          'balance': {
              'string': '500'
          },
          'label': 'Points',
          'pointsType': 'points'
      },
      'state': 'active',
      'version': 1
  }
  return loyalty_object
