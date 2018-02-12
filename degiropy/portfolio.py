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
        print('get product names')
        self.get_product_names()
        print('done')       
 
        #create pandas dataframe
        print('pandas shit')
        pandas = pd.DataFrame(self.portfolio)
        pandas = pandas.assign(profit=(pandas.plBase + pandas.value))
        pandas = pandas.assign(todayProfit=(pandas.todayPlBase + pandas.value))

        print('done')
        self.pandas = pandas

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

    def get_product_names(self):
        session = self.session
        ids = self.ids
        product_names = Product.from_ids(session,ids)
 
        for product in self._products:
            id = product.id
            product_name = product_names[str(id)]
            for key,item in product_name.items():
                setattr(product, key, item)

    @property
    def ids(self):
        ids = []
        for product in self._products:
            ids.append(product.id)
        return ids
        
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
        return tabulate(self.pandas[['name','price','currency','size','closePrice','value','profit','todayProfit']],headers='keys', tablefmt='psql')


