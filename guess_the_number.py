import random

game = True
guess = 3
bot = random.randrange(1,11)

while game and guess > 0:
    
    answer = int(input(f"Guess the number between 1-10! {guess} chance(s) left. | "))
    
    if answer <= 0 or answer > 10:
        print("Choose a number between 1 and 10!")
    
    if answer == bot:
        print("You've got it!", guess - 1 ,"Guess(es) remained: ")
        guess = 0
        
    else:
        guess = guess - 1

    if game and guess == 0:
        restart = input("Would you like to play another round? (y/n)")
    
        if restart == "y" or restart == "Y":
            bot = random.randrange(1,11)
            guess = 3
    
        elif restart == "n" or restart == "N":
            break
    
        else:
            break

print("Thanks for playing!")
input("Press Enter to terminate...")
