import random
print("Playing Rock Paper Scissors with the computer")
chooseFrom = ["r","p","s"]


compCh = random.choice(chooseFrom)
userCh = input ("What is your choice ?")

if (userCh == "r" and compCh == "p"):
    print("You chose rock. The computer chose paper.")
    print("Sorry. You lose.")
elif (userCh == "r" and compCh == "s"):
    print("You chose rock. The computer chose scissor.")
    print(" You won.")
elif (userCh == "r" and compCh == "r"):
    print("You chose rock. The computer chose rock.")
    print(" Its a tie!")
    
elif (userCh == "p" and compCh == "r"):
    print("You chose paper. The computer chose rock.")
    print("You won.")
elif (userCh == "p" and compCh == "s"):
    print("You chose paper. The computer chose scissor.")
    print(" You lose.")
elif (userCh == "p" and compCh == "p"):
    print("You chose paper. The computer chose paper.")
    print(" Its a tie!")
    
elif (userCh == "s" and compCh == "r"):
    print("You chose scissor. The computer chose rock.")
    print("You lose.")
elif (userCh == "s" and compCh == "s"):
    print("You chose scissor. The computer chose scissor.")
    print(" Its a tie.")
elif (userCh == "s" and compCh == "p"):
    print("You chose scissor. The computer chose paper.")
    print(" You won")
else:
    print("pls choose only from - r/p/s")