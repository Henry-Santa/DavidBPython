first_num = input("please enter an int:  ")     # str, '5'
second_num = input("please enter an int:  ")    # str, '3'

try:
    first_num = int(first_num)                  # int, 5
    second_num = int(second_num)                # int, 3

    result = round(first_num/second_num, 2)     # float, 1.67

    print(f"{first_num} / {second_num} = {result}")
    
except ValueError:
    print("error:  both values must be integers")
except ZeroDivisionError:
    print("error:  second value cannot be 0")