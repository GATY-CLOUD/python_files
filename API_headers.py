# Headers allow us to send additional information about and context about our requests.
# When servers receive request with headers, they respond with headers of their own.

import requests, json
# GET REQUEST: Retrieving data

headers = {
    "accept": "application/json",
    "user-agent":"HP/Chrome"
}

response = requests.get("https://jsonplaceholder.typicode.com/users", headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Server response headers: {response.headers}')
print(f'Content-type: {response.headers["content-type"]}')
print(f'server: {response.headers["server"]}')
print(f'Date: {response.headers["date"]}')
print(f'Requests User Agent: {response.request.headers["user-agent"]}')
print(response.text)
