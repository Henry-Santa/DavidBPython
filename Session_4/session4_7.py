unique_years = set()                # set, {}

data_file = open("FF_data.txt")     # 'File' object

for line in data_file.readlines():  # str, '19260701    0.09   -0.22   -0.30   0.009'
    unique_years.add(line[:4])      # str, '1926'

sorted_years = sorted(unique_years) # list

print(sorted_years)
print(f"{len(sorted_years)} unique years found")