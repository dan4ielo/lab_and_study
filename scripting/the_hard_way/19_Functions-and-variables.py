# This excercise shows that the variables in a functions are not neccessarily directly connected
# To the arguments of the script

def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print ("You have %d of cheese!" %(cheese_count))
    print ("You have %d cboxes of crackers" %(boxes_of_crackers))
    print ("Man that's enough for a party! When do we have to come? \n")

# We can give the function arguments directly 
cheese_and_crackers (20, 30)

# Or we can use variables defined in the script
variable_one = 10
variable_two = 50
cheese_and_crackers (variable_one, variable_two)

# It is also possible to do math inside of the function
cheese_and_crackers ( 2 * 7, 8 * 8 )

# We can even combine both variables and math
cheese_and_crackers (variable_one + 13, variable_two / 5)
 