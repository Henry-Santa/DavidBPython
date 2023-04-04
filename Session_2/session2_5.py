end_num = int(input("please enter an int:  ")) # int, 5

sum = 0 # int, 0

for number in range(1, end_num + 1):
    sum += number # int, 1 then 3 then 6 then 10 then 15

print(f"sum from 1 to {end_num} is {sum}")