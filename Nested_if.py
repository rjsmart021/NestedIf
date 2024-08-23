#Nested if
#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        action == "cross a river"
        print("You found a boat!")
else:
    place = "cave"
    print("You find a hidden treasure!")

#Task 2: Setting the Scene
#Based on your corrected code from Task 1, expand the game. 
#If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        action == "cross a river"
        print("You found a boat!")
else:
    place = "cave"
    act2 = input("do you want to light a torch, or proceed in the dark")
    print("You find a hidden treasure!")
    if act2 == "light a torch":
        print("It's Bright")
    else:
        act2 == "proceed in the dark"
        print("Night Time.")
#Task 3: Default Path
#If the user makes an invalid choice at any point, incorporate a pass statement to handle it. 
# HINT: How can an else statement be of use here?
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
else:
    place = "cave"
    act2 = input("do you want to light a torch, or proceed in the dark")
    print("You find a hidden treasure!")
    if act2 == "light a torch":
        print("It's Bright")
    elif act2 == "proceed in the dark":
        print("Night Time.")
    else:
        pass
#2. Quick Decisions: The Event Planner
#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
attendees = input("Enter number of attendees: ")
venue = "large hall" 
if attendees > 100:
    print("Its a" + venue)
else:
    print("Its a small conference room")
    
#Task 2: Venue Selection
#Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector"
#based on the number of attendees.
attendees = input("Enter number of attendees: ")
venue = "large hall" 
if attendees > 100:
    print("Its a" + venue +" I would recomend an audiosystem")
else:
    print("Its a small conference room I would recomend a projector")
#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
meal = input("Would you like want vegetarian food?")
if meal == "yes":
    print("Recommend Veggie Delight Caterers")
else:
    print("We recomend Gourmet Meals Caterers") 
