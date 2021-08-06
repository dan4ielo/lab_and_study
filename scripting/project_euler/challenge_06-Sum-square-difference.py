# The sum of the squares of the first 10 natural numbers is 385
# and the square of the sum of the first 10 natural numbers is 55^2 = 3025
# This means the difference between the sum of the squares and the square
# of the sum is 3025-385 = 2640.

# Find the same number but for the first 100 natural numbers

natural = [n for n in range(101)]
square_of_the_sum = sum(natural)**2
sum_of_the_square = sum([n**2 for n in natural])
result = square_of_the_sum - sum_of_the_square
print(result)

# One-liner
print(sum([n for n in range(101)])**2 - sum([n**2 for n in range(101)]))
