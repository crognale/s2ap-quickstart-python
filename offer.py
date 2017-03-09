import config

def offer_class():
    body = {
        'id': config.ISSUER_ID + '.' + config.OFFER_CLASS_ID, 
        'issuerName': config.ISSUER_NAME,
        'provider': config.OFFER_PROVIDER,
        'titleImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': config.OFFER_TITLE_IMAGE
            }
        },
        'heroImage': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': config.LOYALTY_HERO_IMAGE
            }

        },
        'redemptionChannel': 'both',
        'title': config.OFFER_TITLE,
        'reviewStatus': 'underReview'
    }
    return body

def offer_object():
    obj = {
            'classId' : config.ISSUER_ID + '.' + config.OFFER_CLASS_ID,
            'id' : config.ISSUER_ID + '.' + config.OFFER_OBJECT_ID,
            'state': 'active',
            'version': 1
    }

    return obj
