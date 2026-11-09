"""
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
"""
import httpx

# GET request to example.com

response = httpx.get("https://www.example.com")

response.raise_for_status()

print(response.text)
data = response.json()

# ======================================================================================================================
# With a Client

page = 1
with httpx.Client() as client:
    while True:
        response = client.get("https://www.example.com", params={"page": page})

        response.raise_for_status()

        print(response.text)
        data = response.json()

        if not data:
            break

        page += 1