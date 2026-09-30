import requests

response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
print("Response text (pehle 200 characters):", response.text[:200])