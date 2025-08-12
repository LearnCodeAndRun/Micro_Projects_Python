# Creating a higher - lower game using python
import Logo
import os
import Data
import random
def check_answer(choice,index1,index2):
  if choice=='A':
    if Data.data[index1]['follower_count']>Data.data[index2]['follower_count']:
      return True
    return False
  elif choice=='B':
     if Data.data[index1]['follower_count']<Data.data[index2]['follower_count']:
       return True
     return False
  else:
    return False
ans=True
lst=[False for i in range(0,len(Data.data))]
score=0
index1=-1
index2=-1
while ans:
  if index1==-1 and index2==-1:
    index1=random.randint(0,len(Data.data)-1)
    lst[index1]=True
    print(Logo.logo)
  else:
    index1=index2
    os.system("clear")
    print(Logo.logo)
    print(f"You're right ! Current score: {score}")
  print(f"Compare A: {Data.data[index1]['name']}, a {Data.data[index1]['description']}, from {Data.data[index1]['country']}")
  print(Logo.vs)
  while lst[index2]==True:
    index2=random.randint(0,len(Data.data)-1)
  lst[index2]=True
  print(f"Against B: {Data.data[index2]['name']}, a {Data.data[index2]['description']} from {Data.data[index2]['country']}")
  ch=input("Who has more followers ? Type \'A\' or \'B\':  ").upper()
  ans=check_answer(ch,index1,index2)
  if ans==True:
    score+=1
  else:
    os.system("clear")
    print(Logo.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
