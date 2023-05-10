tiny = open("FF_tiny.txt")                                          # 'File' Object
year = input("please enter a year:  ")                              # str, '1926'

final_data = [line.rstrip() for line in tiny if line[:4] == year]   # List, ['19260701    0.09    0.22    0.30   0.009', '19260702    0.44    0.35    0.08   0.009']

print(final_data)