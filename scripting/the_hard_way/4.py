#This excersize focuses on how do Variables and Names work in Python

cars = 60
space_in_a_car = 4.0
drivers = cars * 0.75
passengers = cars * 2.1
cars_not_driven = cars - drivers
cars_driven = cars - cars_not_driven
carpool_capacity = cars_driven * space_in_a_car
avarage_passengers_per_car = passengers / cars_driven

print ("There are ", cars, " number of cars available for use")
print ("There are only ", drivers, " drivers available")
print ("There will be ", cars_not_driven, " empty cars today")
print ("We can transport ", carpool_capacity, " people today")
print ("We have ", passengers, " guests that need to get to the carpool today")
print ("We need to put about ", avarage_passengers_per_car, " people in each car")
