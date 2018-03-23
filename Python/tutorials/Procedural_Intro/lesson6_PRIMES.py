### PRIMES ###

#This program asks the user for a number,
#and then tells the user if that number is prime

def isPrime(num):
    if (num <= 1):
        return False
    elif (num == 2):
        return True

    for i in range(3, int(num / 2) + 1):
        if (num % i == 0):
            return False
    return True

#number = input("What number would you like to test? ")
#if (isPrime(int(number))):
#    print(number + " is prime.")
#else:
#    print(number + " is not prime.")
