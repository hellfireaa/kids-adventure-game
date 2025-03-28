from flask import Flask, request, render_template_string

app = Flask(__name__)

# Game state variables
game_state = {
    "scene": "introduction"
}

# Define scenes
def introduction():
    print("Welcome to the Kids Learning Adventure Game!")
    print("You find yourself on a secluded beach, but you have lost your memory and don't know how you got there. "
    "Your goal is to survive until help arrives!")
    print("Make your choices wisely!\n")

def forest_scene():
    print("On the beach, you see two items, but you can only carry one of them. "
    "The first item is a bottle filled with clean water, and the second item is a rope. Which one do you take?")
    print("1. Take the bottle of water.")
    print("2. Take the rope.")
    choice = input("What do you do? (1/2): ")
    if choice == "1":
        cave_not_thirsty_scene()
    elif choice == "2":
        river_scene()
    else:
        print("Invalid choice. Try again.")
        forest_scene()

def cave_not_thirsty_scene():
    print("You grab the bottle of water and start walking along the beach. You see a cave up ahead.")
    print("You enter the cave and see a small opening at the back. "
    "Do you go through the opening or stay in the cave?") 
    choice = input("What do you do? (1/2): ")
    if choice == "1":
        opening_cave_scene()
    elif choice == "2":
        stay_cave_scene()
    else:
        print("Invalid choice. Try again.")
        forest_scene()

def opening_cave_scene():
    print("The small opening in the back of the cave is just big enough for you to squeeze through. It leads to a hidden path."
    "There is writing on the wall with a riddle you must solve to continue.")
    print("The riddle reads: 'Which one of these words is spelled correctly?'")
    print("1. Acommodate")
    print("2. Accommodate")
    print("3. Acomodate")
    choice = input("What option do you choose? (1/2/3): ")
    if choice == "1":
        end_scene()
    elif choice == "2":
        fairy_scene()
    elif choice == "3":
        end_scene()
    else:
        print("Invalid choice. Try again.")
        opening_cave_scene()

def stay_cave_scene():
    print("You decide it will be safer to stay in the cave. You find a comfortable spot to rest and fall asleep.")
    print("You wake up because you are cold. What items should you look for to build a fire?")
    print("1. Sticks and stones.")
    print("2. Water and leaves.")
    choice = input("What do you do? (1/2): ")
    if choice == "1":
        happy_end_scene()
    elif choice == "2":
        end_scene()
    else:
        print("Invalid choice. Try again.")
        stay_cave_scene()

def river_scene():
    print("The sun is very strong and there is no shelter on the beach. You decide to follow the river to find shade.")
    print("Up ahead, there is an old man sitting by the river. He offers you a ride on his boat if you can answer his question correctly.")
    print("What is 46 + 27?")
    choice = input("What is your answer?: ")
    if choice == "73":
        happy_end_scene()
    else:
        print("Incorrect answer. The old man leaves you behind.")
        end_scene()

def happy_end_scene():
    print("You find a large house made of candy and chocolate. There is no scary witches that live here, it is empty.""You decide to stay a while and eat some of the candy.")
    print("Congratulations! You have reached the happy ending of the game. You have survived and found a safe place to stay until help arrives.")
    print("Thank you for playing the Kids Learning Adventure Game!")

def end_scene():
    print("You become increasingly cold and hungry. You run out of fresh water. You are too weak to continue and succumb to the elements.")
    print("You have reached the end of the game. Thank you for playing the Kids Learning Adventure Game!")

def fairy_scene():
    print("The wall opens up to reveal a hidden path. You follow the path and find a fairy who offers to help you.")
    print("The fairy gives you a magic potion that will help you find your way home. You drink the potion and suddenly remember everything.")
    print("Congratulations! You have reached the happy ending of the game. You have survived and found a way to get home.")
    print("Thank you for playing the Kids Learning Adventure Game!")

def main():
    introduction()
    forest_scene()

if __name__ == "__main__":
    app.run(debug=True)