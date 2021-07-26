#More printing !!! Yay...

formatter = "%r %r %r %r"

print (formatter %(1, 2, 3, 4))
print (formatter %("one", "two", "three", "four"))
print (formatter %(True, False, False, True))
print (formatter %(formatter, formatter, formatter, formatter))
print (formatter %(
    "I had this thing \n", #For some reason I cannot get each of the lines to start on a new line, without affecting the other outputs.
    "That could keep me up at night \n",
    "But it didn't sing \n",
    "So I didn't feel right \n" #Next level rhyming :D
))
