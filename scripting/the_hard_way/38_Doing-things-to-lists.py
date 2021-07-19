# An excercise to show that when we use an object's function
# Python actually transforms it into function_name(name_of_object,parameters_given)

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print (ten_things)
print ("Wait there aren't 10 things in that list... Let's fix that")

stuff = ten_things. split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There are {} items now.".format(len(stuff)))

print ("There we go: ", stuff)

print ("Let's do some things with stuff")

print (stuff[1])
print (stuff[-1]) # Fancy way of returning the last item in the list
print (stuff.pop())
print (" ".join(stuff)) # Join all elements of a list into a single string
print ("#".join(stuff[3:5])) # Join only a specific range of elements from the list using the given delimiting character
