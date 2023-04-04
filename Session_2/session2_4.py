step = int(input("please enter an integer:  ")) # int, 25
print(f"counting from 0 to 100 by {step}'s")

count = 0 # int, 0
while count <= 100: # bool, True then True then True then True then False
    print(count)
    count += step # int, 25 (Initial Value)
# count ends up being 125