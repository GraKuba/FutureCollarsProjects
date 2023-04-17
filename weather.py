import requests
import sys

url = 'https://api.openweathermap.org/data/2.5/forecast?lat=51.51&lon=0.1276&appid=' + sys.argv[1]

class WeatherForecast:
	def __init__(self, url):
		self.url = url
		self.list = []

	def analyseData(self, data):
		dateList = []
		for idx in data['list']:
			date = idx['dt_txt'].split(' ', 1)[0]
			weatherTpl = {date: idx['weather'][0]['main']}
			dateList.append(weatherTpl)
	
		knownDates = []
		for idx in dateList:
			for key in idx.keys():
				knownDates.append(key)

		if sys.argv[2] not in knownDates:
			return print("Date not known")
		else:
			rainyDays = []
			for idx in dateList:
				for key in idx:
					if idx[key] == 'Rain':
						rainyDays.append(key)
			if sys.argv[2] in rainyDays:
				return print('Rain')
			else:
				return print('No rain')

	def addToData(self):
		response = requests.get(self.url).json()	
		return response	

wf = WeatherForecast(url) 

data = wf.addToData()

wf.analyseData(data)
