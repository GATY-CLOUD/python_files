import requests, json
# # GET REQUEST: Retrieving data
# response = requests.get("https://jsonplaceholder.typicode.com/users")
#
# print(f'Status Code: {response.status_code}')
# print(f'Content-type: {response.headers["content-type"]}')
# # print(f'Content-length: {response.headers["content-length"]}')
# print(response.text)



# POST REQUEST: Sending or writing data.
url= "https://jsonplaceholder.typicode.com/users"


headers = {
    "authorization" : "Bearer 234",
    "content-type" : "application/json"
}

Information = {
    "name":"Ezenwosu Chidera",
    "email":"ezenwosuchideracyprian@gmail.com",
    "Net Worth":"$5000000"
}


response = requests.post(url, headers=headers, json=Information)    # the data is in json
print(f'server received: {response.json()}')
print(f'Status: {response.status_code}')
print(f'Content-type: {response.headers["content-type"]}')
print(response.json())     # we convert the json object back to a python object
print(response.request.headers)  