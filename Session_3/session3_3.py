year = '1990'   # str, '1990'

ff_data = open("Session_3/FF_data.txt") # 'file' object

count = 0       # int, 0
mkrft_sum = 0   # int, 0

for line in ff_data: # str, '19260701    0.09   -0.22   -0.30   0.009' (initial value)

    seperated_data = line.split() # List of strings, ['19260701', '0.09', '-0.22', '-0.30', '0.009']

    if len(seperated_data) == 5 and seperated_data[0].startswith(year): # bool, False (initial value)
        count += 1
        mkrft_sum += float(seperated_data[1])

print(count)
print(round(mkrft_sum, 2))