import random

game = True
guess = 3
bot = random.randrange(1,11)

while game and guess > 0:
    
    answer = int(input(f"Guess the number between 1-10! {guess} chance(s) left. | "))
    
    if answer <= 0 or answer > 10:
        print("It's not between 1-10!")
    
    if answer == bot:
        print("You've got it!", guess -1 ,"Guess(es) remained: ")
        game = False
        guess = 0
        
    else:
        guess = guess - 1

print("Thanks for playing!")