# This is a recapping excersize

print ("Let's practice everything now")
print ("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs\n")

poem = '''
\tThe lovely world
\twith logic so firmly planted
\tcannot discern \nthe needs of love
\tnor comprehend passion from intuition
\tand requires an explanation
\n\t\twhere there none.
'''

print("-----------------")
print(poem)
print("-----------------\n")

five = 10 - 2 + 3 - 6
print("This should be five %d" %(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("The starting point is: %d" %(start_point))
print("We'd have %d beans, %d jars and %d crates\n" %(beans, jars, crates))

new_statr_point = start_point / 10
print("We can also do it this way with a new starting point:")
print("We'd have %d beans, %d jars and %d crates" %(secret_formula(new_statr_point)))