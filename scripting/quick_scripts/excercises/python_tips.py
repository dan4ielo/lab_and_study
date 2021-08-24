import sys
from collections import Counter
# Iteration with enumerate() instead of range()
data = [1, 2, -4, -6]
# Example: change all negative values to 0
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print (data)

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print (data)
print ("\n" + "="*25 + "\n")

# Sort using the build in sorted function

data = [3, 5, 1, 10, 9]
sorted_data = sorted(data)
print (sorted_data)

data = (3, 5, 1, 10, 9) # NOTE: We are using a tuple here, but the result will be a list
sort_reversed = sorted(data, reverse = True)
print (sort_reversed)

# Sort a complex data set - list of dict
ls = [  {'name': 'Max', 'age': 6},
        {'name': 'Lisa', 'age': 20},
        {'name': 'Ben', 'age': 9},
]
sort_dics = sorted(ls, key=lambda x: x['age'])
print (sort_dics)
print ("\n" + "="*25 + "\n")

# Store unique values with sets
this_list = [1,1,1,1,2,3,4,5,6,7,7,7,7,8]
print (this_list)
new_set = set(this_list)
print (new_set)
print ("\n" + "="*25 + "\n")

# Save memory with generators
new_list = [i for i in range(12000)]
print (sum(new_list))
print (sys.getsizeof(new_list), 'bytes')

new_gen = (i for i in range(12000))
print (sum(new_gen))
print (sys.getsizeof(new_gen), 'bytes')

print ("\n" + "="*25 + "\n")

# Define default values in dicts with get() and setdefault()

my_dict = {'item': 'football', 'price': 10.00}
#count = my_dict['count']
#print (count) # Gives back a Key error 
# A better method is to use the .get method
count = my_dict.get('count', 'default value')
print (count) # Returns None when nothing is found or the specified default value

count = my_dict.setdefault('count', 0)
print (count)
print (my_dict)
print ("\n" + "="*25 + "\n")

# Count hashable objects with collections.Counter
my_list = [10,10,10,10,10,10,5,5,2,9,9,9,9,9]
counter = Counter(my_list)
print (counter)
print (counter.most_common(1))
print ("\n" + "="*25 + "\n")

# Concatenate strings with .join

list_of_strings = ['My', 'name', 'Jeff']
# Very BAD!!!
new_string = ""
for word in list_of_strings:
    new_string += word + " "
print (new_string)

# Way faster for big strings
new_string = ' '.join(list_of_strings)
print (new_string)
print ("\n" + "="*25 + "\n")

# Merge dictionaries with **d syntax
d1 = {'name': 'Alex', 'age': 32}
d2 = {'name': 'Alex', 'city': 'NY'}
merged_dict = {**d1, **d2}
print (merged_dict)
print ("\n" + "="*25 + "\n")


