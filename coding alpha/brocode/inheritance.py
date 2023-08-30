"""
class Animal: 
    def __init__(self, name):
        pass
import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y : x+y , letters)
print(word)

def hello(variables):
    return sum(variables)
print(hello([1,2,3,4,5]))
if __name__ =="__main__":
    print(__name__)
"""
 
unknown_land = "heaven"
guess = ""
count = 0
limit = 4
out_of_guesses = False
while guess != unknown_land and not(out_of_guesses):
    if count < limit:
        guess = input("Enter guess: ")
        count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose. The correct answer was " + unknown_land + ".")
else:
    print("You win! Congratulations!")


   


print("you win")