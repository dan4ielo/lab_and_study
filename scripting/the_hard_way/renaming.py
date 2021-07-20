# This file is used to rename all of the excercises from the book Learn Python the hard way

import os

def get_names(_file):
    old_names = []
    new_names = []
    
    return old_names, new_names # two lists containing the old names and the new ones


current_directory = os.getcwd()

print (current_directory)
print()

name_changes = input("Please specify a source file: ")

with open(name_changes, 'r') as names_list:
    # get_names(names_list)
    print (names_list.readlines())
