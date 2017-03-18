import config

def offer_class():
    offer = {
        'allowMultipleUsersPerObject': True,
        'heroImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': 'http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg'
            }

        },
        'id': config.ISSUER_ID + '.' + config.OFFER_CLASS_ID, 
	'imageModulesData': [{
	    'mainImage': {
		'kind': 'walletobjects#image',
		'sourceUri': {
		    'kind': 'walletobjects#uri',
		    'uri':  'http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg',
		    'description': 'Coffee beans'
		}
	    }
	}],
        'issuerName': 'Baconrista Coffee',
	'linksModuleData': {
	    'uris': [
		{
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
        'provider': 'Test Offer Provider',
        'redemptionChannel': 'both',
        'reviewStatus': 'underReview',
        'title': '20% off any T-shirt',
        'titleImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': 'https://lh3.googleusercontent.com/MGmuJePqkG8AiRWlPAHL1KAJV70jRhA66UQqCYboPugLB697JQoALjA0xgMtDkgoB9_QNKzdWPR1fJFCZGKOLbwSAK-WO6J3x30Km5fOJyT33qPcK5dbJqPj3k3FxTX9a0iOGpiI'
            }
        }
    }
    return offer

def offer_object():
    obj = {
	'barcode': {
	    'kind': 'walletobjects#barcode',
	    'type': 'upcA',
	    'value': '123456789012',
	    'label': 'Offer Code',
	    'alternateText': '12345'
	},
	'classId' : config.ISSUER_ID + '.' + config.OFFER_CLASS_ID,
	'id' : config.ISSUER_ID + '.' + config.OFFER_OBJECT_ID,
	'state': 'active',
	'version': 1
    }
    return obj
