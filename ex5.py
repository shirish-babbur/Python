name = 'Shirish Babbur'
age = 22 #Yes it's a Lie.
HEIGHT_CONSTANT = 2.54 #Constant to multiply with to convert inches to centimeters.
height = 71  * HEIGHT_CONSTANT #inches
WEIGHT_CONSTANT = 0.435 #Constant to multiply with to convert lbs to Kgs.
weight = 149 *WEIGHT_CONSTANT #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} Kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total} .")
