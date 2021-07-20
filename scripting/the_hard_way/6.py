#In this excersize the focus will be on complex strings and text and how to manupulate it

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print (x) #Prints out the string contained in the x variable
print (y) #Prints out the string contained in the y variable
print ("I said %r." %x) #Here we replace the %r with the variable specified afterwards. The %r means that it going to be raplaced regardles of the type (integer, string, boolean etc.)
print ("I also said: %s" %y) #The replaced %s means that we are replacing the spot with a string value that is specified after the print statement

hilarious = False #It is important to know that to initiate a boolean variable the value must be specified with a capitalisation (True/False rather than true/flase)
joke_evaluation = "Isn't that funny?!? %r" # similarly to line 10 we have a section where we are going to be replacing the value with any variable, but since it is not the print statement we can conclude that this is going to be done at a later stage

print (joke_evaluation %hilarious) #We have reached the later stage we spoke about in line 14. Here we replace the %r value with the Boolean variable we created

w = "This is the left side of... "#Just a string
e = "a string with a right side."#Just a string

print (w + e) #This is one was we can append to strigs together
