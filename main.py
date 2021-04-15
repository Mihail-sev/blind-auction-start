from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print (logo)
print("Welcome to  the private auction!")

member = {}
new_member = True

def new_auctionist ():
  name = input("What is your name?\n")
  bet = int(input("How much do you bet?\n"))
  member[name] = bet

def winner():
  max_bet = 0
  winner = {}
  s =""
  for human in member:
    if member[human] > max_bet:
      max_bet = member[human]
      winner = human
    elif member[human] == max_bet:
      winner += " and "+human
      s = "s"
  print (f"\nAnd winner{s} of our auction is {winner} with bet equal ${max_bet}")    
  
while  new_member:
  new_auctionist()
  add_new_member = input ("Are the more auctionist?\n Write 'yes' or 'no'\n ").lower()
  if add_new_member == "no":
    new_member = False
  clear ()
winner()