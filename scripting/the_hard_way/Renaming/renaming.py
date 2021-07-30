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
for old_name, new_name in zip(old_names, new_names):
    # print(current_directory + "/" + old_name)
    try:
        os.rename(src = current_directory + "/" + old_name, dst = current_directory + "/" + new_name)
    except FileNotFoundError:
        continue
