import asyncio
import time
import aiohttp


async def fetch(url, session, index):
    # Pomiar czasu dla każdego zapytania
    # start_time = time.time()
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}") # Pobranie treści odpowiedzi (opcjonalne)
        # elapsed_time = time.time() - start_time
        # print(f"Request {index}: {elapsed_time:.4f} seconds")
        return response.status

async def measure_aiohttp():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"
    tasks = []

    # Pomiar całkowitego czasu dla wszystkich zapytań
    overall_start_time = time.time()

    async with aiohttp.ClientSession() as session:
        for i in range(100):  # Tworzenie 10 równoczesnych zadań
            tasks.append(fetch(url, session, i + 1))

        # Wykonanie wszystkich zadań równocześnie
        statuses = await asyncio.gather(*tasks)

    overall_elapsed_time = time.time() - overall_start_time
    print(f"Overall time for 100 requests: {overall_elapsed_time:.4f} seconds")
    return statuses

asyncio.run(measure_aiohttp())
# Overall time for 100 requests: 0.6136 seconds
# dla 1 Overall time for 100 requests: 0.0610 seconds