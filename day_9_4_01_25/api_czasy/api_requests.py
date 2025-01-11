import time
import requests
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

def multiple_requests():
    start_time = time.time()
    for _ in range(100):
        r = requests.get(url)
        print(r.json())
    elapsed = time.time() - start_time
    print(f"Requests time: {elapsed:.4f}s")

multiple_requests()
# Requests time: 3.9896s
# dla 1 -> Requests time: 0.0580s