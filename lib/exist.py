from lib.mind.aware import Aware

def leave():
    from sys import exit
    exit()

def input_source():
    external = input('Input: ') # for sample data
    if external == 'stop':
        leave()
    return external

class Exist():
    
    ons = list()

    def __init__(self, introduced):
        self.alive = True
        self.aware = Aware(self)

        self.introduced = introduced

        self.source(input_source)

        from threading import Thread
        self.persisting = Thread(target=self.persist)
        self.persisting.start()

    def source(self, method): # asin to source something
        self.ons.append(method)

    def on(self):
        for source in self.ons:
            if callable(source):
                self.aware.of(source())
            else:
                print('provided source ' + str(source) + ' is not callable')
            
    def persist(self):
        while self.alive:
            self.on()
        leave()


