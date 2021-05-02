import requests

try:
    request = requests.get("http://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    print("Sin conexión a internet.")
else:
    print("Con conexión a internet.")