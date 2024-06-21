#!/usr/bin/python3


from lib.introduce import Introduce

i = Introduce()

person2 = Introduce()

i.existence.aware.of("sample")

from lib.mind.injector import Injector
i.existence.sample = Injector(i.existence, person2, [1, 1, 1])
