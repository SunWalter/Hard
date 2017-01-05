from sys import exit

def gold_room():
    print ("This room is full of gird. How much do you take? ")

    choice = input('> ')
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not a greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch a honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        chioce = input('> ')

        if choice == "take money":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print ("I got no idea what that means.")

def cthulhu_room():
    print ("Here you see the great cthulhu_room.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    chioce = input('> ')

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print (why, "good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is door to your right or left.")
    print ("Which one do you take?")

    chioce = input('> ')

    if chioce == "left":
        bear_room()
    elif chioce =="right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
