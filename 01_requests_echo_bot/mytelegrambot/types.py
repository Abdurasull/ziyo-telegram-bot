from typing import Optional, Union


class User:
    """Telegram foydalanuvchisi haqidagi ma'lumotlarni saqlovchi klass."""
    
    def __init__(self, id: Union[int, str], first_name: str):
        self.id = id
        self.first_name = first_name


class Dice:
    """Telegram'dagi tanga tashlash (zar) emoji obyekti."""

    def __init__(self, emoji: str, value: int):
        self.emoji = emoji
        self.value = value


class Message:
    """Telegram xabari modeli."""

    def __init__(
        self, 
        message_id: Union[int, str], 
        from_user: User, 
        text: Optional[str] = None, 
        dice: Optional[Dice] = None
    ):
        self.message_id = message_id
        self.from_user = from_user
        self.text = text
        self.dice = dice

    def reply_message(self, bot, text: str):
        """Xabarga javob sifatida matnli xabar yuborish."""
        bot.send_message(self.from_user.id, text)

    def reply_dice(self, bot, emoji: str):
        """Xabarga javob sifatida zar yuborish."""
        bot.send_dice(self.from_user.id, emoji)


class Update:
    """Telegram yangilanish modeli (update)."""

    def __init__(self, update_id: Union[int, str], message: Optional[Message] = None):
        self.update_id = update_id
        self.message = message
