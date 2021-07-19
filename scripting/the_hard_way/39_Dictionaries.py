# Dictionaries in Python

# Create a mapping of state to abbreviation
states = {
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities = {
        'CA':'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some states
print ()
print ("-" * 10)
print ("Michigan's abbreviation is: {}".format(states['Michigan']))
print ("Florida's abbreviation is: {}".format(states['Florida']))

# print out some cities
print ()
print ("-" * 10)
print ("NY State has: {}".format(cities['NY']))
print ("OR State has: {}".format(cities['OR']))

# do it by using the state then cities dict
print ()
print ("-" * 10)
print ("Michigan has: {}".format(cities[states['Michigan']]))
print ("Florida has: {}".format(cities[states['Florida']]))

# print every state abbreviation
print ()
print ("-" * 10)
for state, abbrev in states.items():
    print ("{} is abbreviated {}".format(state, abbrev))

# print every city in state
print ()
print ("-" * 10)
for abbrev, city in cities.items():
    print ("{} has the city of {}".format(abbrev, city))

# print now do both at the same time
print ()
print ("-" * 10)
for state, abbrev in states.items():
    print ("{} state is abbreviated {} and has the city of {}".format(state, abbrev, cities[abbrev]))
print ("-" * 10)

# safely get an abbreviation by state that might not be there
state  = states.get("Texas", None)  # This means that if the searched term - Texas, is not found
                                    # the state variable will get a default value of None

if not state:
    print ("Sorry, there is no Texas in our records")

# get a city with a default value
city  = cities.get("TX", "Does not exist")
print ("The city for the state 'TX' is: {}".format(city))
