year_vals = {}                                      # dict, {}

tiny = open("FF_tiny.txt")                          # "File" object

for line in tiny:                                   # str, "19260701    0.09    0.22    0.30   0.009"
    data = line.split()                             # list, ["19260701", "0.09", "0.22", "0.30", "0.009"]
    if line[:4] in year_vals:                       # bool, False
        year_vals[line[:4]].append(float(data[1]))  
    else:                                               
        year_vals[line[:4]] = [float(data[1])]      # list, [0.09]

for year in year_vals:                              # str, "1926"
    print(f"{year} : {year_vals[year]}")   