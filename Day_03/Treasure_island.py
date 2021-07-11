<<<<<<< HEAD
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

level_1 = input(' \n\n You have come to a cross road. Were do you want to go? Type "left" or "right"').lower()

if level_1 == 'left':

	level_2 = input('You have arrived at a river? Do you want to swim or wait? Type "swim" or "wait"').lower()
	if level_2 == "wait":

		level_3 = input('Now you are at a place with 3 doors Red, Blue and Yellow. Choose one. Type "red" or "blue" or "yellow"').lower()
		if level_3 == "yellow":
			print("Hooray!! You have won the Treasure!!.")
		elif level_3 == "red":
			print("Fire! Fire! Fire! You had nowhere to go. GAME OVER.")
		else:
			print("You tried your best but the beast got the best of you. GAME OVER.")

	else:
		print("An alligator made you his meal. GAME OVER.")

else:
	print("Unlucky 0.0 You fell into a ditch. GAME OVER.")



=======
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

level_1 = input(' \n\n You have come to a cross road. Were do you want to go? Type "left" or "right"').lower()

if level_1 == 'left':

	level_2 = input('You have arrived at a river? Do you want to swim or wait? Type "swim" or "wait"').lower()
	if level_2 == "wait":

		level_3 = input('Now you are at a place with 3 doors Red, Blue and Yellow. Choose one. Type "red" or "blue" or "yellow"').lower()
		if level_3 == "yellow":
			print("Hooray!! You have won the Treasure!!.")
		elif level_3 == "red":
			print("Fire! Fire! Fire! You had nowhere to go. GAME OVER.")
		else:
			print("You tried your best but the beast got the best of you. GAME OVER.")

	else:
		print("An alligator made you his meal. GAME OVER.")

else:
	print("Unlucky 0.0 You fell into a ditch. GAME OVER.")



>>>>>>> 19121e03e7058d9c9c3111deb40dd08e76c21791
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload