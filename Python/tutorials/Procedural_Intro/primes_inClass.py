#This is the function that we all created together on 1/24/18


def isPrime(num):
    for i in range(2, int(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True

numToTest = input ("Give me a number:")
print(isPrime(int(numToTest)))