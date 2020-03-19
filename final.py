""""
About: This program will be a mini game based on one of my favorite shows
called Rick and Morty. This will focus on one of their adventures where they
accidentally turned all the humans in the world into a useless slug like creature 
called a Cronenberg. I will allow them to go on a small adventure that is based on
their choices and will follow the criteria given by my teacher.

Name:Nia Alvarado.

Teacher: oe Paris.

Due Date:03/18/2020. 

"""
#This program will make a text adventure
#! usr/bin/env python3

import math 
import PyPDF2 as p2

def dial_ogue():
    """Mainly dialogue, carries main plot."""
    print("The world's population has turned into slug-like creature's called Cronenbergs")
    print("that are forced to roam the earth aimlessly due to Rick's inaccuracy")
    print("when making a love potion for Morty.")
    print("It is up to you what they do next to solve this problem")
    answer = str(input("Are you ready for an adventure? (Yes or No) "))
    if answer.lower().strip() == "yes":
        print("RICK:\n Let's move, we don't have all day! These Cronenbergs won't fix themselves!")
        print("RICKS:\n M-m-MORTY hurry up, even the new guy is faster than you.")
        print("MORTY:\n Alright Rick calm down, you're the one who created this")
        print("problem in the first place, not me.")
        print("RICK:\n Well Morty isn't it you who wanted me to make something to make Jessica like you?")
        print("MORTY:\n ...")
        print("RICK:\n Yeah that's what I thought Morty, let's not forget who got us into this mess.")
        print("MORTY:\n Whatever Rick let's just get this over with.")
    else:
        print("Rick:\n Oh no Morty, this is unsolvable. We have no choice but to leave.")
        print("Morty:\n Where are we going to go rick?")
        print("Rick:\n A new dimension where we can start over right where we want to in the same world we used to have")
        print("Rick and Morty leave to a new dimension find themselves in that dimesnion and kill them to take their place")

print(dial_ogue())

def second_choice():
    """Second choice and main play again function."""
    ending = str(input("Want to play a game? Yes or No?"))
    #says ending, is only one possibility.
    if ending.lower().strip() == "yes":
        dial_ogue()
    else: 
        ending.lower().strip() == "no"
        print("Thanks for playing!")
        #end of game by choice.

print(second_choice())


def mid_game():
    """Is the middle of the game."""
    choice = input("Where would you like to start? Miniverse or Spacecraft?")
    if choice.lower().strip() == "house":
        #choice one.
        print("You have chosen to start the game off by searching for a cure! Here you will find some items")
        things = { 
        "Items in the house": 4, 
        "Items in the miniverse": 2
        }
        #Informs the user
        print(things)
        choice = input("Would you like look in the kitchen or the lab first?  ")
    if choice.lower().strip() == "kitchen":
        #another choice.
        print("We are now in the kitchen and have found nothing. Let's try the lab.")
        print("*Walks to the lab* Check the lab")
        items = {"circuit board","tin can","cable","fleeb","bacteria cell","turbulent juice"}
        for x in items:
            print(x)
            print("Found the items!")
    else: 
        print("Congrats! you chose the right choice. The lab is where everything is located.")
        print("Now walk over to the cabinet and pull it all out.")
        cabinet = input("Open cabinet, enter 'open'")
        #More input that is not a choice really.
    if cabinet == "open":
        print("Here they are!")
        print("Let's move on to finding the defense and speed mega seed.")
    if choice.lower().strip() == "spacecraft":
        print("\nWe will be traveling to the miniverse to retrieve the defense and speed mega seed")
        print("Rick created this miniature universe to power his spacecraft and also stores his seeds here.")
        print("We will no enter and say hellow to the aliens of this miniverse.")
        print("Now that we have said hello we are able to go to the seed forrest.")
        print("Oh no!! Large alien animals are gaurding the forrest!") 
        print("What do you want to do next?")
        
print(mid_game())

def end_game():
    """Essentially end of the game."""
    move = str(input("Fight or teleport them to another dimension? Type fight or teleport to chose a path."))
    if move.lower().strip() == "fight": 
         print("Sorry, you did't survive this fight unfortunately.")
         second_choice()
    else: 
        move.lower().strip() == "teleport"
        print("Oof, now they are gone. Let's move on and get back to the ship.")
        print("You are now back at the ship. Time to fly assemble the items anc create the formula.")
        PDFfile = open("cure.pdf", "rb")
        pdfread = p2.PdfFileReader(PDFfile)
        """Extract single page""" 
        x = pdfread.getPage(0)
        print(x.extractText())
        #should bring up a PDF, hope it does for you cause did not for me.
        
        print("Make sure you have all the items on this list!!")
        print("Rick has now assembled the items but wait! He needs help with this mathematical equation to finish!")
        numbers = float(31.8)
        print("The area of the earth is 31.6 fleeb metros")
        print("We must also use PI: which is 3.14 and multiply them together.")
        guess = str(input("Enter your answer: "))
    while guess != round(numbers*math.pi):
        print("That's not it, try again!")
        try: 
            round(numbers*math.pi) != 99.852
        except ValueError:
            print("close enough.")
        finally:
            print("make sure to round.")
        break
    if guess == round(numbers*math.pi):
        print("Good job you got it!")
        print("Now Rick can finish the formula and spray it across the world!")
        print("*Flies across the world*")
        print("The cure worked! Now everything is back to normal!")
        dial_ogue()

print(end_game())