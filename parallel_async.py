import asyncio
import aiohttp
import time

urls = ["https://www.sch9.by/",
        "https://abiturient.by/",
        "https://www.boston.gov/homepage-bostongov",
        "http://sch7.baranovichi.edu.by/",
        "https://bsu.by/",
        "https://evroopt.by/",
        "https://ok.ru/",
        "https://www.speedtest.net/ru",
        "https://www.deepseek.com/",
        "https://gemini.google.com/?hl=ru"]

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

def sync_requests():
    import requests
    start = time.time()
    for url in urls:
        requests.get(url, headers=headers).status_code
    return time.time() - start

async def async_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []
        start = time.time()
        for url in urls:
            tasks.append(session.get(url, headers=headers))
        responses = await asyncio.gather(*tasks)
        return time.time() - start

def main():
    print("Aсинхронка:")
    print(f"Синхронные запросы: {sync_requests():.2f} сек")
    print(f"Асинхронные запросы: {asyncio.run(async_requests()):.2f} сек")

if __name__ == "__main__":
    main()