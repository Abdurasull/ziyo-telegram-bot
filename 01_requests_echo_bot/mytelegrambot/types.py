class User:
    def __init__(self, id: int, first_name: str):
        self.id = id
        self.first_name = first_name


class Dice:
    def __init__(self, emoji: str, value: int):
        self.emoji = emoji
        self.value = value


class Message:
    def __init__(self, message_id: int, from_user: User, text: str = None, dice: Dice = None):
        self.message_id = message_id
        self.from_user = from_user
        self.text = text
        self.dice = dice
    
    def reply_message(self, text):
        pass
    
    def reply_dice(self, emoji):
        pass


class Update:
    def __init__(self, update_id: int, message: Message = None):
        self.update_id = update_id
        self.message = message

