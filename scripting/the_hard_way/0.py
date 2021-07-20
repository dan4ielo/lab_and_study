# This file is used to rename all of the excercises from the book Learn Python the hard way

import os

def get_names(source):
    old_names = []
    new_names = []
    
    lines = source.readlines()

    for line in lines:
        try:
            old_names.append(line.split(" . ")[0])
            new_names.append(line.split(" . ")[1])
        except IndexError:
            continue
    return old_names, new_names # two lists containing the old names and the new ones

source = input("Please specify a source file: ")

with open(source, 'r') as names_list:
    old_names, new_names = get_names(names_list)

current_directory = os.getcwd()

print (current_directory)

destination = current_directory + "/" + new_names[2]
os.rename(src = current_directory + "/" + old_names[2], dst = destination)
# os.replace(src = current_directory + "/" + old_names[1], dst = current_directory + "/" + new_names[1])
# os.rename(src = current_directory + "/1.py", dst = current_directory + "/1_A-good-first-program.py")

