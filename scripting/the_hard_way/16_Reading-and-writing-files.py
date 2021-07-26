#Reading and writing files
#Functions used for operating with files:
#close      - closes the file, Like File->Save.. in the editor
#read       - reads the contetns of the file. You can assign the result to a variable
#readline   - reads just one line of a text file
#write(n)   - writes "n" to the file

from sys import argv
script, filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that - hit CTRL+C (^C).")
print("If you do want that hit RETURN.")

#Here by pressing enter we are just entering an empty value that is not safed anywhere in the code, allowing us to halt the execution of the program
input("?")

print("Oppening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

s = line1 + "\n" + line2 + "\n" + line3 + "\n"

print("I'm going to write these to the file")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(s)

print("And finally we are done... Now just to close it.")

target.close()
