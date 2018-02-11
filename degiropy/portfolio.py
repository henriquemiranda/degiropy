import requests
import json
from tabulate import tabulate
import pandas as pd
from .product import Product
from .field import Field

class Portfolio:
    def __init__(self,session,products):
        self.session = session
        self._products = products
        self.pandas = pd.DataFrame(self.portfolio)

    @staticmethod
    def from_url(session):
        params='portfolio=0'
        dict_url = {'tradingUrl':session.config.tradingUrl,
                    'account':session.accountid,
                    'sessionid':session.sessionid,
                    'params':params}
        funds_url = '{tradingUrl}v5/update/{account};jsessionid={sessionid}?{params}'.format(**dict_url)
        response = requests.get(funds_url)
        data = json.loads(response.text)

        #start parsing
        products = []
        field = Field.from_dict(data['portfolio'])
        for item in field.portfolio:
            product = Product.from_dict(item)
            products.append(product)

        return Portfolio(session,products)

    def get_product_by_ids(ids):
        session = self.session
        dict_url = {'productSearchUrl':session.config.productSearchUrl,
                    'account':session.accountid,
                    'sessionid':session.sessionid}
        product_url = '{productSearchUrl}v5/products/info?intAccount={account}&sessionId={sessionid}'.format(**dict_url)
        data = list(map(str,ids))
        response = requests.post(product_url, json=data)
        print(response.text)

    @property
    def portfolio(self):
        portfolio = []
        for product in self._products:
            portfolio.append(vars(product))
        return portfolio 

    def write_portfolio(self,filename='portfolio.json'):
        with open(filename,'w') as f:
            json.dump(self.portfolio,f)

    def __str__(self):
        return tabulate(self.pandas,headers='keys', tablefmt='psql')

