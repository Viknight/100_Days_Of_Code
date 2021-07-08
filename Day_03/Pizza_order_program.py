print('\n Welcome to Python Pizza!')
size = int(input('What size pizza do you want? \n\n1. Small \n2. Medium\n3. Large\n'))
Bill = 0

if size == '1':
	Bill += 15
elif size == '2':
	Bill += 20
elif size == "3":
	Bill += 25

print(Bill)


add_pepperoni = input('What you want pepporoni added?  \n1. Yes \n2.No ')

if add_pepperoni == '1':
	if size == '1':
		Bill += 2
	else:
		Bill += 3

extra_cheese = input('Do you want extra cheeeeeeeeeese?  \n1. Yes \n2.No ')

if extra_cheese == 'Y':
	Bill += 1

# name = input('What is your name?')
# if name == 'AARADHYA':
# 	Bill = 0

print('Your total Bill amount is ' +str(Bill) +' \nEnjoy your Pizza!')
