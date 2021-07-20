# Functions and files
from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)
current_line = 0
lines_to_print = 3

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind it. Kind of like a tape: \n")
rewind(current_file)

print ("Let's print %d lines: \n" %(lines_to_print))
for current_line in range(1, lines_to_print + 1):
    print_a_line(current_line, current_file)