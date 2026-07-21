class vehical:
    def __init__(self):
        self.door = None
        self.color = None
        self.body = None
        self.tyre = None


class car(vehical):
    def __init__(self):
        self.HP = None
        self.engin_cap = None
        self.spark = False
        self.gear = 0
        self.air_val = False
        self.fuel_injection = False
    def ignition(self):
        self.fuel_injection = True
        self.air_val = True
        self.spark = True

    def start(self):
        self.ignition()
    
    def getproperty(self,name:str):
        return super().__getattribute__(name)
    
    def getproperties(self,names:list):
        return [super().__getattribute__(attr) for attr in names]
    
    def setproperty(self,n:str,v):
        super().__setattr__(n,v)

    def setproperties(self, attr:dict):
        for k, v in attr.items():
            super().__setattr__(k,v)
    


car1 = car()

car1.setproperties({"color":"Silver","engin_cap":1000,'door':4})

print(car1.getproperties(['color','engin_cap','door']))