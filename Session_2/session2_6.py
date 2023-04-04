print("Think of a number between 100 and 0, and I will try to guess it.")
input("Hit [Enter] to start.")

global upper
global lower

upper = 100 # int, 100
lower = 0 # int, 0

# Player thinks of 25
while True:
    guess = round((upper + lower) / 2)
    guessed = input(f"is it {guess} (yes/no/quit)?")
    if guessed == "yes":
        print("I knew I could do it!")
        break
    elif guessed == "quit":
        print("Goodbye.")
        break
    else:
        side = input(f"is it higher or lower than {guess}?")
        if side == "higher":
            lower = guess # int, 0
        else:
            upper = guess # int, 50
