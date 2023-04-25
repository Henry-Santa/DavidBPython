green_space = open("cities_green_space.csv")            # 'File' Object

green_space_dict = {}                                   # dict, {}

for line in green_space:                                # str, 'Amsterdam,13.00%,,2018,Statistics Netherlands/TNO,'
    data = line.split(',')                              # list, ['Amsterdam','13.00%','2018','Statistics Netherlands/TNO']
    green_space_dict[data[0]] = float(data[1][:-1])     # dict, {"Amsterdamn" : 13.0}

cities_in_order = sorted(green_space_dict, key=green_space_dict.get, reverse=True) # List, ['Oslo', 'Vienna', 'Edinburgh'... 'Taipei', 'Bogotá', 'Istanbul']

for city in cities_in_order:                                                       # str, 'Oslo'
    print(f"{city} : {green_space_dict[city]}") 