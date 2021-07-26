#This excersise focuses on reading files
from sys import argv
script, file_name = argv

#Safes a the openned text file within a variable called txt
txt = open(file_name)

print("Here is the file %r:" %file_name)
#Reads the text file from the txt variable and prints it out
print(txt.read())
#This is used for testing (I added it on my own) in order to understand what the program expects to see in terms of the filename
print(file_name)
print("Type the filename again:")
#Stores the typed in characters within a new variable that is used to call out the file a second time
file_name_second = input("> ")
txt_second = open(file_name_second)

print(txt_second.read())
