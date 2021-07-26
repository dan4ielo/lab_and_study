#In this excersize we continue with the printing of values

print ("mary had a little lamb.")
print ("Its' fleece was white as %s. " %"snow")
print ("And everywhere that Mary went.")
print ("." * 10) #Prints a line of 10 dots

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

end7 = "B"
end8 = "u"
end9 = "r"
end10= "g"
end11= "e"
end12= "r"

#print (end1 + end2 + end3 + end4 + end5 + end6,) #Here we have two print statements, which print their respective
#print (end7 + end8 + end9 + end10 + end11 + end12) #values on different lines

print (end1 + end2 + end3 + end4 + end5 + end6, #Here we have one print statement that spans on mulitple lines
end7 + end8 + end9 + end10 + end11 + end12) #This results in us seeing the end print statement on one line
                                            #We achieve this by implementing the coma at the end of the first line
#In Python 2 the same code would look like this:
#print end1 + end2 + end3 + end4 + end5 + end6,
#print end7 + end8 + end9 + end10 + end11 + end12 #Resulting in the same lines as in code lines 25 and 26 in the file
