import requests


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()

    return []