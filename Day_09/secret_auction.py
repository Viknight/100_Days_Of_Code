from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

people_remain = True
bidders_data = []

def find_highest_bidder():
  max_bid = 0
  for i in bidders_data:
    dict = i
    if dict["bid"] > max_bid:
      max_bid = dict["bid"] 
      max_bidder_name = dict["name"]
  print(f"{max_bidder_name} has won.")
   

while people_remain:
  name = input("What is your name?")
  bid = int(input("Place your bid: "))

  bidder = {"name": name, "bid":  bid}
  bidders_data.append(bidder)

  query = input("Are there any more bidders? type 'yes' or 'no'")

  if query == "yes":
    clear()
  elif query == "no":
    people_remain = False

find_highest_bidder()
