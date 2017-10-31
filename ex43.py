from random import randint
from sys import exit

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while(current_scene != last_scene):
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        #be sure to print out current scene
        current_scene.enter()

class Death(Scene):
    quips = ['You Died. You kinda suck at this',
            'You Mom would be proud...if she were smarter',
            'Such a Luser.',
            "I have a small that's better at this",
            "You're worse than your Dad's jokes!"]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("Looks like a big place and in front you there is this creature called GOTHON!")
        print("You need to defate this guy to go to the next level.You can destract him with your lame jokes though.")
        decision = input("What will you do?\n>>")
        if "joke" in decision:
            return 'LaserWeaponArmory'
        else:
            return 'Death'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("This is where you are in Ship.You have a Neutron bomb choice is yours.")
        print("Wait there!...But you have a escapePod as well..Door to escapePod opens when right combination is given")
        print("Good Luck Guessing..")
        right_combo = randint(100,1000)
        guesses = 1
        number = 0
        while(guesses < 3 and right_combo != number):
            if guesses == 2:
                print("Hint : { 2 + 3 -2, 5 + 5 - 2, 3 + 8 / 2}")
                right_combo = 387
            number = int(input(">>"))
            guesses += 1

        if right_combo == number:
            print("Congrats! Door Opened...")
            return 'TheBridge'
        else:
            print("Dumb!")
            return 'Death'

class TheBridge(Scene):
    def enter(self):
        print("Oh Bad thing you cannot enter escapePod until you defate this GOTHON...What you will do?")
        decision = input("What will you do?\n>>")
        if "joke" in decision:
            print("Another Joke...xD..yay!..good to go.")
            return 'EscapePod'
        else:
            return 'Death'

class EscapePod(Scene):
    def enter(self):
        print("Enter the right combination to get the right pod..")
        number = int(input(">> "))
        if (number % 2) == 0:
            print("Yay! right Pod...you escaped...You live!")
            return 'finished'
        else:
            print("Wrong one Bye Bye...")
            return 'Death'

class finished(Scene):
    def enter(self):
        print("Long Live My Friend!")

class Map(object):
    scenes = {
            'CentralCorridor': CentralCorridor(),
            'LaserWeaponArmory' : LaserWeaponArmory(),
            'TheBridge' : TheBridge(),
            'Death' : Death(),
            'EscapePod' : EscapePod(),
            'finished' : finished()
    }
    def __init__(self,strart_scene):
        self.start_scene = strart_scene
    def next_scene(self,scene_name):
        val = Map.scenes[scene_name]
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map("CentralCorridor")
a_game = Engine(a_map)
a_game.play()
