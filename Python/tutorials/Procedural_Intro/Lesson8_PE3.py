from lesson6_PRIMES import isPrime
from lesson7_FACTOR import isFactor

num = 600851475143
toCheck = int(num / 2) + 1
largest = 0

while (largest == 0):
    for i in range(2, toCheck):
        while isFactor(i, num):
            num /= i
            print(str(num) + " is a factor.")
            if isPrime(num):
                largest = num
        if i > num:
            break
print(largest)