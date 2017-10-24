# create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('--' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('--' * 10)
print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities direction
print('--' * 10)
print("Michigan has : ", cities[states['Michigan']])
print("Florida has : ", cities[states['Florida']])

# print every state abbreviation
print('--' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('--' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} state has {city}")

# Now do both at the same time
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")
    print(f" and has city {cities[abbrev]}")

print('--' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, No Texas!")

# get a city with default
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")


# Dictionary in Python v3.6 is Ordered.
States_IN = {
    "Maharashtra":"MH",
    "Karnataka":"KA",
    "Telangana":"TN",
    "Andhra Pradesh":"AP"
}

Cities_IN = {
    "MH":"Mumbai",
    "KA":"Banglore",
    "TN":"Hydrabad",
    "AP":"Amaravati"
}
for state,abbrev in States_IN.items():
    print(f"State {state} has abbreviation as {abbrev}.")
    print(f"This {state} has Capital city {Cities_IN[abbrev]}.")

print("-"*20)
print("Now Let's delete Maharashtra!")
del States_IN['Maharashtra']
del Cities_IN['MH']
print("After Deletion")
for state,abbrev in States_IN.items():
    print(f"State {state} has abbreviation as {abbrev}.")
    print(f"This {state} has Capital city {Cities_IN[abbrev]}.")
print("-"*20)

print("Now Let's merge both the Dictionaries....")
States_IN_List = list(States_IN.items())
Cities_IN_List = list(Cities_IN.items())
combined = dict(list(zip(States_IN_List, Cities_IN_List)))
print(len(combined))
for state,abbrev in combined.items():
    print(f"State {state} has abbreviation as {abbrev}.")
