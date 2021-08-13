# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def factors(n):
    factors = [1,]
    factor = 2
    while factor < n:
        if n % factor == 0:
            factors.append(factor)
        factor += 1
    return factors

def d(n):
    return sum(factors(n))

def amicable_pair(a, b):
    if a == b:
        return False
    # if a == 0 or b == 0:
        # return False
    if d(b) == a: # d(a) == b and d(b) == a It should be like that, but we can skip a calculation
        return True
    return False
'''
LIMIT = 10 * 1000
a = 1
b = 1
pairs = []
while a <= LIMIT:
    b = d(a)
    if amicable_pair(a, b):
        pairs.append((a, b))
    a += 1
'''
print (factors(12))
print (d(12))

#print (pairs)

# forgot to calculate the sum :/
pairs = [(220, 284), (284, 220), (1184, 1210), (1210, 1184), (2620, 2924), (2924, 2620), (5020, 5564), (5564, 5020), (6232, 6368), (6368, 6232)]
nums = []

for i in range(len(pairs)):
    for n in pairs[i]:
        nums.append(n)

nums = list(set(nums))

print (sum(nums))

