# Alright so this is a very basic treasure hunting game I created as a beginner in python programming 

print ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# The choice variables (choice1,choice2,choice3) are the user's inputs as to the choice they make
#The choice made by them is compared using nested if statements and the corresponding results are printed
print("Welcome to treasure Island\n")
print("Your mission is to find the treasure!\n")
choice1=input("Where do you want to go? left or right?\n") #Takes the user's input using a prompt
if choice1=="left": 
    choice2=input("You have reached a water body.You can either wait for a boat or swim through. Do you want to swim or wait?\n")
    if choice2=="wait":
        choice3=input("A boat has come for you and taken you across the water body. You see 3 doors: red, blue and yellow. Which one do you choose?\n")
        if choice3=="yellow":
             print("Congratulations, you won!\n")
        elif choice3=="red":
             print("The room was full of lions and they ate you! Game over!\n")
        elif choice3=="blue":
             print("The king cobra in the room bit you. You died. Game over!\n")
        else:     
             print("That doesn't look like an option :O read the options again or check if there was a typo and try again :)") #This is printed only if the user inputs something that is outside the options in the question prompt
    elif choice2 =="swim":
        print("The sharks ate you! Game over.\n")
    else: 
        print("That doesn't look like an option :O read the options again or check if there was a typo and try again :)")
elif choice1=="right":
   print("Game over! You took the wrong turn...")
else:
   print("That doesn't look like an option :O read the options again or check if there was a typo and try again :)")
         
#The print statements can be customized based on your needs and interests