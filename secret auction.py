#initiators
from replit import clear
from art import auction_logo
print(auction_logo,"\n")
print("Welcome to the secret auction program.\n")
data_dict = {}
again = "yes"
#repetitive
while again=="yes":
  person = input("Whats your name?:")
  bid = input("Whats your bid?")
  data_dict[person] = bid
  again = input("Are there any other bidders? Yes or No:")
  clear()
#conclusion
winner = max(data_dict)
print(f"The winner is {winner} with a bid of {data_dict[winner]}")