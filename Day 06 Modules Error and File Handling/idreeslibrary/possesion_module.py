# classes
class Possesions:
    def __init__(self, type, value, age, action):
        self.type = type
        self.value = value
        self.age = age
        self.action = action

    def get_activity(self): # getter method
        print(f"I do {self.action} on this {self.type}")

    def get_value(self): # getter 
        print(f"I got this {self.type} for {self.value}")

    def set_value(self, new_value): # setter method
        self.value = new_value
        print(f"value updated to {self.value}")


class Electronics(Possesions):
    # track battery percentage
    def __init__(self, type, value, age, action, battery):
        self.battery = battery
        super().__init__(type, value, age, action)

class Vehicles(Possesions):
    # mileage
    pass

class Home(Possesions):
    # how many days in a year
    pass



# functions
def new_function(x,y):
    return (x*y + 2*x)

def sum(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def div(x,y):
    return x / y


# attributes saved
idrees = 121451
pi = 6.14323
