import time
import requests
from config import TOKEN


BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

def send_request(method, payload=None):
    """Telegram API'ga so'rov yuboruvchi yordamchi funksiya."""
    url = f"{BASE_URL}/{method}"
    try:
        response = requests.get(url, json=payload, timeout=10)
        return response.json().get("result", [])
    except requests.RequestException:
        return []

def get_updates(offset):
    """Yangi xabarlarni olib kelish."""
    return send_request("getUpdates", {'offset': offset})

def send_message(chat_id, text):
    """Berilgan chat ID'ga xabar yuborish."""
    send_request("sendMessage", {'chat_id': chat_id, 'text': text})

def send_dice(chat_id, emoji="🎲"):
    """Berilgan chat ID'ga tasodifiy zar yoki boshqa emoji yuborish."""
    send_request("sendDice", {'chat_id': chat_id, 'emoji': emoji})

def main():
    """Botning asosiy ishlash jarayoni."""
    offset = None
    print("Bot ishga tushdi...")

    try:
        while True:
            updates = get_updates(offset)
            if updates:
                for update in updates:
                    offset = update['update_id'] + 1
                    message = update.get("message", {})
                    chat_id = message.get("from", {}).get("id")

                    if not chat_id:
                        continue

                    if "text" in message:
                        send_message(chat_id, message["text"])
                    elif "dice" in message:
                        send_dice(chat_id, message["dice"]["emoji"])

            time.sleep(2)  # API'ni ortiqcha yuklamaslik uchun
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")

if __name__ == '__main__':
    main()
