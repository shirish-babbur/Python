# defiend a function that takes two arguments and prints those values.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enoughfor a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# Call to function defined above using direct value passing.
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Call to function defined above using varibles defined in script.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# Call to function defined above using operation between constants.
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, vaiables and math:")
# Call to function defined above using variables and some constants.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

# 1 Taking inputs from the User.
am_crackers = input("values for anount of cheese and crackers: ")
am_cheese = input()
cheese_and_crackers(am_cheese, am_crackers)

# 2 Using other function to call above defined function
print("Calling through call_original function.")
def call_original():
    cheese_and_crackers(100,200)

call_original()
