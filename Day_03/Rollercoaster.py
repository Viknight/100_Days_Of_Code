<<<<<<< HEAD
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

Bill = 0

if (height > 120):

	Age = int(input('What is your age?'))
	if Age < 12:
		Bill+=5
		print('Child tickets are $5')

	elif Age <= 18:
		Bill += 7
		print('Teen Tickets are $7')
        
	else:
		Bill += 12
		print('Adult Tickets are $12')
        

	want_photos = input("Do you want photos as well? (Y/N)")

	if want_photos == 'y' or want_photos == "Y":
		Bill  += 3

	print(f"Total bill amount is ${Bill}.")

else:
=======
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if (height > 120):
	Age = int(input('What is your age?'))
	if Age > 18:
		print('Please pay 12$')
	else:
		print('Please pay 7$')
  print('You can go ahead and enjoy your ride')
else:
>>>>>>> 19121e03e7058d9c9c3111deb40dd08e76c21791
  print('Sorry, you cannot proceed')