# Making a number guessing game in python
import random
lst=[i for i in range(1,101)]
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
choice=input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
actual_number=random.choice(lst)
flag=0
if choice=='easy':
    for i in range(10,0,-1):
     print(f"You have {i} attempts to guess the number")
     chosen_number=int(input("Make a guess: "))
     if chosen_number<actual_number:
        print("Too low\nGuess again")
     elif chosen_number>actual_number:
        print("Too high\nGuess again")
     else:
        print(f"You got it! The answer was {actual_number}")
        flag=1
        break
    if flag==0:
      print("You have run out of guesses, you lose")
elif choice=='hard':
   for i in range(5,0,-1):
     print(f"You have {i} attempts to guess the number")
     chosen_number=int(input("Make a guess: "))
     if chosen_number<actual_number:
        print("Too low\nGuess again")
     elif chosen_number>actual_number:
        print("Too high\nGuess again")
     else:
        print(f"You got it! The answer was {actual_number}")
        flag=1
        break
   if flag==0:
    print("You have run out of guesses, you lose")
else:
   print("Invalid choice")
