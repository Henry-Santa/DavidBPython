import math

user_year = '1927'                      # str, '1927'
mktrf_list = [0.97, 0.30, 0.00, 0.72]   # list, [0.97, 0.30, 0.00, 0.72]

length = len(mktrf_list)                    # int, 4
maximum = max(mktrf_list)                   # float, 0.97
minimum = min(mktrf_list)                   # float, 0.0
average = sum(mktrf_list) / len(mktrf_list) # float, 0.4975
rounded_average = round(average, 1)         # float, 0.5

sorted_list = sorted(mktrf_list)            # list, [0.00, 0.30, 0.72, 0.97]

low_index = math.ceil(length/2 -1)          # int, 1
high_index = math.floor(length/2)           # int, 2

# If the length / 2 ends with .5, meaning the length was odd,
# Both indexs end the same but if the length is even, they become the 
# two middle indexes

median = (mktrf_list[high_index] + mktrf_list[low_index]) / 2   # float, 0.15


print(f"{user_year} (Mkt-RF):  {length} values, max {maximum}, min {minimum}, avg {rounded_average}, med {median}")

