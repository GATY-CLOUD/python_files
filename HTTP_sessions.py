#Here, the session is being used to store common headers and automatically apply them to multiple requests.

import requests, json
session = requests.Session()

url = 'https://www.google.com'

# We are adding or updating the default HTTP headers.
session.headers.update({
    "content-type" : "application/json",
    "user-agent" : "HP/Chrome",
    "Authorization" : "Bearer gaty123"})

Archives = {
         "Name" : "Ezenwosu Chidera",
         "Email" : "ezenwosuchideracyprian@gmail.com",
         "Company" : "Apple Inc.",
         "Country" : "US",
         "Phone" : "+13125550143"
}

try:
    response1= session.get(url)
    response1.raise_for_status()
    print(response1.request.headers)
    print(f'Authorization {response1.request.headers['Authorization']}')
    print(response1.status_code)

except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as err:
    print(f'Error: {err}')

try:
    response2 = session.post(url, json=Archives)
    response2.raise_for_status()
    print(f'Authorization {response2.request.headers['Authorization']}')
    print(response2.status_code)

except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as err:
    print(f'Error: {err}')

