#Banker roulette

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)

index = random.randint(0,len(names)-1
)

payee = names[index]

print(f"{payee} is going to buy the meal today")
