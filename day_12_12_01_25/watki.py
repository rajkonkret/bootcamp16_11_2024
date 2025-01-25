# koorutyny
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=20) as executor:
    for i in range(20):
        executor.submit(print, i)
