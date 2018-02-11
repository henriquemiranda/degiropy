import requests
import json

class Config():
    """
    Manage all the urls of the degiro platform
    """
    base_trader_url = 'https://trader.degiro.nl'
    login_url = 'https://trader.degiro.nl/login/secure/login'
    config_url = 'https://trader.degiro.nl/login/secure/config'

    def __init__(self,urls):
        for key in urls:
            setattr(self,key, urls[key])

    @staticmethod
    def from_url(sessionid):
        config_url = '{}'.format(Config.config_url)
        headers = { 'Cookie': 'JSESSIONID={};'.format(sessionid)}
        response = requests.get(config_url, headers=headers)
        urls = json.loads(response.text)
        return Config(urls)

    def __str__(self):
        s=""
        for item in vars(self):
            s+="{:<25} : {:<25}\n".format(item,getattr(self,item))
        return s
