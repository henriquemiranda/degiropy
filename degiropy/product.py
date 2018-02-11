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
    def from_dict(json):
        product = {}
        field = Field.from_dict(json)
        for item in field.positionrow:
            field = Field.from_dict(item)
            product.update(vars(field))
        return Product(product)

    def __str__(self):
        return str(self.json)
