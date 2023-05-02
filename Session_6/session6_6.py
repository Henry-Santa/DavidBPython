import requests
import json
response = requests.get('https://api.weather.gov/gridpoints/'
                        'OKX/33,39/forecast')                       # 'Response' object

obj = json.loads(response.text)                                     # dict, {"@context" : {}, "type" : "Feature"... "properties" : {"updated" :  "2023-05-01T02:02:11+00:00"... "periods" : []}}
curr = obj["properties"]["periods"][0]                              # dict, {"number": 1, "name": "Tonight", "startTime": "2023-04-30T22:00:00-04:00", "detailedForecast" : "Rain and a slight chance of thunderstorms...and half of an inch possible."}


forecast = f"""{curr["name"]}, {curr["startTime"][:10]}
{curr["startTime"][14:19]}

{curr["detailedForecast"]}  
"""                                                                 # str, "Tonight, 2023-04-30\n00:00\n\nRain and a slight chance of thunderstorms before 2am, then a slight chance of rain showers between 2am and 5am. Cloudy. Low around 48, with temperatures rising to around 51 overnight. Northwest wind 7 to 14 mph, with gusts as high as 24 mph. Chance of precipitation is 80%. New rainfall amounts between a quarter and half of an inch possible."

print(forecast)