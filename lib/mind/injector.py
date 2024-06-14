class Injector:
    def __init__(self, existence, information, interval):
        self.existence = existence
        self.information = information
        self.interval = interval

        from threading import Thread
        self.injecting = Thread(target=self.inject)
        self.injecting.start()

    def inject(self):
        from time import sleep
        for duration in self.interval:
            self.existence.aware.of(self.information)
            sleep(duration)

