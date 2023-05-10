tiny = open("FF_tiny.txt")                                                  # 'File' Object
year = input("please enter a year:  ")                                      # str, '1926'

final_data = [float(line.split()[1]) for line in tiny if line[:4] == year]  # List, [0.09, 0.44]

print(final_data)
