import config

def loyalty_class():
    body = {
        'id': config.ISSUER_ID + '.' + config.LOYALTY_CLASS_ID, 
        'issuerName': config.ISSUER_NAME,
        'programLogo': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': config.LOYALTY_PROGRAM_LOGO
            }
        },
        'heroImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': config.LOYALTY_HERO_IMAGE
            }

        },
        'programName': config.LOYALTY_PROGRAM_NAME,
        'reviewStatus': 'underReview'
    }
    return body

def loyalty_object():
    obj = {
            'classId' : config.ISSUER_ID + '.' + config.LOYALTY_CLASS_ID,
            'id' : config.ISSUER_ID + '.' + config.LOYALTY_OBJECT_ID,
            'accountId': '1234567890',
            'accountName': 'Jane Doe',
            'state': 'active',
            'version': 1
    }

    return obj

