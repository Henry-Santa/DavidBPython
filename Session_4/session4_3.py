year = input("please enter a 4-digit year:  ") # str, '1990'

if len(year) == 4 and year.isdigit():          # bool, True
    print(f"input validated:  {year}")
else:
    print("sorry, must be 4 digits")
    exit()