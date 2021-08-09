# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive nuber that is evenly divisible
# by all of the numbers from 1 to 20?

def replace_values(_list):
    new_list = [element for element in _list]
    return new_list
    
def divide_list(_list, divider):
    for el in _list:
        if el == divider:
            _list.remove(el)
        elif el % divider == 0:
            index = _list.index(el)
            _list[index] = int(el / divider)
        else: # This is obsolete, but still
            index = _list.index(el)
            _list[index] = el
    return _list

def get_multipliers(_list, primes):
    new_list = replace_values(_list)
    new_list.remove(1) # sanitary cleaning
    multipliers = []
    for prime in primes:
        try:
            while min(new_list) % prime == 0:
                new_list = divide_list(new_list, prime)
                multipliers.append(prime)
                print(new_list)
        except:
            continue
    return multipliers

def least_common_multiple(_list):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    multipliers = get_multipliers(_list, primes)
    print(multipliers)
    result = 1
    for el in multipliers:
        result = result * el
    return result

sequence = [num for num in range(1, 21)]
print (sequence)
print (least_common_multiple(sequence))
