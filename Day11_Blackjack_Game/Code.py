# Creating a game of blackjack
import random
import os
from BlackJackLogo import logo
def deal_cards():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)
def calculate_score(cards_list):
  return sum(cards_list)
choice='y'
while True:
  choice=input("Do you want to play a game of Blackjack ? Type \'y\' or \'n\': ").lower()
  if choice=='n' or choice!='y':
    break
  os.system("clear")
  print(logo)
  user_cards=[]
  computer_cards=[]
  computer_cards.extend([deal_cards(),deal_cards()])
  while calculate_score(computer_cards)<17:
    computer_cards.append(deal_cards())
    if 11 in computer_cards and calculate_score(computer_cards)>21:
      computer_cards.remove(11)
      computer_cards.append(1)
  user_cards.append(deal_cards())
  while choice=='y':
    user_cards.append(deal_cards())
    if 11 in user_cards and calculate_score(user_cards)>21:
      user_cards.remove(11)
      user_cards.append(1)
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    if calculate_score(user_cards)>21:
      break
    choice=input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
  sum1=calculate_score(computer_cards)
  sum2=calculate_score(user_cards)
  print(f"Your final hand: {user_cards}, final score: {sum2}")
  print(f"Computer's final hand: {computer_cards}, final score: {sum1}")
  if sum1==21 and sum2<sum1:
    print("Computer got a blackjack! You lose")
  elif sum2==21:
    print("Blackjack! Congratulations, you won!")
  elif sum1<sum2<=21:
    print("Congratulations, you won")
  elif sum2<sum1<=21:
    print("Computer won. You lose")
  elif sum1==sum2 and sum2<=21:
    print("Draw")
  elif sum2>21:
    print("You went over. You lose")
  elif sum1>21:
    print("Computer went over. You won")
  else:
    print("None won, it is a draw")
