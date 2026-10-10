print("Hello Welcome To My Guessing Game.")
print()
import random
secret= random.randint (1,10)
guess= 0
tries=0
while tries>=0:
    guess= int(input("Guess the correct number?:"))
    tries +=1
    if guess== secret:
        print("You won!!!")
        print("Congrats, won in", tries,"attempts")
        break
    elif guess< secret:
        print("Too low!")
    else:
        guess> secret
        print("Too high!")












