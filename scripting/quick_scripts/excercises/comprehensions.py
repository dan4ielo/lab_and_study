from pprint import pprint
from math import sqrt
# List comprehention
words = [] # A list of words
sentence = "This is a sentance that is going to be used for demonstration"
words = sentence.split()
print (words)
words_len = [len(word) for word in words]
print (words_len)

# Set comprehention
words_len = {len(word) for word in words}
print (words_len)

# Dictionary comprehentions
country_to_capital = {
        'United Kingdom': 'London',
        'Brazil': 'Brassilia',
        'Morocco': 'Rabat',
        'Sweden': 'Stockholm',
    }

# a nice addition to dictionaries is to invert the dictionary so we
# can perform efficient lookups in the opposite direction

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pprint(capital_to_country)

# Filtering Comprehentions
def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primes = [_ for _ in range(50) if is_prime(_)]
print (primes)

prime_square_divisors = {x*x: (1, x, x*x) for x in range(10) if is_prime(x)}
pprint (prime_square_divisors)

#======================================================================================#
# Iteration Protocols

# Iterable - Can be passed to iter() to produce an iterator
# Iterator - Can be passed to next() to get the next value in the sequence

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print (next(iterator))

# Generators
# A generator is defined by the yield word in a function

def gen123():
    yield 1
    yield 2
    yield 3

g = gen123() # NOTE: g is a generator object, meaning that we can iterate over it
print (g)
print (next(g))
print (next(g))
print (next(g))

for v in gen123():
    print ('This comes from a for loop: {}'.format(v))

# Maintaining state in Generators
