# Here we use the ability of python to safe the results of a function withing a variable
def add (a, b):
    c = a + b
    return c

def subtr (a, b):
    c = a - b
    return c

def multiply (a, b):
    c = a * b
    return c

def divide (a, b):
    c = a/b
    return c

age = add(12, 19)
height = subtr(178, 4)
weight = multiply(8, 10)
iq = divide(500, 2.5)

print("Age: %d \nHeight: %d\nWeight= %d \nIQ: %d" %(age, height, weight, iq))

print("And here is the result of the puzzle:")
what = add(age, subtr(height, multiply(weight, divide(iq, 2))))
print (what)