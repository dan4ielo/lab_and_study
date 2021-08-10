# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
                                                # a**2 + b**2 = c**2
# Example: 3**2 + 4**2 = 5**2

# There exists exactly one Pythogorean triplet for which a + b + c = 1000
# Find the product of a, b, c

# c**2 = x + y ,where sqrt(x) and sqrt(y) are N
# How many pairs like that up to c = 1000?
c = 100
groups = []
while c < 1000:
    for a in range(1, c+1):
        big = c**2 - a**2
        sqrt = big**0.5
        if sqrt.is_integer() and big != 0:
            if a < int(sqrt):
                group = (a, int(sqrt), c)
                groups.append(group)
    c += 1

for group in groups: 
    RESULT = 1000
    current = 0
    i = 0
    while i < 3:
        current = current + group[i]
        i += 1
    if current == RESULT:
        answer = group

# print (groups)
print (answer)

product = 1
for num in list(answer):
    product = product * num

print (product)
