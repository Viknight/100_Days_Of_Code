print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() +name2.lower()

# score = 0
# score_true_name1 = 0
# score_true_name2 = 0
# score_love_name1 = 0
# score_love_name2 = 0

# for i in name1_lower:
# 	if i == "t" or i == "r" or i == "u" or i == "e": #or i == "l" or i == "o" or i == "v" or i == "e":
# 		score_true_name1 += 1

# for j in name2_lower:
# 	if j == "t" or j == "r" or j == "u" or j == "e": #or i == "l" or i == "o" or i == "v" or i == "e":
# 		score_true_name2 += 1


# for k in name1_lower:
# 	if k == "l" or k == "o" or k == "v" or k == "e":
# 		score_love_name1 += 1

# for l in name2_lower:
# 	if l == "l" or l == "o" or l == "v" or l == "e":
# 		score_love_name2 += 1


t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")

l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")

true = t+r+u+e
love = l+o+v+e
score = str(true) + str(love)
score = int(score)

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")