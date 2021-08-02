# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23

# Find the sum of all the multiples of 3 or 5 below 1000

def divisible(i):
    if i % 3 == 0:
        return i
    elif i % 5 == 0:
        return i
    else:
        return 0

LIMIT = 1 * 1000
result = 0

i = 0
while i < LIMIT: # from 0 to 1000 - NOTE the question asks for numbers below 1000 :/
    result = result + divisible(i)
    i += 1

print (result)
