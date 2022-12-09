import random

top_bound=input("What should be the top bound of the range? ")

if top_bound.isdigit():
    top_bound=int(top_bound)
    
    if top_bound<=0:
        print("Please type a number greater than 0")
        quit()

else:
    print("Please enter a number")
    quit()

random_number=random.randint(0,top_bound)

guess=0

while True:
    guess+=1
    user_guess=input("Make a guess: ")

    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print("Please enter a number")
        continue

    if user_guess==random_number:
        print("You got it!")
        break
    elif user_guess<random_number:
        print("""Your guess was lower than the number.
         Try Again!""")
    else:
        print("""Your guess was higher than the number.
         Try Again!""")

print("You got it in", guess, "guesses!")