print('\n Welcome to Python Pizza!')

size = input("What size pizza do you want? S, M, or L ")

Bill = 0

if size == 's':
	Bill += 15
elif size == 'm':
	Bill += 20
elif size == "l":
	Bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N ")

if add_pepperoni == 'y':
	if size == 's':
		Bill += 2
	else:
		Bill += 3
        
        
extra_cheese = input("Do you want extra cheese? Y or N ")

if extra_cheese == 'Y':
	Bill += 1

print(f"Your total bill amount is ${Bill}.")