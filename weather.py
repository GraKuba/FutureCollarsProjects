import requests
import sys
from datetime import datetime
import pprint

url = 'https://api.openweathermap.org/data/2.5/forecast?lat=51.51&lon=0.1276&appid=' + sys.argv[1]

class WeatherForecast:
	def __init__(self, url):
		self.url = url
		self.list = []

	def checkInData(self):
		for i in self.list:
			self.list.append(i)
		return self.list

	def addToData(self):
		response = requests.get(self.url).json()	
		return response	

wf = WeatherForecast(url) 

data = wf.addToData()

# pprint.pprint(data)

dateList = []
for idx in data['list']:
	date = idx['dt_txt'].split(' ', 1)[0]
	weatherTpl = {date: idx['weather'][0]['main']}
	dateList.append(weatherTpl)

for idx in dateList:
	for i,j in idx.items():
		



# weatherList = []
# for idx in dateList:
# 	if idx[1] == 'Rain': 

# print(weatherList)

# if test == sys.argv[2]:
# 	print('yes')
