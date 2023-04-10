import csv
import requests
import matplotlib.pyplot as plt

my_url = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&'
          'symbol=IBM&interval=5min&apikey=demo&datatype=csv')

response = requests.get(my_url)         # return a 'response' object
text = response.text                    # read into a string

lines = text.splitlines()               # list of str (lines)

reader = csv.reader(lines)              # 'reader' object

header_line = next(reader)              # (Only if file data has a header line - skips to next line.
                                        #  Returns the skipped line.)

rows = [] # List of lists 
          # So I can reverse the times and have them in historical order
for row in reader:
    rows.append(row)


points_open = []  # List of floats
                  # Serves as the y points because the x points are about evenly spaced
points_high = []  # List of floats
                  # Serves as the y points because the x points are about evenly spaced
points_low = []   # List of floats
                  # Serves as the y points because the x points are about evenly spaced
points_close = [] # List of floats
                  # Serves as the y points because the x points are about evenly spaced
for row in rows[::-1]:
    points_open.append(float(row[1]))
    points_high.append(float(row[2]))
    points_low.append(float(row[3]))
    points_close.append(float(row[4]))

plt.plot(points_open, linestyle = 'solid', color = "green")
plt.plot(points_high, linestyle = 'solid', color = "red")
plt.plot(points_low, linestyle = 'solid', color = "blue")
plt.plot(points_close, linestyle = 'solid', color = "black")
plt.show()