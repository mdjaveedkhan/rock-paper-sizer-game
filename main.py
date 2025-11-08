import random
print("1.Rock\n2.Paper\n3.Sizer")
choice1=int(input("Select your choice :"))
choices = ["rock", "paper", "scissors"]
random_choice = random.choice(choices)
print(random_choice)
if choice1==random_choice:
    print(":-) You Won the game!")
elif choice1!=random_choice:
    print(":-( You Lost the game!")
else:
    print("Select Correct Option :")    
