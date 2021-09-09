# A permutation is an ordered arangement of objects. For example, 3124 is on possible
# permutation of the digits 1, 2, 3 and 4. If all the permutations are listed alphabetically
# or numerically, we call it lexicographic order. The lexicographic permutations of 0, 1, 2 are:
                # 012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

# def num_of_perm(lon): # Take in a list of numbers to permutate
#     sort_lon = sorted(lon) # From small to high - [0, 1, 2, 3, 4 ...]
#     count = 1
#     # for idx, _ in enumerate(sort_lon):
#     for i in range(1, len(sort_lon) + 1):
#         count *= i
#     return count

from itertools import permutations

test = [0, 1, 2]
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(num_of_perm(test))
# print(num_of_perm(data))

l = list(permutations(range(10)))
print (len(l))
l = sorted(l)
print(l[999999])

# Python function to print permutations of a given list
# def permutation(lst):
# 
#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []
# 
#     # If there is only one element in lst then, only
#     # one permutation is possible
#     if len(lst) == 1:
#         return [lst]
# 
#     # Find the permutations for lst if there are
#     # more than 1 characters
# 
#     l = [] # empty list that will store current permutation
# 
#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#        m = lst[i]
# 
#        # Extract lst[i] or m from the list.  remLst is
#        # remaining list
#        remLst = lst[:i] + lst[i+1:]
# 
#        # Generating all permutations where m is first
#        # element
#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l
# 
# 
# # Driver program to test above function
# data = list('123')
# for p in permutation(data):
#     print (p)

