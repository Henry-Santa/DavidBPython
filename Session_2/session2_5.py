end_num = int(input("please enter an int:  ")) # int, 5

sum = 0 # int, 0

for number in range(1, end_num + 1):
    sum += number # int, 1 (Initial Value)
# sum ends up being 15
print(f"sum from 1 to {end_num} is {sum}")