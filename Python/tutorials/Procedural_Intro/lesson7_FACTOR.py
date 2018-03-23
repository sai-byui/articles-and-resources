### FACTOR ###

#This program asks the user for two numbers,
#and then tells the user if the first number
#is a factor of the second

#Functions like this should never exist because they are so short!
#The exception is if the function name makes it very much clearer what it does

def isFactor(factor, number):
    return (number % factor == 0)

#factor = input("What is the first number?")
#number = input("What is the second number?")
#print(isFactor(int(factor), int(number)))