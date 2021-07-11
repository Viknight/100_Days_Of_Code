<<<<<<< HEAD
year = int(input("Which year do you want to check? "))

#Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
=======
year = int(input("Which year do you want to check? "))

#Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
>>>>>>> 19121e03e7058d9c9c3111deb40dd08e76c21791
  print("Not leap year.")