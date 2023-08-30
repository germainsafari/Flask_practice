operator = input("enter the operator")
n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))


def add(n1, n2):
    if (operator == "+" ):
        return n1 + n2
    elif (operator == "-"):
        return n1 - n2

    elif (operator == "*"):
        return n1 * n2
    else:
        return "invalid"
print(add(n1, n2))
    

    