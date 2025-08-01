import requests
import time
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch(url, delay=True):
    """Отправляет GET-запрос и возвращает HTML текст"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        if delay:
            time.sleep(random.uniform(1, 2))
        return response.text
    except requests.RequestException as e:
        print(f"не удалось загрузить {url}: {e}")
        return None
