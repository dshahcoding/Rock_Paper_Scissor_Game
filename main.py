import random

print("Welcome to the STONE,PAPER,SCISSOR game...")

game_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your choice = Rock , Paper , Scissor = ")
com_choice = random.choice(game_list)

print(f"User choice = {user_choice} and Computer choice = {com_choice}")

if user_choice == com_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if com_choice=="Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if com_choice=="Rock":
        print("Paper covers Rock = You win")
    else:
        print("Scissor cuts Paper = Computer win")

elif user_choice == "Scissor":
    if com_choice=="Paper":
        print("Scissor cuts Paper = You win")
    else:
        print("Rock smashes Scissor = Computer win")


print("\nGAME END SUCCESSFULLY...")
