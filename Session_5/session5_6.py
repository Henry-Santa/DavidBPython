market_data = open('FF_abbreviated.txt')            # 'File' Object

sum_dict = {}                                       # dict, {}

for line in market_data:                            # str, '19260701    0.09    0.22    0.30   0.009'

    data = line.split()                             # list, [19260701, 0.09, 0.22, 0.30, 0.009]

    if line[:4] in sum_dict:                        # bool, False
        sum_dict[line[:4]] += float(data[1])

    else:                               
        sum_dict[line[:4]] = float(data[1])         # dict, {'1926' : 0.09}

sorted_years = sorted(sum_dict, key=sum_dict.get)   # list, ['1926', '1928', '1927']

for year in sorted_years:                           # str, '1926'
    print(f"{year}:   {sum_dict[year]}")       