import os
import requests

# Get MY_API_KEY from the environment.
# Raise RuntimeError if it doesn't exist.
# Return a dictionary containing the correct Authorization header.

def make_headers():
    api_key = os.getenv("MY_API_KEY")

    if not api_key:
        raise RuntimeError("MY_API_KEY not set")

    return  {
        'Authorization' : f'Bearer {api_key}'
    }

Headers = make_headers()
print(Headers)


response = requests.get("https://jsonplaceholder.typicode.com/users", headers=Headers)
print(response.status_code)
print(response.json())








