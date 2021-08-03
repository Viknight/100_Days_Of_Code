#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

actual_number = random.randint(0,100)
turns_left = 0

def game():
  print(f"""
  Welcome to the number guessing game!
  I'm thinking of a number between 1 and 100.
  Pssst, the correct number is {actual_number}.
  """)

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if difficulty == "hard":
    turns_left = 5 
  elif difficulty == "easy":
    turns_left = 10


  while turns_left != 0:
    print(f"You have {turns_left} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    
    if guess == actual_number:
      print(f"You got it! The answer was {actual_number}")
      return
    else:
      if guess > actual_number:
        print("Too High.")
      else:
        print("Too Low.")

    turns_left -= 1
    if turns_left == 0:
      print(f"You lose. Have run out of guesses. {actual_number} was the number")
      return
    print("Guess again.")

game()