class Aware():
    def __init__(self, existence): # used by Exist class
        self.existence = existence
        
        from .measurement import Measurement
        self.occupation = Measurement(10, 10.0)

    def of(self, information):
        self.occupation.increase(1)
        #pass
