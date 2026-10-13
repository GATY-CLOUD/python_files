# When our access token has expired, we send a request like this to the authentication server.
# an endpoint in the authorization server - POST/oauth/token

data = {
    "grant_type" : "refresh_token",
    "refresh_token" : refresh_token,
}
url = "https://auth.example.com/oauth/token"

response = requests.post(url, json=data)
print(f'Status Code: {response.status_code}')


# server receives something like:
# POST /oauth/token HTTP/1.1
# Content-Type: application/x-www-form-urlencoded

# grant_type=refresh_token&refresh_token=refresh_456


# authorization server may respond with something like this
{
    "access_token": "new_access_789",
    "token_type": "Bearer",
    "expires_in": 3600
}

# python extracts it
data = response.json()
access_token = data["access_token"]

# and uses it
headers = {"Authorization": f"Bearer {access_token}"}


matric_number = "AU202300910"
