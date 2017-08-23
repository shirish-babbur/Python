print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy!")


# Study drill
print("Let's go for quick round of quiz.")
score = 0
total = 4
country = input("Which country has 2nd largest population? ") # input function can take string as parameter which can be printed on screen.
if (country == "India"):
    score+=1

wonder = input("Which is the 7th wonder in the world? ")
if (wonder == "Taj Mahal"):
    score+=1

pm = input("Who is the priminister of India? ")
if(pm == "Narendra Modi"):
    score+=1

result = eval(input("What will be result of this: 5 + 2 * (16 / 4) / 4 ")) # Here eval will convert raw input to proper datatype.In our case it is Number.
if(result == 7):
    score+=1

print(f"Hurray! You have completed the quiz with a score of {score} out of {total}.")
