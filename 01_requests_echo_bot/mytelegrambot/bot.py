import time
import requests
from .types import Update, Message, User, Dice

class Bot:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'
        self.offset = None

    def get_updates(self) -> list[Update]:
        url = f'{self.base_url}/getUpdates'
        payload = {
            'offset': self.offset
        }
        response = requests.get(url, json=payload)

        if 'result' in response.json():
            updates = []
            for update in response.json()['result']:
                current_update = Update(update_id=update['update_id'])
                
                if 'message' in update:
                    current_message = Message(
                        message_id=update['message']['message_id'],
                        from_user=User(
                            id=update['message']['from']['id'], 
                            first_name=update['message']['from']['first_name']
                        )
                    )

                    if 'text' in update['message']:
                        current_message.text = update['message']['text']
                    elif 'dice' in update['message']:
                        current_dice = Dice(
                            emoji=update['message']['dice']['emoji'], 
                            value=update['message']['dice']['value']
                        )
                        current_message.dice = current_dice
                    current_update.message = current_message

                updates.append(current_update)

            return updates

        return []
    
    def send_message(self, chat_id: int, text: str):
        url = f"{self.base_url}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': text
        }
        response = requests.get(url, json=payload)

    def send_dice(self, chat_id: int, emoji: str):
        url = f"{self.base_url}/sendDice"
        payload = {
            'chat_id': chat_id,
            'emoji': emoji
        }
        response = requests.get(url, json=payload)

    def run(self):

        while True:

            updates = self.get_updates()
            if updates:
                for update in updates:
                    self.offset = update.update_id + 1

                    if update.message:
                        chat_id = update.message.from_user.id

                        if update.message.text:
                            text = update.message.text
                            self.send_message(chat_id, text)
                        elif update.message.dice:
                            emoji = update.message.dice.emoji
                            self.send_dice(chat_id, emoji)
            time.sleep(2)