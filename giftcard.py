import config
import datetime

def giftcard_class():
    giftcard = {
	'allowMultipleUsersPerObject': True,
        'kind': 'walletobjects#giftCardClass',
        'id': config.ISSUER_ID + '.' + config.GIFTCARD_CLASS_ID, 
        'issuerName': 'Baconrista',
        'merchantName': 'Baconrista',
        'heroImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': 'http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg'
            }

        },
	'linksModuleData': {
	    'uris': [{
		'kind': 'walletobjects#uri',
		'uri': 'http://www.baconrista.com',
		'description': 'Baconrista'
	    }]
	},
	'locations': [{
	    'kind': 'walletobjects#latLongPoint',
	    'latitude': 37.422601,
	    'longitude': -122.085286
	}],
        'programLogo': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': 'https://lh3.googleusercontent.com/MGmuJePqkG8AiRWlPAHL1KAJV70jRhA66UQqCYboPugLB697JQoALjA0xgMtDkgoB9_QNKzdWPR1fJFCZGKOLbwSAK-WO6J3x30Km5fOJyT33qPcK5dbJqPj3k3FxTX9a0iOGpiI'
            }
        },
        'reviewStatus': 'underReview',
	'textModulesData': [{
	    'header': 'Where to Redeem',
	    'body': 'All US gift cards are redeemable in any US and Puerto Rico' +
		' Baconrista retail locations, or online at Baconrista.com where' + 
		' available, for merchandise or services.'
	}]
    }
    return giftcard


def giftcard_object():
    obj = {
            'balance': {
                'currencyCode': 'USD',
                'kind': 'walletobjects#money',
                'micros': 10000000
            },
            'balanceUpdateTime' : {
                'date': datetime.datetime.utcnow().isoformat('T') + 'Z'
            },
            'barcode': {
                'alternateText': '12345',
                'label': 'Gift Card Id',
                'type': 'qrCode',
                'value': '28343E3'
            },
            'cardNumber': '123456789',
            'classId' : config.ISSUER_ID + '.' + config.GIFTCARD_CLASS_ID,
            'eventNumber': '123456',
            'id' : config.ISSUER_ID + '.' + config.GIFTCARD_OBJECT_ID,
            'pin': '1111',
            'state': 'active',
            'version': 1
    }
    return obj
