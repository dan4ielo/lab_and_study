# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from math import factorial as fac

def digit_sum (num):
    num = str(num)
    result = 0
    for i in num: 
        result += int(i)
    return result

print (digit_sum(fac(100)))
