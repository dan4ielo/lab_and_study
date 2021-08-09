# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive nuber that is evenly divisible
# by all of the numbers from 1 to 20?

# We are essentially looking for the smallest common multiple (NOK)

# Using a simple algorithm
# This method works easily for finding the lcm of several integers.[citation needed]

# Let there be a finite sequence of positive integers X = (x1, x2, ..., xn), n > 1. The algorithm proceeds in steps as follows: on each step m it examines and updates the sequence X(m) = (x1(m), x2(m), ..., xn(m)), X(1) = X, where X(m) is the mth iteration of X, that is, X at step m of the algorithm, etc. The purpose of the examination is to pick the least (perhaps, one of many) element of the sequence X(m). Assuming xk0(m) is the selected element, the sequence X(m+1) is defined as

# xk(m+1) = xk(m), k ≠ k0
# xk0(m+1) = xk0(m) + xk0(1).
# In other words, the least element is increased by the corresponding x whereas the rest of the elements pass from X(m) to X(m+1) unchanged.

# The algorithm stops when all elements in sequence X(m) are equal. Their common value L is exactly lcm(X).

# For example, if X = X(1) = (3, 4, 6), the steps in the algorithm produce:

# X(2) = (6, 4, 6)
# X(3) = (6, 8, 6)
# X(4) = (6, 8, 12) - by choosing the second 6
# X(5) = (9, 8, 12)
# X(6) = (9, 12, 12)
# X(7) = (12, 12, 12) so lcm = 12.
def replace_values(_list):
    '''
    A function used for differenciating between list objects
    '''
    new_list = [element for element in _list]
    return new_list
    
def least_common_value(_list):
    step_counter = 0
    new_list = replace_values(_list)  # Create a new object that is equal to the argument but with different id
    while True:
        # print ('current list is {}'.format(new_list))
        # print ('the value of _list is {}'.format(_list))
        index = new_list.index(min(new_list)) # Get the index of the smallest element
        # print ('current index: {}'.format(index))
        # print ('new_list[{}] + _list[{}] = {} + {}'.format(index, index, new_list[index], _list[index]))
        new_list[index] = new_list[index] + _list[index] # Increment the value
        # print ('the new list is {}'.format(new_list))
        if new_list.count(min(new_list)) == len(new_list): # while elements in list != from each other
            break
        # step_counter += 1
        # if step_counter > 9: break
    return new_list

sequence = [num for num in range(1, 11)]
print (sequence)
print (least_common_value(sequence))


