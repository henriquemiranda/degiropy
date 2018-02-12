from copy import deepcopy

class Currency(dict):
    def __init__(self,json):
        dict.__init__(self,**json)
        for key in json:
            setattr(self,key,json[key])

    def __add__(self,other):
        new = deepcopy(self)
        new.EUR += other
        return new

    def __str__(self):
        return str(self.EUR)
