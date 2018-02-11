
class Currency(dict):
    def __init__(self,json):
        dict.__init__(self,**json)
        for key in json:
            setattr(self,key,json[key])

    def __str__(self):
        return str(self.EUR)
