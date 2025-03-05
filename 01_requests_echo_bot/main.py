import time
import requests
import config


URL = f'https://api.telegram.org/bot{config.TOKEN}'


def get_updates(offset):
    url = f"{URL}/getUpdates"
    payload = {
        'offset': offset
    }
    response = requests.get(url, json=payload)

    if 'result' in response.json():
        return response.json()['result']
    return []

def send_message(chat_id, text):
    url = f"{URL}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(url, json=payload)

def send_dice(chat_id, emoji):
    url = f"{URL}/sendDice"
    payload = {
        'chat_id': chat_id,
        'emoji': emoji
    }
    response = requests.get(url, json=payload)

def main():
    offset = 1741156083 + 1
    while True:

        updates = get_updates(offset)
        if updates:
            for update in updates:
                offset = update['update_id'] + 1

                if 'message' in update:
                    chat_id = update['message']['from']['id']

                    if 'text' in update['message']:
                        text = update['message']['text']
                        send_message(chat_id, text)
                    elif 'dice' in update['message']:
                        emoji = update['message']['dice']['emoji']
                        send_dice(chat_id, emoji)
                    elif 'photo' in update['message']:
                        pass
            
        time.sleep(2)

if __name__ == '__main__':
    print("bot is runnning...")
    main()
