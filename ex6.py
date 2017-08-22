#Different ways to format or concatination of strings.
types_of_people = 10
x = f"There are {types_of_people} types of people."
#F'string example for storing in varibles
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
                        #1                      #2
print(x)
print(y)
#print statement using 'F' Strings
print(f"I said: {x}")#3
print(f"I also said: {y}")#4
#Format function demo code
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {} "
#print statement using format function
print(joke_evaluation.format(hilarious))
#String varibles
w = "This is the left side of..."
e = "a string with right side"
#print statement concatinating both strings. Operator overloading '+'
print(w+e)
