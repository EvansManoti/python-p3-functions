#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello Manoti!")

greet_programmer

def greet(name):
    pass
    print("Hello {}".format(name))

    greet("Manoti")

def greet_with_default(name="programmer"):
    pass
    print("Hello {}".format(name))

    greet_with_default()

def add(num1, num2):
    pass
    return(num1*num2)

result = add(12, 888)
print("sum:", result)

def halve(number):
    pass
    number // 4

result =halve(2)
print("Half:" ,result)