###GET Input and IF STATEMENTS###

#This program gets input from the user, and tests the input

variable = input("Give me a number please!")

if variable.isnumeric():
    if (variable == "5"):
        print("I don't like that number.")
    else:
        print(variable + " is a good number.")
else:
    print("That's not a number!")

print()

#separate demo

variable = ""
while (variable != "password"):
    variable=input("What's the password?")
