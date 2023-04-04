def is_prime(num): # int, 5
    prime = True # bool, True
    for factor in range(2, num):
        if (num % factor) == 0: # False, False, False
            prime = False # bool, False
            break
    return prime
print("* Prime Numbers *")
search_to = int(input("Please enter max integer:  ")) # int, 5
print("") # Spacing

for number in range(2, search_to + 1): # int, 2 then 3 then 4 then 5
    if is_prime(number): # bool, True (Initial Value)
        print(number)
# Prints 2, 3, 5