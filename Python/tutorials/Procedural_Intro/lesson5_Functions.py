### FUNCTIONS ###

#This program defines some functions, then calls those functions.

def sayHello():
    print("Hello World! I'm speaking from inside a function.")

def greaterThan(a, b):
    return (a > b)

sayHello()

var1 = input("Give me a number")
var2 = input("Give me another number")

if (greaterThan(var1, var2)):
    print(var1 + " is greater than " + var2)
else:
    print(var2 + " is greater than " + var1)
