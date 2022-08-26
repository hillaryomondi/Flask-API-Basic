import requests

BASE = "http://127.0.0.1:5000/"

#data = [{"likes": 78, "name": "Joe", "views": 1000},
 #       {"likes": 1000, "name": "Making APIs", "views": 100},
 #       {"likes": 24, "name": "Wanyonyi", "views": 2000}]

#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json())


#input()

#response = requests.get(BASE + "video/2")
response = requests.patch(BASE + "video/2", {"views":99, "likes": 101})
print(response.json())
