'''Welcome to the number gussing game(challenge)
    in this game , a random number between 1 and 100
    is selected 

    - 3 mode of game (easy,midium,hard)
    - 7 chances to guess the correct number
    -40 second to complete the game.
    - Hints' after you loss 2 attempts[even/odd]'''

## Your goal is simple: Guess the number before time or attempts run out!

import random
import time


n = random.randint(1,100)

level = int(input("choose difficulty level(1=Easy,2=mdeium,3=hard:) = "))

if level ==1:
    # n = random.randint(1,30)
    time_limit = 60
    
elif level ==2:
    # n = random.randint(1,50)
    time_limit = 45

else:
    # n = random.randint(1,100)
    time_limit = 30

a = -1
guesses = 0
attemt = 0
max_attempt = 7
## provide fix amount of time for user to guess game.

user_time = time.time()
while(a !=n ):
    if time.time() - user_time > time_limit:
        print(f"Time up' You lost the game. the number is {n}")
        break
    
    guesses+=1
    attemt+=1

    a = int(input("guess a number = "))
    
    if a<0 or a>100:
        print("invalid number❌' please input valid number")
        break

    print(f" remaining attempt : {max_attempt-attemt}")

    ## check how much attempt user used
    if(attemt>max_attempt):
        print(f"You loss 'your max attempt is complete the number is {n}")
        break

    ## they provide hint to user 
    if attemt == 2:
        print("hint: the number is even"
    if n%2 == 0 else "hint: the number is odd" )
        
    if(a>n):
        print("please guess low number")
    elif(a<n):
        print("please guess high number")
    else:
        print(f"You guess a number {n} in {guesses} attepts")