# This script does the same as exercise 17, but as a oneliner 
from sys import argv
open(argv[2], "w").write((open(argv[1])).read())

# Success!!!

# Explaining open(argv[2], "w").write((open(argv[1])).read())

# first step is to open the files
# open(argv[2],"w") = a 
# open(argv[1]) = b

# The expresion becomes:
# a.write(b.read())

# The new expression uses the read date from file b (the first input)
# to write into file a
# In excersize 17 this is done using the indata variable 