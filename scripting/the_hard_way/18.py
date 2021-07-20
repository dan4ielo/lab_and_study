# Excercise 18 is all about functions. in Python you define functions with Def

# This is a function that prints its own arguments
def print_arguments(arg1, arg2):
    print("The value of arg1 is: %s \n And the arg2 value is: %r" %(arg1, arg2))

# Now a function that takes only one argument
def print_one_argument(arg1):
    print("The value of arg1 is: %r" %(arg1))

# And now a function without arguments
def print_no_arguments():
    print("Well, I am empty :D")

print_arguments("Argument one", "Argument two")

print_one_argument("This is the argument")

print_no_arguments()