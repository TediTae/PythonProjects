###################VERSION ONE####################################

import random
from art import logo

print(logo)
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")
print("Easy Level : 10 Attempts")
print("Hard Level : 5 Attempts")
difficulty_type = input("Choose a difficulty type: 'easy' or 'hard'.").lower()
life = 10
game_over = False

if difficulty_type == "hard":
    life = 5


def random_number_generator():
    number_to_guess = random.randint(1,100)
    return number_to_guess

computer_choice = random_number_generator()
# print(f"Computer choice is {computer_choice}")

def compare(num, num_to_guess):
    global life
    global game_over
    if num == num_to_guess:
        print("You guessed it right!! YOU WIN!! 🤩")
        game_over = True
    elif num > num_to_guess:
        life -= 1
        if life == 0:
            game_over = True
            print("You are out of your attempts GAME OVER ! ☠️☠️😭")
            print(f"The number was {computer_choice}")
        else:
            print("Too high! Try a lower number.")
            print(f"You have {life} attempts to guess the number.")
    elif num < num_to_guess:
        life -= 1
        if life == 0:
            game_over = True
            print("You are out of your attempts GAME OVER ! ☠️☠️😭")
            print(f"The number was {computer_choice}")

        else:
            print("Too low! Try a higher number.")
            print(f"You have {life} attempts to guess the number.")


while not game_over:
    players_guess = int(input("Make your guess: "))
    compare(players_guess, computer_choice)


###########################VERSION TWO################################################


# from random import randint
# from art import logo


# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5


# # Function to check users' guess against actual answer
# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}")


# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS


# def game():
#     print(logo)
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")

#     turns = set_difficulty()

#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         # Let the user guess a number
#         guess = int(input("Make a guess: "))
#         # Track the number of turns and reduce by 1 if they get it wrong
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")




# game()


