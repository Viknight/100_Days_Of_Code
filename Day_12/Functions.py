################### Scope ####################

enemies = 1

#modify a global variable 

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


pi = 3.14159246