# pip is a package manager
import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:  # it's better to specify the encoding to avoid potential issues with character encoding
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveToFile(url, "data/times.html")