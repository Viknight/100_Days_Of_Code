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
print(f'\n Your Choice: {user_bet}')

if user_bet == "rock":
  print(rock)
elif user_bet == "paper":
  print(paper)
elif user_bet == "scissors":
  print(scissors)
else:
  print('Invalid Choice')

Bets = ["rock", "paper", "scissors"]

comp_bet = random.randint(0,len(Bets)-1)

if comp_bet == 0:
  comp_bet = "rock"
  print(f'\nThe computer chose Rock {rock}')
elif comp_bet == 1:
  comp_bet = "paper"
  print(f'\nThe computer chose Paper{paper}')
else:
  comp_bet = "scissors"
  print(f'\nThe computer chose Scissors {scissors}')

if user_bet == "rock":
  if comp_bet == "scissors":
    print('You Win!!')
  elif comp_bet == "rock":
    print('It is a tie.')
  else:
    print('You Loose.')
elif user_bet == "paper":
  if comp_bet == "rock":
    print('You Win!!')
  elif comp_bet == "paper":
    print('It is a tie.')
  else:
    print('You Loose.')
else:
  if comp_bet == "paper":
    print('You Win!!')
  elif comp_bet == "scissors":
    print('It is a tie.')
  else:
    print('You Loose.')

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.