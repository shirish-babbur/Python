class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#Object created!
happy_bday = Song(["Happy birthday to you,","I don't want to get sued","So i'll stop there!"])

#Object created!
bulls_on_parade = Song(["Thye rallly around tha family","With pockets full of shells"])
print("--"*20)

# Object function Called!
happy_bday.sing_me_a_song()
print("--"*20)

# Object function Called!
bulls_on_parade.sing_me_a_song()
print("--"*20)

thug_song = ["How many brothers fell victim to the streets?","Rest in peace, young nigga, there's a heaven for a G","Be a lie If I told you that I never thought of death","Yes! That's our Thug..!"]
#Object created!
thug = Song(thug_song)

# Object function Called!
thug.sing_me_a_song()
print("--"*20)
