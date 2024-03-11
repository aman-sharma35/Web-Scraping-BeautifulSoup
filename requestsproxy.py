import requests

proxies = {
  "http": "http://scraperapi:efd3c31516d26400d43697@proxy-server.scraperapi.com:800",
  "https": "http://scraperapi:efd3c31516d26400d43697@proxy-server.scraperapi.com:800",
}

url = "https://api64.ipify.org?format=json"

try:
    r = requests.get(url, proxies=proxies)
    r.raise_for_status()  # Raise an HTTPError for bad responses
    print(r.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
