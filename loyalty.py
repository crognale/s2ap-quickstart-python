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

def generate_loyalty_class(issuer_id, class_id):
  loyalty_class = {
      'accountIdLabel': 'Member Id',
      'accountNameLabel': 'Member Name',
      'allowMultipleUsersPerObject': True,
      'homepageUri': {
          'kind': 'walletobjects#uri',
          'uri': 'https://www.example.com'
       },
      'id': '%s.%s' % (issuer_id, class_id),
      'issuerData': {
          'g_expanded': {
              'textModule': {
                  'header': {
                      'string': 'Rewards details'
                  },
                  'body': {
                      'string': 'Welcome to Baconrista rewards. For every 5 ' +
                                'coffees purchased you\'ll receive a free ' +
                                'bacon fat latte. '
                  }
              },
              'linksModule': {
                  'uri0': {
                      'uri': {
                          'kind': 'walletobjects#uri',
                          'uri': 'http://www.example.com',
                          'description': 'Example'
                      }
                  }
              },
              'infoModule': {
                  'fontColor': {
                      'string': '#FF3300'
                  },
                  'backgroundColor': {
                      'string': '#ABABAB'
                  },
                  'row0': {
                      'col0': {
                          'label': {
                              'string': 'Label 0'
                          },
                          'value': {
                              'string': 'Value 0'
                          }
                      },
                      'col1': {
                          'label': {
                              'string': 'Label 1'
                          },
                          'value': {
                              'string': 'Value1'
                          }
                      }
                  },
                  'row1': {
                      'col0': {
                          'label': {
                              'string': 'Label 0'
                          },
                          'value': {
                              'string': 'Value 0'
                          }
                      },
                      'col1': {
                          'label': {
                              'string': 'Label 1'
                          },
                          'value': {
                              'string': 'Value1'
                          }
                      }
                  }
              }
          }
      },
      'issuerName': 'Baconrista',
      'kind': 'walletobjects#loyaltyClass',
      'locations': [{
          'kind': 'walletobjects#latLongPoint',
          'latitude': 37.422601,
          'longitude': -122.085286
      }],
      'messages': [{
          'actionUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://baconrista.com'
          },
          'body': 'Welcome to Baconrista Rewards!',
          'header': 'Welcome',
          'image': {
              'kind': 'walletobjects#image',
              'sourceUri': {
                  'kind': 'walletobjects#uri',
                  'uri': 'http://ssl.gstatic.com/codesite/ph/images/search-48.png'
              }
          },
          'kind': 'walletobjects#walletObjectMessage'
      }],
      'programLogo': {
          'kind': 'walletobjects#image',
          'sourceUri': {
              'kind': 'walletobjects#uri',
              'uri': 'http://www.google.com/images/icons/product/drive-128.png'
          }
      },
      'programName': 'Baconrista Rewards',
      'renderSpecs': [{
          'templateFamily': '1.loyaltyCard1_list',
          'viewName': 'g_list'
          }, {
          'templateFamily': '1.loyaltyCard1_expanded',
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
      'accountName': 'Joe Smith',
      'barcode': {
          'alternateText' : '12345',
          'label' : 'User Id',
          'type' : 'qrCode',
          'value' : '28343E3'
      },
      'classId' : '%s.%s' % (issuer_id, class_id),
      'id' : '%s.%s' % (issuer_id, object_id),
      'issuerData': {
          'g_expanded': {
              'infoModule': {
                  'row0': {
                      'col0': {
                          'label': {
                              'string': 'Member Name'
                          },
                          'value': {
                              'string': 'Jane Doe'
                          }
                      },
                      'col1': {
                          'label': {
                              'string': 'Next Reward In'
                          },
                          'value': {
                              'int': 2
                          }
                      }
                  }
              }
          }
      },
      'loyaltyPoints': {
          'balance': {
              'string': '500'
          },
          'label': 'Points',
          'pointsType': 'rewards'
      },
      'state': 'active',
      'version': 1
  }
  return loyalty_object