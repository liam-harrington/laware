#!/usr/bin/python3


from lib.introduce import Introduce

i = Introduce()

i.existence.aware.of("sample")

from lib.mind.injector import Injector
i.existence.sample = Injector(i.existence, i, [1, 1, 1])
