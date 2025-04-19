import requests
import json

API_KEY = "jMO7HnaoAPg2i6DJIujrPf4al10xIfJbkqyWjmVrGwCA3jNPRs9bxfsJlZlYdHc6RZfFPYRK77MBqcQjtvQ1H1"
BASE_URL = "https://api.ataix.kz"

SYMBOL = " IMX-USDT"  # здесь символ, под который точно есть ордера

HEADERS = {
    "X-API-Key": API_KEY,
    "accept": "application/json"
}

ORDERS_FILE = "orders.json"

def fetch_orders():
    url = f"{BASE_URL}/api/orders/{SYMBOL}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        if data["status"] and "result" in data:
            return data["result"]
        else:
            print("Нет активных ордеров или ошибка в данных.")
            return []
    else:
        print(f"Ошибка при запросе: {response.status_code}")
        print(response.text)
        return []

def save_to_file(orders):
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=2, ensure_ascii=False)
    print(f"✅ Успешно сохранено в {ORDERS_FILE}")

if __name__ == "__main__":
    orders = fetch_orders()
    if orders:
        save_to_file(orders)


