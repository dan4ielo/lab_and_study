# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below 2 mil
from math import sqrt

LIMIT = 2 * 1000 * 1000 # 2 Million

def smallest_divisors(n):
    if n % 2 == 0:
        return 2
    small = 3
    while small <= sqrt(n):      # small < N/small -> small*small < N -> small < sqrt(N)
        if small * int(n/small) == n:
            return small
        small += 2
    return n

def sum_of_primes_below(limit):
    # k is an index for the number of the prime wanted - 10 001 in our case
    result = 2 # start from the smallest prime
    num = 3 # This is so we can iterate faster
    while num < limit:
    # increment only when a prime is found
        if smallest_divisors(num) == num:
            result = result + num
            num += 2
        else:
            num += 2
    return result

print (sum_of_primes_below(LIMIT))

