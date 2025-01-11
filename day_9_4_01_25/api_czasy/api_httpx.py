import asyncio
import time
import httpx

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"


async def fetch_data(client, url, index):
    start_time = time.time()
    response = await client.get(url)
    elapsed_time = time.time() - start_time
    print(f"Request {index}: Status {response.status_code}, Time {elapsed_time:.4f}s")

    # Odczytanie zawartości odpowiedzi jako JSON
    try:
        json_data = response.json()
        print(f"Request {index}: Data {json_data}")
    except httpx.HTTPStatusError:
        print(f"Request {index}: Failed with status {response.status_code}")
    except Exception as e:
        print(f"Request {index}: Error {e}")


async def multiple_httpx():
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        # Tworzenie zadań dla 100 równoczesnych zapytań
        tasks = [fetch_data(client, url, i + 1) for i in range(100)]
        await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    print(f"HTTPX total time: {elapsed:.4f}s")


# Uruchomienie funkcji
asyncio.run(multiple_httpx())
# HTTPX total time: 1.3791s
# dla 1-> HTTPX total time: 0.6850s
