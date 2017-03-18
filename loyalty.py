import config

def loyalty_class():
    loyalty = {
        'accountIdLabel': 'Member Id',
        'accountNameLabel': 'Member Name',
        'heroImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': 'http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg'
            }
        },
        'hexBackgroundColor': '#5dba67',
        'id': config.ISSUER_ID + '.' + config.LOYALTY_CLASS_ID, 
	'infoModuleData': {
	    'hexFontColor': '#F8EDC1',
	    'hexBackgroundColor': '#442905'
	},
        'issuerName': 'Test Issuer',
        'kind': 'walletobjects#loyaltyClass',
        'linksModuleData': {
            'uris': [{
                    'kind': 'walletobjects#uri',
                    'uri': 'http://maps.google.com/?q=google',
                    'description': 'Nearby Locations'
                    },{
                        'kind': 'walletobjects#uri',
                        'uri': 'tel:6505555555',
                        'description': 'Call Customer Service'
                    }]
        },
        'locations': [{
            'kind': 'walletobjects#latLongPoint',
            'latitude': 37.424015499999996,
            'longitude': -122.09259560000001
        }],
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
        'reviewStatus': 'underReview',
        'rewardsTier': 'Gold',
        'rewardsTierlabel': 'Tier',
        'textModulesData': [{
            'header': 'Rewards details',
            'body': 'Welcome to Baconrista rewards. Enjoy your rewards for beyng a loyal customer. ' + 
                '10 points for every dollar spent. Redeem your points for free coffee, bacon and more!'
        }]
    }
    return loyalty

def loyalty_object():
    obj = {
            'accountId': '1234567890',
            'accountName': 'Jane Doe',
            'barcode': {
                'alternateText': '12345',
                'label' : 'User Id',
                'type': 'qrCode',
                'value' : '28343E3'
            },
            'classId' : config.ISSUER_ID + '.' + config.LOYALTY_CLASS_ID,
            'id' : config.ISSUER_ID + '.' + config.LOYALTY_OBJECT_ID,
	    'infoModuleData': {
		'hexFontColor': '#F8EDC1',
		'hexBackgroundColor': '#442905',
		'labelValueRows': [{
			'hexFontColor': '#F8EDC1',
			'hexBackgroundColor': '#922635',
			'columns': [{
			'label': 'Next Reward in',
			'value': '2 coffees'
		    }, {
			'label': 'Member Since',
			'value': '01/15/2013'
		    }]
		},{
		    'hexFontColor': '#F8EDC1',
		    'hexBackgroundColor': '#922635',
		    'columns': [{
			'label': 'Local Store',
			'value': 'Mountain View'
		    }]
		}],
		'showLastUpdateTime': 'true'
	    },
	    'linksModuleData': {
		'uris': [{
		    'kind': 'walletobjects#uri',
		    'uri': 'http://www.baconrista.com/myaccount?id=1234567890',
		    'description': 'My Baconrista Account'
		}]
	    },
	    'loyaltyPoints': {
		'balance': {
		    'string': '500'
		},
		'label': 'Points',
		'pointsType': 'points'
	    },
            'secondaryLoyaltyPoints': {
                'balance': {
                    'string': '20'
                },
                'label': 'Secondary Pionts',
                'pointsType': 'points'
            },
            'state': 'active',
            'version': 1
    }
    return obj

