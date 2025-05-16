# Implementing coffee machine using Python
import Menu,CoffeeMaker,MoneyMachine,os
coffee_machine=True
ob1=CoffeeMaker.CoffeeMaker()
ob2=Menu.Menu()
ob3=MoneyMachine.MoneyMachine()
while coffee_machine==True:
    if ob1.is_resource_sufficient(ob2.find_drink('espresso'))==False:
        break
    print(ob2.get_items())
    choice=input("Type your choice: ").lower()
    if choice=="report":
        ob1.report()
        ob3.report()
    elif choice=='off':
        print("Maqchine turning off...")
        break
    elif choice!='espresso' and choice!='latte' and choice!='cappuccino':
        print("Please enter correct choice of drinks")
    else:
        beverage=ob2.find_drink(choice)
        resources=ob1.is_resource_sufficient(beverage)
        if resources==True:
            if ob3.make_payment(beverage.cost)==True:
                ob1.make_coffee(beverage)
        else:
            print("Sorry, this drink can not be prepared due to insufficient resources. Please type another drink")
print("MACHINE IS OFF NOW. REGRET FOR INCONVENIENCE CAUSED")