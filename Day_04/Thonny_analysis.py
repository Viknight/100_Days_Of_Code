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

user_bet = input('Choose your bet. "Rock" "Paper" or "Scissors"').lower()
print(f'\n Your Choice: {user_bet} \n')

if user_bet == "rock":
  print(rock)
elif user_bet == "paper":
  print(paper)
elif user_bet == "scissors":
  print(scissors)
else:
  print('Invalid Choice')