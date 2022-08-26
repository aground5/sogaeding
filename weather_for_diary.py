from pydoc import describe
import requests
import json

apikey = "2c132e7faed1ebc1700c42def7338aca"
city = ["Seoul", "Washington D.C."]
weather_dict = {2: "번개", 3: "비",5: "비",6: "눈", 7: "흐림", 800: '맑음', 8: '흐림'}
                
for i in range(2):
	api = f"https://api.openweathermap.org/data/2.5/weather?q={city[i]}&appid={apikey}"
	response = requests.get(api)
	result = json.loads(response.text)
	print('icon: ', f"https://openweathermap.org/img/wn/{result['weather'][0]['icon']}@2x.png")
	descrip = result['weather'][0]['description']
	if descrip != 800:
		descrip = descrip // 100
	print(city[i], ': ', weather_dict[descrip])
	