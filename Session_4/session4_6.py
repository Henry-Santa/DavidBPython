import math

year = input("please enter a 4-digit year:  ") # str, '1926'

if len(year) == 4 and year.isdigit():          # bool, True
    pass
else:
    print("sorry, must be 4 digits")
    exit()

mktrf_list = []                 # list, []

data_file = open("FF_data.txt") # 'File' object

for line in data_file.readlines():  # str, '19260701    0.09   -0.22   -0.30   0.009'
    if line.startswith(year):       # bool, True
        data = line.split()         # List, [19260701, 0.09, -0.22, -0.30, 0.009]
        mktrf_list.append(float(data[1]))

length = len(mktrf_list)                    # int, 150
maximum = max(mktrf_list)                   # float, 1.48
minimum = min(mktrf_list)                   # float, -1.69
average = sum(mktrf_list) / len(mktrf_list) # float, 0.04860000000000001
rounded_average = round(average, 1)         # float, 0.0

sorted_list = sorted(mktrf_list)            # list, [-1.69, -1.38, -1.38, -1.2, -1.08, -1.07, -1.04, -0.99, -0.94, -0.9, -0.81, -0.76, -0.76, -0.74, -0.69, -0.68, -0.64, -0.63, -0.59, -0.59, -0.57, -0.56, -0.56, -0.55, -0.55, -0.5, -0.5, -0.47, -0.43, -0.39, -0.35, -0.35, -0.35, -0.32, -0.32, -0.32, -0.32, -0.3, -0.26, -0.24, -0.24, -0.22, -0.2, -0.18, -0.17, -0.17, -0.15, -0.13, -0.12, -0.12, -0.1, -0.09, -0.08, -0.08, -0.08, -0.07, -0.06, -0.04, -0.04, -0.03, -0.02, -0.01, 0.0, 0.0, 0.02, 0.04, 0.05, 0.06, 0.07, 0.07, 0.07, 0.08, 0.09, 0.09, 0.09, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.21, 0.21, 0.22, 0.24, 0.26, 0.26, 0.28, 0.29, 0.3, 0.31, 0.31, 0.33, 0.33, 0.33, 0.33, 0.34, 0.35, 0.35, 0.36, 0.36, 0.37, 0.39, 0.4, 0.41, 0.42, 0.44, 0.44, 0.44, 0.44, 0.44, 0.45, 0.46, 0.46, 0.48, 0.48, 0.49, 0.51, 0.51, 0.52, 0.52, 0.54, 0.55, 0.56, 0.57, 0.57, 0.59, 0.6, 0.61, 0.62, 0.65, 0.67, 0.67, 0.69, 0.77, 0.78, 0.78, 0.82, 0.83, 0.83, 0.86, 0.89, 0.91, 0.97, 1.23, 1.48]


low_index = math.ceil(length/2 -1)          # int, 74
high_index = math.floor(length/2)           # int, 75

# If the length / 2 ends with .5, meaning the length was odd,
# Both indexs end the same but if the length is even, they become the 
# two middle indexes

median = (mktrf_list[high_index] + mktrf_list[low_index]) / 2   # float, 0.475

print(f"{year} (Mkt-RF):  {length} values, max {maximum}, min {minimum}, avg {rounded_average}, med {median}")
