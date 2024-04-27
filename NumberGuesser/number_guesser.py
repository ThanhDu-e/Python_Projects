import random

# keeps track of guesses
Number_Of_guesses = 0

# input for the range the number will be in
range = input("Enter a large number: ")

# checks if string input is a number and convert it to int
if range.isdigit:
    range = int(range)

# assign random value
RANDOM_NUMBER = random.randint(-range, range)

# loop
while (True):
    # get user guess
    guess = input("Guess the random number: ")
    
    # check if the guess is a number
    if guess.isdigit:
        guess = int(guess) # convert to int
        Number_Of_guesses += 1 # increment guess count

        # if guess is greater than random value, let user know  the value is lower
        if guess > RANDOM_NUMBER:
            print("Lower")
            continue # skips the rest and goes to next loop iteration

        # if guess is less than random value, let user know the value is higher
        if guess < RANDOM_NUMBER:
            print("Higher")
            continue # skips the rest and goes to next loop iteration
        
        # if guess isn't greater than or less than value, then guess == RANDOM_NUMBER
        # break out loop
        break 

    else:
        print("Enter a number. ")



print("Correct!")
print("Total guess: " + str(Number_Of_guesses))