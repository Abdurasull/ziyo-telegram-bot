import time
import requests
from typing import List, Optional
from .types import Update, Message, User, Dice


class Bot:
    """
    Telegram boti uchun API bilan ishlovchi asosiy sinf.
    """
    
    def __init__(self, token: str, timeout: int = 30):
        """
        Bot obyektini yaratish.

        :param token: Telegram bot tokeni.
        :param timeout: getUpdates uchun kutish vaqti (sekundlarda).
        """
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.offset = None
        self.timeout = timeout

    def send_request(self, method: str, payload: Optional[dict] = None) -> dict:
        """
        Telegram API'ga so'rov yuborish.

        :param method: API metod nomi.
        :param payload: JSON formatidagi so'rov ma'lumotlari.
        :return: API javobi (`dict` formatida).
        """
        url = f"{self.base_url}/{method}"
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return {}

    def get_updates(self) -> List[Update]:
        """
        Telegram'dan yangi yangilanishlarni olish.
        :return: Yangilanishlar (`Update` obyektlari ro‘yxati).
        """
        response = self.send_request("getUpdates", {
            "offset": self.offset,
            "timeout": self.timeout
        })

        updates = []
        for update in response.get("result", []):
            update_obj = Update(update_id=update["update_id"])
            
            if "message" in update:
                message_data = update["message"]
                user = User(
                    id=message_data["from"]["id"],
                    first_name=message_data["from"]["first_name"]
                )
                
                message = Message(
                    message_id=message_data["message_id"],
                    from_user=user,
                    text=message_data.get("text"),
                    dice=Dice(
                        emoji=message_data["dice"]["emoji"],
                        value=message_data["dice"]["value"]
                    ) if "dice" in message_data else None
                )
                
                update_obj.message = message
            
            updates.append(update_obj)

        return updates

    def send_message(self, chat_id: int, text: str):
        """
        Foydalanuvchiga matnli xabar yuborish.
        :param chat_id: Telegram chat ID.
        :param text: Yuboriladigan matn.
        """
        self.send_request("sendMessage", {"chat_id": chat_id, "text": text})

    def send_dice(self, chat_id: int, emoji: str = "🎲"):
        """
        Foydalanuvchiga zar yuborish.
        :param chat_id: Telegram chat ID.
        :param emoji: Emoji turi ("🎲", "🎯", "🏀", "⚽", "🎰", "🎳").
        """
        self.send_request("sendDice", {"chat_id": chat_id, "emoji": emoji})

    def run(self):
        """
        Botni ishga tushirish va yangi xabarlarni qayta ishlash.
        """
        print("Bot ishga tushdi...")

        try:
            while True:
                updates = self.get_updates()
                if updates:
                    for update in updates:
                        self.offset = update.update_id + 1

                        if update.message:
                            chat_id = update.message.from_user.id
                            
                            if update.message.text:
                                update.message.reply_message(self, update.message.text)
                            elif update.message.dice:
                                update.message.reply_dice(self, update.message.dice.emoji)
                
                time.sleep(1)  # API'ni ortiqcha yuklamaslik uchun
        except KeyboardInterrupt:
            print("Bot to'xtatildi.")
