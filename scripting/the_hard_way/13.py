#Parameters, Unpacking, Variables
from sys import argv #With this line we make it possible to read arguments from the console line
#It looks like this: root@10.10.10.1 ~$ python index.py arg1 arg2 arg3
#The things you are importing are also know as modules(Python alternative to libraries)

#It is important to note that the arguments (argv) start from argv[0], which is considered the name of the script
#In our case argv[0] would be index.py

script, first, second, third = argv #here we manually set the 'expectation'
#With this line the script expects 4 variables - argv[0]-argv[3], respectively set: script, first, second, third
#This process is also known as Unpacking

print ("The script is called: ", script)
print ("your first variable is: ", first)
print ("your second variable is: ", second)
print ("your third variable is: ", third)
