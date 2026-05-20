import requests
import time
from bs4 import BeautifulSoup

url = "https://www.google.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.title.text)

else:
    print("Request failed")

time.sleep(1)
