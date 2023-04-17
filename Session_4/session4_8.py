year = input("please enter a 4-digit year:  ") # str, '1926'

if len(year) == 4 and year.isdigit():          # bool, True
    pass
else:
    print("sorry, must be 4 digits")
    exit()

factor = input("enter a factor to process: ")   # str, 'SMB'

if factor == "Mkt-RF":                          # bool, False
    data_index = 1
elif factor == "SMB":                           # bool, True
    data_index = 2                              # int, 2
elif factor == "HML":
    data_index = 3
elif factor == "RF":
    data_index = 4
else:
    exit("That factor does not exist")


data_factors = open("FF_Research_Data_Factors_daily.txt")

factor_list = []                 # list, []

for line in data_factors.readlines()[6:-3]:     # str, '19260701    0.10   -0.24   -0.28   0.009'
    if line.startswith(year):                   # bool, True
        data = line.split()                     # List, [19260701, 0.10, -0.24, -0.28, 0.009]
        factor_list.append(float(data[data_index]))

if not len(factor_list):
    exit("no values found")

average = sum(factor_list) / len(factor_list)       # float, 0.07012096774193549

print(f"{year} ({factor}):  {len(factor_list)} values, avg {average}")