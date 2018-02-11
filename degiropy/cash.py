import requests
import json
from tabulate import tabulate
import pandas as pd
from .config import Config
from .field import Field

class Cash():
    def __init__(self,session,cashFunds):
        self.session = session
        self.json = cashFunds
        self.pandas = pd.DataFrame(data=cashFunds)

    @staticmethod
    def from_url(session):
        """
        Get cash data from account

        Args:
            session: instance of the Session class
        """
        #data request
        dict_url = {'tradingUrl':session.config.tradingUrl,
                    'account':session.accountid,
                    'sessionid':session.sessionid,
                    'params':'cashFunds=0'}
        funds_url = '{tradingUrl}v5/update/{account};jsessionid={sessionid}?{params}'.format(**dict_url)
        response = requests.get(funds_url)
        data = json.loads(response.text)

        #start parsing
        cashFunds = []
        field = Field.from_dict(data['cashFunds'])
        for item in field.cashFunds:
            field = Field.from_dict(item)
            cashFund = {}
            for item in field.cashFund:
                field = Field.from_dict(item)
                cashFund.update(vars(field))
            cashFunds.append(cashFund)

        return Cash(session,cashFunds)
    
    def write_cash(self,filename='cash.json'):
        with open(filename,'w') as f:
            json.dump(self.json,f)
        
    def __str__(self):
        return tabulate(self.pandas,headers='keys', tablefmt='psql')
        
        
