#This is a program to create the classic rock paper and scissors game using python
#I've designed this program for a single match of rock paper scissors
import random
random_num=random.randint(0,2)
print('''
Rock
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
\n''')
print('''
Paper
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
\n''')
print('''
Scissors
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
\n''')
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")) # This is the prompt for the users input 
options = ['''Rock
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      ''', 
      '''
Paper
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)]
    ''',
    '''
Scissors
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
      '''] # Rock, paper and scissors are stored as strings inside a list and is pulled out using list index whenever required
if   choice == 0 and random_num == 1:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("You lost! Better luck next time...\n")
elif choice == 0 and random_num == 2:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("You won! Congratulations...\n")
elif choice == 1 and random_num == 0:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("You won! Congratulations...\n")
elif choice == 1 and random_num == 2:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("You lost! Better luck next time...\n")
elif choice == 2 and random_num == 0:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("You lost! Better luck next time...\n")
elif choice == 2 and random_num == 1:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("You won! Congratulations...\n")
elif choice == random_num:
    print("You chose:\n"+options[choice]+"\n")
    print("Computer chose:\n"+options[random_num]+"\n")
    print("Same choice! Draw game...")
else: 
    print("Invalid choice! Only input numbers from 0 to 2.")
    
      