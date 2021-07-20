# 32nd Exercise from the book
# Loops and lists

# What is a list? 
# here is an example of a few lists
hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4, 5]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# The first kind of for-loop goes through a list
for number in the_count:
    print("This count is %d" % number)

# Same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# We can also go through mixed lists
# Notice that to print different variable types we need to use %r 
for i in change: 
    print("I have %r" % i)

# We can also dynamicall build lists
# To do that we must start with an emty one first
empty_list = []

# Then we use the reange function to caount from 0 to 5
for num in range (0, 6):
    print("We are adding %d to the empty list" % num)
    # Append the value to the list using the built in append method
    empty_list.append(num)

# Now we can print the new list to check if our operation was successful
for element in empty_list:
    print("This is an element from the generated empty list: %d" %element)
