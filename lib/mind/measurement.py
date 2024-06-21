class Measurement:

    def __init__(self, steps, interval):
        self.steps = steps
        self.interval = interval

        self.all = list()
        self.result = float()
        for step in range(0, steps):
            self.all.append(int())

        from threading import Thread
        self.measuring = Thread(target=self.measure)
        self.measuring.start()

    def switch(self):
        self.all.pop(0)
        self.all.append(int())

    def increase(self, amount):
        self.all[-1] += amount

    def calculate(self):
        total = int()
        for measurement in self.all:
            total += measurement
        self.result = total / self.steps

        return self.result

    def measure(self):
        from time import sleep
        while True:
            sleep(self.interval)
            self.switch()
