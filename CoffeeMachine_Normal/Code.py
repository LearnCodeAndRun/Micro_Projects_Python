# Making a coffee machine using Python
import Data_For_Coffee
def show_report():
    print(f"Coffee: {Data_For_Coffee.initial['Coffee']}g")
    print(f"Water: {Data_For_Coffee.initial['Water']}ml")
    print(f"Milk: {Data_For_Coffee.initial['Milk']}ml")
    print(f"Money: ${Data_For_Coffee.initial['Money']}")
def make_espresso():
    if Data_For_Coffee.initial["Water"]>=Data_For_Coffee.data["espresso"]["Water"]:
        if Data_For_Coffee.initial["Coffee"]>=Data_For_Coffee.data["espresso"]["Coffee"]:
          quarters=float(input("Enter quarters: "))
          dimes=float(input("Enter dimes: "))
          nickels=float(input("Enter nickels: "))
          pennies=float(input("Enter pennies: "))
          payment=0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies
          if payment>=Data_For_Coffee.data["espresso"]["Cost"]:
              if payment-Data_For_Coffee.data["espresso"]["Cost"]>0:
                  print(f"Payment received. Here's your change: ${round(payment-Data_For_Coffee.data['espresso']['Cost'],2)}")
              print("Here's your espresso... Enjoy! 😊")
              Data_For_Coffee.initial["Coffee"]-=Data_For_Coffee.data["espresso"]["Coffee"]
              Data_For_Coffee.initial["Water"]-=Data_For_Coffee.data["espresso"]["Water"]
              Data_For_Coffee.initial["Money"]+=Data_For_Coffee.data["espresso"]["Cost"]
          else:
              print(f"Not enough money. Money refunded: ${round(payment,2)}")
        else:
            print("Not enough coffee")
    else:
        print("Not enough water")
def make_cappuccino():
    if Data_For_Coffee.initial["Water"]>=Data_For_Coffee.data["Cappuccino"]["Water"]:
        if Data_For_Coffee.initial["Coffee"]>=Data_For_Coffee.data["Cappuccino"]["Coffee"]:
          if Data_For_Coffee.initial["Milk"]>=Data_For_Coffee.data["Cappuccino"]["Milk"]:
            quarters=float(input("Enter quarters: "))
            dimes=float(input("Enter dimes: "))
            nickels=float(input("Enter nickels: "))
            pennies=float(input("Enter pennies: "))
            payment=0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies
            if payment>=Data_For_Coffee.data["Cappuccino"]["Cost"]:
              if payment-Data_For_Coffee.data["Cappuccino"]["Cost"]>0:
                  print(f"Payment received. Here's your change: ${round(payment-Data_For_Coffee.data['Cappuccino']['Cost'],2)}")
              print("Here's your cappuccino... Enjoy! 😊")
              Data_For_Coffee.initial["Coffee"]-=Data_For_Coffee.data["Cappuccino"]["Coffee"]
              Data_For_Coffee.initial["Water"]-=Data_For_Coffee.data["Cappuccino"]["Water"]
              Data_For_Coffee.initial["Milk"]-=Data_For_Coffee.data["Cappuccino"]["Milk"]
              Data_For_Coffee.initial["Money"]+=Data_For_Coffee.data["Cappuccino"]["Cost"]
            else:
              print(f"Not enough money. Money refunded: ${round(payment,2)}")
          else:
            print("Not enough milk")
        else:
            print("Not enough coffee")
    else:
        print("Not enough water")
def make_latte():
    if Data_For_Coffee.initial["Water"]>=Data_For_Coffee.data["latte"]["Water"]:
        if Data_For_Coffee.initial["Coffee"]>=Data_For_Coffee.data["latte"]["Coffee"]:
          if Data_For_Coffee.initial["Milk"]>=Data_For_Coffee.data["latte"]["Milk"]:
            quarters=float(input("Enter quarters: "))
            dimes=float(input("Enter dimes: "))
            nickels=float(input("Enter nickels: "))
            pennies=float(input("Enter pennies: "))
            payment=0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies
            if payment>=Data_For_Coffee.data["latte"]["Cost"]:
              if payment-Data_For_Coffee.data["latte"]["Cost"]>0:
                  print(f"Payment received. Here's your change: ${round(payment-Data_For_Coffee.data['latte']['Cost'],2)}")
              print("Here's your latte... Enjoy! 😊")
              Data_For_Coffee.initial["Coffee"]-=Data_For_Coffee.data["latte"]["Coffee"]
              Data_For_Coffee.initial["Water"]-=Data_For_Coffee.data["latte"]["Water"]
              Data_For_Coffee.initial["Milk"]-=Data_For_Coffee.data["latte"]["Milk"]
              Data_For_Coffee.initial["Money"]+=Data_For_Coffee.data["latte"]["Cost"]
            else:
              print(f"Not enough money. Money refunded: ${round(payment,2)}")
          else:
            print("Not enough milk")
        else:
            print("Not enough coffee")
    else:
        print("Not enough water")
choice="on"
while choice!="off" and Data_For_Coffee.initial["Water"]>=50 and Data_For_Coffee.initial["Coffee"]>=18:
    print("Welcome to the Coffee Machine ! ☕")
    choice=input("What do you want ? Type (espresso / cappuccino/ latte): ").lower()
    if choice=='report':
        show_report()
    elif choice=='espresso':
        make_espresso()
    elif choice=='cappuccino':
        make_cappuccino()
    elif choice=='latte':
        make_latte()
    elif choice=='off':
       break
    else:
        print("Invalid choice. Please enter correct choice")
print("Machine turned off... Please come again later. Sorry for the inconvenience caused 😔")
