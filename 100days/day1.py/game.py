import random
rock = "✊"
paper = "✋"
scissors = "✌️"
#print(f"{rock}\n{paper}\n{scissors}")

images = [rock, paper, scissors]

user_choice = int(input("type 0 for rock, 1 for paper, 2 for scissors: "))
if user_choice >= 3 or user_choice < 0:
    print("invalid input")
else:
    print(images[user_choice])
    
    computer_choice = random.randint(0,2)
    print("computer chose: ") 
    print(images[computer_choice])
    if computer_choice == user_choice:
        print("Draw.")
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
        print("You lose!")
    else:
        print("You win!")
        
