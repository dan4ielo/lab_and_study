# Boolean practice

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print ("Not many cats! The world is safe")

if people < dogs:
    print ("The world is drooled on!")

if people > dogs:
    print ("The world is dry!")

dogs += 20

if people >= dogs:
    print ("People are greater than or equal to the dogs.")

if people <= dogs:
    print ("People are less than or equal to dogs.")

if people == dogs:
    print ("People are dogs.")

print ("\n +-------------------------+ \n")

# If/elif/else

people = 25 
cars = 30 
buses = 15

if cars > people:
    print ("We should use the cars more")
elif cars < people: 
    print ("We should not take the cars. There aren't enough!!")
else:
    print ("We can't decide!")

if buses > cars:
    print ("That's way too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

if people > buses:
    print ("Alright, let's just use the buses.")
else:
    print("Fine, let's stay home then.")
