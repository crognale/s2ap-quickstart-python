import config

def giftcard_class():
    body = {
        'id': config.ISSUER_ID + '.' + config.GIFTCARD_CLASS_ID, 
        'issuerName': config.ISSUER_NAME,
        'merchantName': config.GIFTCARD_MERCHANT_NAME,
        'programLogo': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': config.GIFTCARD_PROGRAM_LOGO
            }
        },
        'heroImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': config.GIFTCARD_HERO_IMAGE
            }

        },
        'reviewStatus': 'underReview'
    }
    return body


def giftcard_object():
    obj = {
            'classId' : config.ISSUER_ID + '.' + config.GIFTCARD_CLASS_ID,
            'id' : config.ISSUER_ID + '.' + config.GIFTCARD_OBJECT_ID,
            'cardNumber': config.GIFTCARD_OBJECT_CARDNUMBER,
            'balance': {
                'currencyCode': 'USD',
                'kind': 'walletobjects#money',
                'micros': config.GIFTCARD_OBJECT_BALANCE
            },
            'state': 'active',
            'version': 1
    }
    return obj
