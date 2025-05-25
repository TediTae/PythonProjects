import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_game = ["rock", "paper", "scissors"]

choice_of_computer = random.choice(list_of_game)

players_choice = int(input("Pick one of the numbers: 1 for ROCK, 2 for PAPER, 3 for SCISSORS\n"))

if choice_of_computer == "rock" and players_choice == 1:
    print("YOUR CHOICE :")
    print(rock)
    print("COMPUTER'S CHOICE :")
    print(rock)
    print("ITS A DRAW !!")

elif choice_of_computer == "paper" and players_choice == 2:
    print("YOUR CHOICE :")
    print(paper)
    print("COMPUTER'S CHOICE :")
    print(paper)
    print("ITS A DRAW !!")

elif choice_of_computer == "scissors" and players_choice == 3:
    print("YOUR CHOICE :")
    print(scissors)
    print("COMPUTER'S CHOICE :")
    print(scissors)
    print("ITS A DRAW !!")

elif choice_of_computer == "rock" and players_choice == 3:
    print("YOUR CHOICE :")
    print(scissors)
    print("COMPUTER'S CHOICE :")
    print(rock)
    print("COMPUTER WINS !!")

elif choice_of_computer == "paper" and players_choice == 1:
    print("YOUR CHOICE :")
    print(rock)
    print("COMPUTER'S CHOICE :")
    print(paper)
    print("COMPUTER WINS !!")

elif choice_of_computer == "scissors" and players_choice == 2:
    print("YOUR CHOICE :")
    print(paper)
    print("COMPUTER'S CHOICE :")
    print(scissors)
    print("COMPUTER WINS !!")

elif choice_of_computer == "rock" and players_choice == 2:
    print("YOUR CHOICE :")
    print(paper)
    print("COMPUTER'S CHOICE :")
    print(rock)
    print("YOU WIN !!")

elif choice_of_computer == "paper" and players_choice == 3:
    print("YOUR CHOICE :")
    print(scissors)
    print("COMPUTER'S CHOICE :")
    print(paper)
    print("YOU WIN !!")

elif choice_of_computer == "scissors" and players_choice == 1:
    print("YOUR CHOICE :")
    print(rock)
    print("COMPUTER'S CHOICE :")
    print(scissors)
    print("YOU WIN !!")
else:
    print("You chose a invalid number. YOU LOSE !!")
