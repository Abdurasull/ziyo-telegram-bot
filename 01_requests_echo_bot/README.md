# MyTelegramBot

`MyTelegramBot` — bu Telegram botlarini yaratish uchun mo‘ljallangan Python kutubxonasi. Kutubxona Telegram API bilan ishlashni osonlashtiradi va botni yaratish, xabar yuborish va yangilanishlarni olish funksiyalarini taqdim etadi.

## Xususiyatlar
- Telegram API bilan integratsiya
- Xabar yuborish va qabul qilish
- Emoji bilan tasmalar (dice) yuborish
- Yangilanishlarni (`updates`) olish uchun timeout qo‘llab-quvvatlanadi
- Pythonic obyektlarga asoslangan arxitektura

## O‘rnatish

Loyihangizga `MyTelegramBot` kutubxonasini qo‘shish uchun quyidagi amallarni bajaring:

```bash
pip install requests  # Agar requests kutubxonasi o‘rnatilmagan bo‘lsa
```

Keyin, kutubxonani loyihangizga import qiling:

```python
import config
from mytelegrambot.bot import Bot

bot = Bot(config.TOKEN)

if __name__ == '__main__':
    bot.run()
```

## Foydalanish

### Bot obyektini yaratish
```python
from mytelegrambot.bot import Bot

bot = Bot("YOUR_TELEGRAM_BOT_TOKEN")
```

### Yangilanishlarni olish
```python
updates = bot.get_updates()
for update in updates:
    print(update.message.text)
```

### Xabar yuborish
```python
bot.send_message(chat_id=123456789, text="Salom, dunyo!")
```

### Emoji bilan tasmalar yuborish
```python
bot.send_dice(chat_id=123456789, emoji="🎲")
```

## Tuzilma

Kutubxona quyidagi asosiy modullardan iborat:

- `bot.py` — Bot bilan ishlash uchun asosiy funksiya va metodlar
- `types.py` — Telegram API javoblarini obyektlar sifatida ishlashga yordam beradigan klasslar
