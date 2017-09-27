
def start():
    print("Hello there!")
    play = input("Ready to play?")

    if "y" in play:
        first()
    elif "n" in play:
        print("You have missed great chance to win ton of gold!")
    else:
        print("I don't Understand what you are saying")
        start()

def first():
    print("Let's start by knowing about you...")
    age = int(input("What is your age?\n> "))
    itr = 0
    if age > 1 and age < 99:
        permission = True
    else:
        itr += 1
        print("Don't fool me around..This is your last chance.")
        if itr <= 1:
            first()
        else:
            bye("Sorry for your loss!")
    print("There are 3 doors depending on your fate a door will open.")
    print("Calculating.....fingures crossed...")
    door = age % 2;
    print(f"Voila! you got number {door}")
    if (door == 0):
        door_zero()
    elif door == 1:
        door_one()
    else:
        door_two()

def bye(line):
    print(line," Good Job!")

def gold_cave():
    print("Whoa....This is what you get if you are good person!")
    print("Take home these tons of gold!")

def door_zero():
    print("It seems you are dark room where you can hear sound of snakes...")
    print("You have a stick.")
    print("What you wanna do go back or fight with it?")
    decision = input("> ")

    if "back" in decision:
        print("You are not yet saved or cleared this game...insted you just rolled back..")
        start()
    elif "stick" in decision:
        print("Start biting with stick everywhere..you might get lucky!")
        print("Boom!...sound stops.. you can watch out for the door from where you can see something glowing..")
        gold_cave()
    else:
        bye("You will be die due to poison by snake..")

def door_one():
    print("You are in the second room.....Every room comes with it's surprises..!")
    print("There is a strange man standing over there and watching you")
    print("You have two paths right and left")
    print("What would you do?")
    decide = input("> ")

    if "man" in decide:
        print("Man looks at you and points to left direction...")
        direction = input("Where would you go?\n> ")

        if direction == "left":
            gold_cave()
        else:
            bye("You have gone in infite long path which will never end..")
    elif "left" in  direction:
        gold_cave()
    else:
        bye("You have gone in infite long path which will never end..")

def door_two():
    print("You are in the Third room.....Every room comes with it's surprises..!")
    print("You got a man dying in this room and a key to a secret door...you have to make one choice..")
    print("Either save the man or take the key you can't do the both taking any one of them will vanish other.")
    took = input("What will you do?\n> ")

    if "man" in took:
        print("Great decision by you..you are not greedy..so your prize is...secret door opens...")
        gold_cave()
    else:
        bye("You are a greedy!...door will not open by the key..you are now trapped....")

start()
