class MenuItem:
    def __init__(self,name,cost,water,milk,coffee,):
        self.name=name
        self.cost=cost
        self.ingredients={"water":water,"milk":milk,"coffee":coffee}
class Menu:
    def __init__(self):
        self.menu=[MenuItem("espresso",1.5,50,0,18),
                   MenuItem("latte",2.5,200,150,24),
                   MenuItem("cappuccino",3,250,50,24)]
    def get_items(self):
        options=[]
        for item in self.menu:
            options.append(item.name)
            options.append("/")
        del options[len(options)-1]
        choice=""
        for i in options:
            choice+=i
        return choice 
    def find_drink(self,order_name):
        for item in self.menu:
            if item.name==order_name:
                return item
        return None
    
