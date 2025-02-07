# Snake Water Gun Game
import random

print("Snake, Water, Gun Game")
print("Enter your choice: \n1. Snake\n2. Water\n3. Gun")

user = int(input("Enter your choice: "))
comp = random.randint(1, 3)

if user == 1:
    user_choice = 'Snake'   
elif user == 2:
    user_choice = 'Water'
elif user == 3:
    user_choice = 'Gun'
    
if comp == 1:
    comp_choice = 'Snake'   
elif comp == 2:
    comp_choice = 'Water'
elif comp == 3:
    comp_choice = 'Gun'
    
print("Your choice: ", user_choice)
print("Computer's choice: ", comp_choice)

if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice == 'Snake' and comp_choice == 'Water':
    print("You win!")
elif user_choice == 'Water' and comp_choice == 'Gun':
    print("You win!")
elif user_choice == 'Gun' and comp_choice == 'Snake':
    print("You win!")
else:
    print("Computer wins!")     
    