from random import randiant

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        Lines_death = [
        'You are so weak, lueluelue.',
        'You lose it.',
        'Three Body is immortal!!!'
        ]
        print (randiant(Lines_death[0,2]), "END!!!")

class Central_Corridor(Scene):

    def enter(self):
        print ("""You have entered the Central_Corridor, It is the first scene you
        will in. Just enjoy this game! In this scene, you will meet a alien from
        ThreeBody plant. Do you want to give up? Then you will have a choose:""")

        yesorno = input("Say: yes or no >: ")
        if yesorno == "yes":
            print ("""You give up and the Three Body man will kill you with Drop of Water
            (a kind of Weapon), then destroy the Earth.""")
			return 'death'

        if yesorno == "no":
            print ("""You stand up and build lots of Aircraft Carrier to fight with Three Body man,
            But you don't know you will dead or live.""")
			return 'aircraft_carrier'

class Aircraft_Carrier(Scene):

    def enter(self):
        print ("""People on Earth build lots of Aircraft Carrier to fight with
        Three Body man. But them don't know a Drop of water will kill all of them easily.
        People choose four Masters to figure out a wanderful way to beat back Three Body.
        But only one can finally finish this task well. Which one you guess:
        1)SUN Weigao
        2)MO Xiaoyu
        3)HU Bo
        4)LUO Ji
        """)
		master = input ("Now type in the number in front of the Master's Name >:")
		if master == '1':
			print ("You Dead! Master SUN Weigao is not the man who can destory the Three Body!")
			return 'death'
		elif master == '2':
			print ("You Dead! Master MO Xiaoyu is not the man who can destory the Three Body!")
			return 'death'
		elif master == '3':
			print ("You Dead! Master HU Bo is not the man who can destory the Three Body!")
			return 'death'
		else:
			print ("""Congratulations! You choose LUO Ji as the true Master, and you are right.
            He is the man who can kill the Three Body !""")
			return 'the_bridge'

class The_Bridge(Scene):

    def enter(self):
        print ("""The bridge is the place you and the Master LUO Ji you choosed to have a final battle.
        But!!!
        The Drop of Water killed all of you in just one second! By through all the
        aircraft carrier from one side to the other side! Earth Human failed !
        And all human become slaves except five people who ZHANG Beihai is the head.
        NOW !!!
        Earth Human have two choose:
        1) Escape! This is the only way Earth Human can keep living and continue the
        earth civilization.
        2) Death! All Earth Human dead! Then the Three Body man will move from
        the Three Body plant to the earth. A new civilization will be created!

        which one do you choose?""")

        tobeornot = input("1 or 2 >:")
        if tobeornot == '1':
            return 'escape'
        else:
            return 'death'

class Escape(Scene):

    def enter(self):
        print ("""After the final battle, Most of people dead and only few astronauts
        with head is ZHANG Beihai survived with other four and only four human.
        They will escape to a plant far away from the earth. And they have a critical
        important task to continue the Human civilization.

        END!!!

        """)

class Map(Scene):

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        scene_name = {
        "death": "Death",
        "central_corridor": "Central_Corridor",
        "aircraft_carrier": "Aircraft_Carrier",
        "the_bridge": "The_Bridge",
        "escape": "Escape"}

    def opening_scene(self):



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
