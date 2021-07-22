# This is a test to see if I can create my own personal
# game - simmilar to 43rd excercise

# Let's begin with the story: 

# Main character is a cowerker in Innovator and needs to go get
# Something to eat from the Kebab place to replenish his energy.
# As the protagonist walks to the Kebab place you meet different
# people that talk to you and thus take out of your time. You
# have 30 minutes for launch so you win the game if you manage to
# come back on time.

# Class structure:

# Engine():
# * start()
# Map():
# * next_scene()
# * openning_scene()
# Scene
# * enter()
#   |- Office
#   |- Corridor (chance to trip down the stairs)
#   |- Street
#   |- Kebab_place (10-15-20 minutes for launch depending on choice)
#   |- Too_late()
#   |- Win()
# Person
# * introduce()
#   |- Guy  # Random chance if you meet a guy or a girl.
#       - talking_skill
#       - interesting_factor
#   |- Girl # Each takes a different amount of time to talk to
#       - talking_skill
#       - interesting_factor
# Protagonist
# -hungry
# -hurt
# -timer
# * eat()
# * talk()
# * walk()
from sys import exit
from random import randint
import time
import math

class Engine():

    def __init__(self, scene_map, protagonist):
        self.scene_map = scene_map
        self.protagonist = protagonist

    def start(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter(self.protagonist)
            current_scene = self.scene_map.next_scene(next_scene_name)

class Person():
    
    def __init__(self):
        pass

    def introduce():
        print ("This person does not exist, so we can't introduce him :D")
        exit(1)

class Protagonist():
    
    def __init__(self):
        self.timer = 35
        self.hurt = False
        self.hungry = True

    def eat(self):
        print ("You decide to order your favourite. Do you eat it in a hurry or do you savor it?")
        print ("(savor / hurry)")

        answer = input("> ")

        if answer == "savor":
            self.timer -= 20
            self.hungry = False
            self.check()
        elif answer == "hurry":
            self.timer -= 10
            self.hungry = False
            self.check()
   
    def check(self):
        if self.timer <= 0:
            return "too late"

    def talk(self, encounter):
        print ("You stop and talk.")
        self.timer = self.timer - (encounter.talking_skill + encounter.interesting_factor)//10
        self.check()
        return

    def walk(self, encounter):
        print ("You pass {} and keep walking only waving back.".format(encounter))
        return

class Guy(Person):
    
    def __init__(self):
        self.talking_skill = randint(1,3)*10
        self.interesting_factor = randint(6,10)*10
    
        self.who_is_that = [
            "your room mate from your 1st year at uni",
            "your best friend",
            "your long lost brother from Egypt",
            "the new boyfriend of your ex"
        ]

    def introduce(self):
        return self.who_is_that[randint(0,len(self.who_is_that)-1)]

class Girl(Person):
    
    def __init__(self):
        self.talking_skill = 95
        self.interesting_factor = randint(6,9) * 10   # between 60 and 90

        self.who_is_that = [
            "your crush",
            "that annoying girl from school",
            "your ex",
            "the girl who was 'secretly' in love with you",
            "that crazy b***h with the cool body"
        ]

    def introduce(self):
        return self.who_is_that[randint(0,len(self.who_is_that)-1)]

class Scene():

    def enter(self, protagonist):
        print ("This scene is not yet created. PLease make sure you instaniate the correct scene.")
        exit(1)

class Office(Scene):

    def enter(self, protagonist):
        print ("You have been working all morning at Innovator since 9 a.m.")
        print ("It was abaout time you decided to go grab something for launch")
        print ("But you have only 40 minutes until a very important meeting, ")
        print ("which might take all afternoon and you will be starving all day.")
        print ()
        print ("Do you go to grab a bite? (y/n)")

        answer = input("> ")
        
        if answer == "y":
            print ("You finish up with the work you are doing now and head out.")
            print ("To reach the kebab place will take you 5 minutes, but you already")
            print ("took 5 minutes to finish things up. You gotta hurry")
            return "corridor"
        elif answer == "n":
            return "win"

class Corridor(Scene):

    def fall(self):
        chance = randint(1,10)

        if chance == 5: 
            return True
        else:
            return False

    def enter(self, protagonist):
        print ("You enter the corridor. While going down the stairs you remmember you")
        print ("forgot your mask (and Covid ...). Do you go back for it or do you hope")
        print ("to bulshit your way through it when you get there? (go back/ bullshit for the win)")

        answer = input("> ")

        if answer == "go back":
            print ("You just lost 3 minutes to do that")
            print ()
            protagonist.timer = protagonist.timer - 3
            if self.fall():
                protagonist.hurt = True
                print ("Aaand... you fell down the stairs. Maaan that sucks. You hurt your leg")
                print ("and now it's going to take you 10 minutes to reach the kebab place.")
                print ("Do you still go? (y/n)")
                
                answer_fall_dmg = input("> ")

                if answer_fall_dmg == "n":
                    return "win"
                else:
                    return "street"
            else:
                return "street"
        elif "bullshit" in answer: 
            return "street"
        else:
            print ("Can you even read?")
            return "corridor"

class Street(Scene):

    def introduction(self):
        # who do you meet?
        sex = {1:Guy(), 2:Girl()}
        person = sex[randint(1,2)]          # creates the object
        return person

    def encounter(self, chance_from, chance_to, protagonist):
        people_met = randint(chance_from,chance_to)
        for encounter in range(0,people_met):
            person = self.introduction()
            introduction = person.introduce()
            print ("You meet {}.".format(introduction))
            print ("Do you stop to talk to them? (y/n)")

            talk = input("> ")
            if talk == "n":
                protagonist.walk(introduction)
                continue
            else:
                protagonist.talk(person)
                print ("You took some time to talk and now you have to hurry up. You have")
                print ("{} minutes left".format(protagonist.timer))
                continue

    def enter(self, protagonist):
        if protagonist.hurt and protagonist.hungry:
            protagonist.timer -= 10
            print ("Finally, you made it out. Stumping along the path you see someone waving.")
            self.encounter(1, 2, protagonist)
            if protagonist.check() == "too late":
                return "too late"
            return "kebab"
        elif protagonist.hungry and not protagonist.hurt:
            protagonist.timer -= 5
            print ("You get out of the building and start walking along the street. While walking")
            print ("you see someone waving at you.")
            self.encounter(1, 2, protagonist)
            if protagonist.check() == "too late":
                return "too late"
            return "kebab"
        elif not protagonist.hungry and protagonist.hurt:
            print ("You need to hurry back to the office. You really don't have much time. But at")
            print ("least your leg doesn't really hurt anymore")
            protagonist.timer = protagonist.timer - 5
            self.encounter(0,1, protagonist)
            if protagonist.check() == "too late":
                return "too late"
            return "win"
        elif not protagonist.hungry and not protagonist.hurt:
            print ("You have done what you set out to do. Now hurry back to the office")
            protagonist.timer -= 5
            self.encounter(0,1, protagonist)
            if protagonist.check() == "too late":
                return "too late"
            return "win"

class Kebab_place(Scene):

    def enter(self, protagonist):
        print ("You made it to the Kebab place! And you have {} minutes left".format(protagonist.timer))
        protagonist.eat()
        return "street"

class Too_late(Scene):

    def enter(self, protagonist):
        print ("You struggled with all your might, but didn't make it on time")
        print ("You curse the people that you met for everything they have done to you")
        print ("After realising, however, that you are the one to blame you commit suicide")
        exit(1)

class Win(Scene):

    def enter(self, protagonist):
        print ("Congrats! You made it on time. Your mom will be proud.")
        exit(1)

class Map():
    
    scenes = {                              # Set a dictionary with key-value pairs
            "office": Office(),             # that will be used to change through scenes
            "corridor": Corridor(),
            "street": Street(),
            "kebab": Kebab_place(),
            "too late": Too_late(),
            "win": Win()
        }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)   # Get the object based on the key given

    def opening_scene(self):
        return self.next_scene(self.start_scene)  

game_map = Map("office")
player = Protagonist()
game_engine = Engine(game_map, player)

game_engine.start()
