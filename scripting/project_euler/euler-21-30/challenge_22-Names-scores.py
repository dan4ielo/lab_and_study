# Using names.txtm a 46K text file containing over 5 000 names, begin by sorting it into 
# alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name space.

# For example, when the list is sorted into alphabetical  order, COLIN, which is worth 
# 3+ 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So COLIN would obtain a score of
# 938 * 53 = 49714

# What is the total of all name scores in the file?

def score(name):
    score = 0
    name = name.upper()
    for letter in name:
        score += ord(letter) - 64 # Get the ASCII Value and substract 'A' = 65
    return score

file_name = input('> ')
with open(file_name) as file:
    # names = file.readline().split(',')
    names = [name.replace('"', '') for name in file.readline().split(',')]

names[-1] = names[-1].replace('\n', '')
names.sort()

pos = 0
result = 0
for name in names:
    if name == 'COLIN':
        print (pos)
    pos += 1 # Start from 1st position
    tmp = pos * score(name)
    result += tmp

print (result)
