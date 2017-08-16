# Number of Cars.
cars = 100
# Study-drill Updations.
#space_in_a_car = 4.0
# Number of drivers.
drivers = 30
# Number of passengers.
passengers = 90
# Number of cars which are placed in junkyard.
cars_not_driven = cars - drivers
 # Number of cars driven.
cars_driven = drivers
#Carpool capacity.
carpool_capacity = cars_driven * 4.0 #Study drill Updations.
# Number of passengers in one car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars ,"cars available.")
print("There are only", drivers ,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can trasport", carpool_capacity,"people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
