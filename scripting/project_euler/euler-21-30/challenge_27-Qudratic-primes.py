# Euler discovered the remarkable quadratic formula:
#
#            n**2 + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 30.
# However, when n = 40, 40**2 + 40 + 41  is divisible by 41, and certainly when n = 41 is clearly divisible by 41.
# 
# The incredible formula n**2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values
# 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
#       n**2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of 
# primes for consecutive values of n, starting with n = 0.

def is_prime(num):
    if num == 2: return True
    if num % 2 == 0: return False
    denom = 3
    while denom <= num / 2:
        if num % denom == 0: return False
        denom += 2
    return True

def main():
    a_gen = (_ for _ in range(-999, 999))
    b_gen = (_ for _ in range(-1000, 1000))
    long_a = 0
    long_b = 0
    longest = 0
    for a in a_gen:
        for b in b_gen:
            consecutive_ns = formula_test(a, b)
            if consecutive_ns > longest:
                long_a = a
                long_b = b
                longest = consecutive_ns
    return long_a * long_b

def formula_test(a, b):
    up_limit = 1000
    gen = (_ for _ in range(up_limit))
    count = 0
    old = 0
    for n in gen: 
        res = n**2 + a*n + b
        if is_prime(res) and n == old + 1: 
            count += 1
        else:
            return count
        old = n

print(main())

