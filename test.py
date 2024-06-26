import requests

base = "http://127.0.0.1:5000/"


# response = requests.get(base + "helloworld/egor/19")
# print(response.json())
# response = requests.post(base + "helloworld")
# print(response.json())
response = requests.put(base + "video/1", json={"likes":10, 'name':"Tim", "views":10000})
print(response.json())
response = requests.get(base + "video/1")
print(response.json())