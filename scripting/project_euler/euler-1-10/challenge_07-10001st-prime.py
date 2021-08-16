# A quick update. If you use the formula f(n) = n*log(n) you will be able to reach the nth prime
# really quickly. The idea is that graphically, f(n) is really close to the distribution of primes

# check: https://stemhash.com/how-to-find-the-nth-prime-number/
# watch: https://www.youtube.com/watch?v=hYxBH1YY9z4  -  min 20:00

# By listing the first six primes: 2, 3, 5, 7, 11 and 13, we ca see that the 6h prime is 13.
# What is the 10 001st prime?

from math import sqrt

def smallest_divisors(n):
    if n % 2 == 0:
        return 2
    small = 3
    while small <= sqrt(n):      # small < N/small -> small*small < N -> small < sqrt(N)
        if small * int(n/small) == n:
            return small
        small += 2
    return n

def nth_prime(k):
    # k is an index for the number of the prime wanted - 10 001 in our case

    prime = 2
    i = 0
    num = 2 # smallest prime - k = 1
    while i < k:
    # increment only when a prime is found
        if smallest_divisors(num) == num:
            prime = num
            i += 1
            num += 1
        else:
            num += 1
    return prime

print (nth_prime(6))
print (nth_prime(100))
print (nth_prime(1000))
print (nth_prime(10001))

