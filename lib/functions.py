def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, {}!".format(name))

def greet_with_default(name="programmer"):
    print("Hello, {}!".format(name))

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

greet_programmer()
greet("Manoti")
greet_with_default()
greet_with_default("Vanessa")
result = add(3, 5)
print("Sum:", result)
halved_value = halve(10)
print("Halved value:", halved_value)
