#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
number=random.randint(1,9)
guessing_number=1
while True:
    guess=input("Hello, welcome to guessing game pick a number between 1-9, if u want to exit the game write 'exit' ")
    if guess=="exit":
        break
    guess=int(guess)
    if guess==number:
        print(f"U won i took U {guessing_number}")
        break
    elif guess>number:
        print("your guess is to higt, try again")
        guessing_number = guessing_number +1

    elif guess<number:
        print("your guess is tolow, try again")
        guessing_number = guessing_number+1