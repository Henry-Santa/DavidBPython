ff_data = open("Session_3/FF_data.txt") # 'file' object

while True:
    year = input("please enter a 4-digit year:  ") # str, '1990'
    
    if len(year) == 4 and year.isdigit():          # bool, True
        count = 0       # int, 0
        mkrft_sum = 0   # int, 0

        for line in ff_data: # str, '19260701    0.09   -0.22   -0.30   0.009' (initial value)

            seperated_data = line.split() # List of strings, ['19260701', '0.09', '-0.22', '-0.30', '0.009']

            if len(seperated_data) == 5 and seperated_data[0].startswith(year): # bool, False (initial value)
                count += 1
                mkrft_sum += float(seperated_data[1])
        # count ends at 253
        # sum ends at -12.770000000000005
        
        avg = round(mkrft_sum / count, 2) # float, -0.05
        
        print(f"count {count}, sum {round(mkrft_sum, 2)}, avg {avg}")
        break
    else:
        print("sorry, that was bad input")