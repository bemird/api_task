import requests

AUTHORIZATION_SERVER_URL = "http://localhost:8000/token"
RESOURCE_API_URL = "http://localhost:9000/resource"

def main():
    # Simulate client obtaining a token from the Authorization Server
    response = requests.get(AUTHORIZATION_SERVER_URL)
    token = response.json()["token"]

    # Use the obtained token to access the Resource API
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(RESOURCE_API_URL, headers=headers)

    if response.status_code == 200:
        print("Resource API response:", response.text)
    else:
        print("Failed to access Resource API:", response.status_code)

if __name__ == "__main__":
    main()

