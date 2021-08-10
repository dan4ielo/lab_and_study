# The four adjacent digits in the 1000-digit number that have the greatest product are 9*9*8*9 = 5832

# The 1000-digit number:
number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

# Find the 13 adjacent digits in the 1000-digit number that have the greatest product. What is the value of the product?

# We can split the string around the 0s since we are not going to use them in the multiplication anyway

#========= Highest 4 =========#

#def extract_fours(string):
#    four= ''
#    list_of_fours = []
#    while len(string) > 4:
#        four = string[0:4]  # Create a four
#        list_of_fours.append(four)
#        string = string.replace(string[0], '', 1) # Remove the first element
#    list_of_fours.append(string) # Append the last 4 characters
#    return list_of_fours

#def create_fours(num):
#    group = 4
#    segments = num.replace('1', '0').split('0') # Remove 1s and 0s since they don't contribute to multiplication
#                                                # and we are looking for a small substring - 4
#    segments = [segment for segment in segments if len(segment) >= group]
#    fours = [segment for segment in segments if len(segment) == group] # Separate the fours
#    for segment in segments: 
#        if len(segment) > group:
#            for extracted in extract_fours(segment):
#                fours.append(extracted)
#    return fours

#def highest_4(num):
#    fours = create_fours(num)
#    highest_result = 0
#    for group in fours:
#        result = 1  # Reset for each element - each four
#        for i in range(len(group)):
#            digit = group[i]
#            result = result * int(digit)
#        if result > highest_result: highest_result = result
#    return highest_result

#test = "1092384074"  # 10 digit number for testing
#print (highest_4(test))
#print (highest_4(number))
# highest_4(number)

#========= Highest 13 ==========#

def extract_groups(string, group):
    four= ''
    list_of_groups = []
    while len(string) > group:
        this_group = string[0:group]  # Create a group
        list_of_groups.append(this_group)
        string = string.replace(string[0], '', 1) # Remove the first element
    list_of_groups.append(string) # Append the last group of characters
    return list_of_groups

def create_groups(num, group):
    segments = num.split('0') # Remove since they don't contribute to multiplication
    segments = [segment for segment in segments if len(segment) >= group]
    groups = [segment for segment in segments if len(segment) == group] # Separate the fours
    for segment in segments: 
        if len(segment) > group:
            for extracted in extract_groups(segment, group):
                groups.append(extracted)
    return groups

def highest_result(num, group):
    groups = create_groups(num, group)
    highest_result = 0
    for group in groups:
        result = 1  # Reset for each element - each four
        for i in range(len(group)):
            digit = group[i]
            result = result * int(digit)
        if result > highest_result: highest_result = result
    return highest_result

print(highest_result(number, 13))

