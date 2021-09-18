############DEBUGGING#####################

# #Describe Problem
# def my_function():
#   for i in range(1, 20+1):    #To iterate over values from 1 to 20 excluding 20 with variable i in local scope
#     if i = 20:             #Checks if the value of i equals to 20
#       print("You got it")   #print a statement when i equals to 20
# my_function()               #A function where no parameter is passed

# # Reproduce the Bug
# from random import randint    #randpm library imported
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]    #list declared iterating 0 to 5
# dice_num = randint(1, 6)      #randint used to choose random integer between 1 to 6 both inclusive
# print(dice_imgs[dice_num])    #prints previous variable

# # Play Computer
# year = int(input("What's your year of birth?"))     #takes int input
# if year > 1980 and year < 1994:         #compares with already provided integer years
#   print("You are a millenial.")         #prints   
# elif year > 1994:                      
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])