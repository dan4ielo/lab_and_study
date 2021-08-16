# Backup of Challenge 3

from math import sqrt

primes = [2, ]  # We start from the first prime - 2

def is_prime(num):
    for prime in primes:
        if num % prime == 0 and prime != 1:
            return False
        else:
            continue
    if num > 1:
        primes.append(num)
    return True

def prime_factors_of(number):
    LIMIT = int(sqrt(number) // 1)
    primes = [num for num in range(2, LIMIT) 
        if is_prime(num) and number % num == 0]
    # primes = [num for num in range(number) if is_prime(num) and number % num == 0 and num != 1]
    return primes

def is_prime(num):
    # invariant


print (prime_factors_of(13195))
# print (prime_factors_of(600851475143))
# Need help with the optimization of the program. It works for
# small numbers, but the one given is too big

