import requests
import json
from .field import Field
from .currency import Currency

class Product:
    def __init__(self,json):
        for key in json:
            if 'lBase' in key:
                currency = Currency(json[key])
                setattr(self,key,currency)
            elif 'accruedInterest' in key:
                pass # at least for now
            else:
                setattr(self,key,json[key])

    @staticmethod
    def from_ids(session,ids):
        dict_url = {'productSearchUrl':session.config.productSearchUrl,
                    'account':session.accountid,
                    'sessionid':session.sessionid}
        product_url = '{productSearchUrl}v5/products/info?intAccount={account}&sessionId={sessionid}'.format(**dict_url)
        data = list(map(str,ids))
        response = requests.post(product_url, json=data)
        data = json.loads(response.text)['data']

        #start processing
        products = {}
        for key in data:
            product = Product(data[key])
            products[key] = product
        return products

    def items(self):
        return vars(self).items()

    @staticmethod
    def from_dict(json):
        product = {}
        field = Field.from_dict(json)
        for item in field.positionrow:
            field = Field.from_dict(item)
            product.update(vars(field))
        return Product(product)

    def __str__(self):
        return str(vars(self))
