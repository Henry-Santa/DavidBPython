year = '1926'                   # str, '1926'

mktrf_list = []                 # list, []

tiny_file = open("FF_tiny.txt") # 'File' object

for line in tiny_file.readlines():  # str, '19260701    0.09    0.22    0.30   0.009'
    if line.startswith(year):       # bool, True
        data = line.split()         # List, [19260701, 0.09, 0.22, 0.30, 0.009]
        mktrf_list.append(float(data[1]))

# mktrf_list ends as [0.09, 0.44]

print(mktrf_list)