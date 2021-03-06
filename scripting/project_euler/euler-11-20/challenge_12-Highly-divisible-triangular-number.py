# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be: 1+2+3+...+7 = 28. The first then would be:
                    # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28

# We can see that 28 is the first triangle number to have over five divisors

# What is the value of the first triangle number to have over five hundred divisors?
from timeit import default_timer as timer

LIMIT = 1 * 1000 # * 1000
ignore = 1 # * 1000 * 1000
def gen_tri_num():
    '''genrate triangle numbers'''
    tri_num = 0
    naturals = [num for num in range(LIMIT)]
    index = 0
    while index < len(naturals):
        num = naturals[index]
        index += 1
        tri_num = tri_num + num
        yield tri_num

def factors(num):
    factors = [1, ]
    even_factors = []
    uneven_factors = []
    n = num
    if num == 0:return []
    if num == 1:return factors
    even_power = 1
    while num % 2 == 0:
        num = int(num / 2)
        factors.append(2**even_power)
        even_factors.append(2**even_power)
        even_power += 1
    uneven_factor = 3
    while uneven_factor <= n:
        if uneven_factor * int(n/uneven_factor) == n:
            factors.append(uneven_factor)
            uneven_factors.append(uneven_factor)
        uneven_factor += 2
    for even in even_factors:
        for uneven in uneven_factors:
            factors.append(even * uneven)
    return factors

gen = gen_tri_num()
tri_num = next(gen)
start = timer()
#while len(factors(tri_num)) < 100:
#    tri_num = next(gen)
#end = timer()

#print(str(tri_num)+': '+str(len(factors(tri_num))) ) # + ' -> factors: ' + str(factors(tri_num)))
#print (end - start)

#=============== This is not fast enough =====================#
# O(n) ~ n^2 -> Probably less, but definetly far from O(n) = n
# This is extremely slow
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num <= 1: continue
        if num % i == 0:
            factors.append(i)
    return factors

#i = 0
#tri = gen_tri_num()
#while i <= 7:
#    value = next(tri)
#    print(str(value)+': '+str(get_factors(value)))
#    i += 1

gen = gen_tri_num()
tri_num = next(gen)
start = timer()
while len(get_factors(tri_num)) < 100:
    tri_num = next(gen)
end = timer()

print(str(tri_num)+': '+str(len(get_factors(tri_num))) ) # + ' -> factors: ' + str(get_factors(tri_num)))
print (end - start)

# A faster way would be to check by which promes is the num divisible
# and then calculate the number of divisors based on combinatorics

#================= Pfffffff, this is even slower :/ ===============#
# O(n) ~ log(n) -> for the prime factorization
# O(n) ~ n^n -- xD - this should be a thing right? -> basically for each n we call a lot of combinations need to be checked

from math import sqrt
from itertools import combinations

def the_prime_way(num):
    '''Gives all prime factors plus all factors that a power of 2'''
    factors = [1, ]
    n = num
    if num == 0:return []
    if num == 1:return factors
    even_power = 1
    while num % 2 == 0:
        num = int(num / 2)
        factors.append(2**even_power)
        even_power += 1
    small = 3
    while small <= num:
        if small * int(num/small) == num:
            factors.append(small)
        small += 2
    factors.append(n)
    return factors

def combination(_list):
    number_of_combinations = 0
    for i in range(2, len(_list)):
        comb = combinations(_list, i)
        # print (list(comb)) # Gives back a list of tuples
        for combination in list(comb): # get a tuple
            result = 1
            combination = list(combination)
            for el in combination: # Iterate over the list from tuple
                result = el * result
            if result not in _list and _list[-1] % result == 0 and _list[-1] != result:
                _list.append(result)
                _list.sort()
    _list = list(set(_list))
    _list.sort()
#    print (_list)
    return len(_list)

#i = 0
#tri = gen_tri_num()
#while i <= 7:
#    value = next(tri)
#    print(str(value)+': '+str(get_factors(value)))
#    i += 1
gen = gen_tri_num()
value = next(gen)

# print (the_prime_way(28))
# print (combination(the_prime_way(28)))
# print (value)

#while combination(the_prime_way(value)) < 100:
#    value = next(gen)
#    combinations = combination(the_prime_way(value))
#print (str(value) + ': ' + str(combination(the_prime_way(value))))# + str(factors) + str(len_factors))






