#dictionary comprehension creates dictionary using an expression(replaces lambda and for loops)
#dictionary = {key: expression for (key,value) in iterables}

# cities_in_Europe = {'warsaw': 5 , 'Berlin': 3 , 'Kiev': 6, 'Amsterdam': 6}
# cities_in_C = {key: round((value*9/5)+32) for (key,value) in cities_in_Europe.items()}
# print(cities_in_C)

# cities_in_Europe = {'warsaw': 5 , 'Berlin': 3 , 'Kiev': 6, 'Amsterdam': 6}
# cities_in_F = {key: round((value*9/5)+32) for (key,value) in cities_in_Europe.items()}
# print(cities_i
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        i = 0
        j = 0
        for ele in range(len(self.ingredients) and len(self.toppings)):
              
            list = [self.ingredients[i], self.toppings[j]]
            i += 1
            j += 1
        return list
if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]