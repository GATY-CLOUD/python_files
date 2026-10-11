import requests
try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()   # checks the HTTP response status code. 200,201,400,401,404,500
    Information = response.json()
    print(Information)

except requests.exceptions.HTTPError as err:   # This handles HTTP errors
    print(f'Error: {err}')

except requests.exceptions.ConnectionError as err:
    print(f'Error: cannot connect to server: {err}')


name ="Ezenwosu Chidera"