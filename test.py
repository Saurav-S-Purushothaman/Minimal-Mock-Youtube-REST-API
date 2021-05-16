import requests

BASE ="http://127.0.0.1:5000/"


data = [{"likes":13,"name":"Saurav", "views":1300},
		{"likes":1,"name":"Hashika", "views":1040},
		{"likes":44,"name":"Samika", "views":140},
		{"likes":555,"name":"Rhithu", "views":1440}]


for i in range(len(data)):

	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())



input()

response = requests.get(BASE + "video/2")
print(response.json())