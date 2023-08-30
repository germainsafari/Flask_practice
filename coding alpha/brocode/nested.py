#Nested loops: The inner loop will finish all of it's iterations before 
# finishing one iteration of the outer loop
rows = int(input("how many rows?"))
columns = int(input("how many columns?"))
symbol = input("what is the integer")

for i in range(rows): 
    for j in range(columns):
        print(symbol, end="")
    print()
#Python interpreter sets "special variables", one of which is __name__
#Python will assign the __name__ variable a value of "__main__" if it's 
#the initial value being run