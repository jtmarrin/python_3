#!/usr/bin/python3

class Calculator:
    def __init__(self, ina, inb):
        self.a = ina
        self.b = inb

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

newCalculation = Calculator(10, 20)
print ('a+b: %d' %newCalculation.add())
print ('a*b: %d' %newCalculation.mul())
