import random

number_to_guess = random.randint(1,100)          # int, 25

print("I am thinking of a number from 1 to 100.   Try to guess it and")
print("I'll give you hints about it.")

number_of_guesses = 1 # int, 1

while True:
    guess = input("Your guess?  (q to quit): ") # str, '25'
    if guess == "q":
        print("You chose to quit.  Have a great day!")
        break

    if guess.isdigit():
        guessed_number = int(guess)  # int, 25
        if guessed_number == number_to_guess: # bool, True
            print("you got it!  You guessed it in " + str(number_of_guesses) + " tries.")
            break
        elif guessed_number > number_to_guess:
            print("your guess is HIGHER than the number I'm thinking of.")
        else: # If it is not the number and not higher than it must be lower than
              # the number to guess so there is no need for an elif statement
            print("your guess is LOWER than the number I'm thinking of.")

        number_of_guesses += 1 # int, number_of_guesses + 1
    else:
        print("Enter a valid response please.")