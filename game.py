import random
ran = random.randint(1, 3)
guy = input("Please enter rock, paper or scissors: ").lower()
if ran == "1":
    "rock"
if ran == "2":
    "paper"
if ran == "3":
    "scissors"
#gameplay
if guy == "rock":
    if ran == 3:
        print("")
        print("Player chose rock, computer chose scissors...Player wins!")
    elif ran == 2:
        print("")
        print("Player chose rock, computer chose paper...Computer wins!")
    elif ran == 1:
        print("")
        print("Player chose rock, computer chose rock...Draw!")
if guy == "paper":
    if ran == 3:
        print("")
        print("Player chose paper, computer chose scissors...Computer wins!")
    elif ran == 2:
        print("")
        print("Player chose paper, computer chose paper...Draw!")
    elif ran == 1:
        print("")
        print("Player chose paper, computer chose rock...Player wins!")
if guy == "scissors":
    if ran == 3:
        print("")
        print("Player chose scissors, computer chose scissors...Draw!")
    elif ran == 2:
        print("")
        print("Player chose scissors, computer chose paper...Player wins!")
    elif ran == 1:
        print("")
        print("Player chose scissors, computer chose rock...Computer wins!")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Made by Alan :)")
print("")
print("")
input("Press Enter to Close")
