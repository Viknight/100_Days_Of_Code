from art import logo, vs
from game_data import data
import random
from replit import clear

# Printing the logo
print(logo)

#Initilizing a variable for recurrsion of game
game_ends = False

#Initilizing a variable score for score
score = 0

# Choosing a random entity from the dataset given
def new_random_entity():
  """
  This function will pick a random entity list from the dataset given
  """
  return random.choice(data)


#Declaring and initializing two variables with entites
random_entity_A = new_random_entity()
random_entity_B = new_random_entity()


def print_an_entity(random_entity, AorB):
  """
  This function takes 2 arguments, first one is a list of details of entity while the second one is just to declare whether the entity is for variable A or B. This function will print the variables of the entity which is a list
  """
  print(f"Compare {AorB}: {random_entity['name']}, a {random_entity['description']}, from {random_entity['country']} with {random_entity['follower_count']}")

def display_options():
  """
  This function will print both the entities on the same screen along with the ascii art 
  """

  print_an_entity(random_entity_A, 'A')  
  print(vs)
  print_an_entity(random_entity_B, 'B') 

while not game_ends:
  
  display_options()

  #variable along with ternary operator to determine which entity has more followers (A or B)
  most_followed = 'A' if (random_entity_A['follower_count']) >= (random_entity_B['follower_count']) else 'B'

  #user input to store the guess made
  user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  clear()
  print(logo)
  # comparing the user guess with the actuality
  if user_guess == most_followed:
    
    score+=1
    print(f"You're right! Current score: {score}")

    random_entity_A = random_entity_B
    random_entity_B = new_random_entity()

  else:
    game_ends = True
    print(f"Wrong, game ends, final score: {score}")

  
    
  



