# 01_requests_echo_bot

🚀 **Echo bot – Python va Requests yordamida Telegram API bilan ishlovchi oddiy bot**  

## 📌 Loyiha tavsifi  
Ushbu loyiha **Python, Requests va Telegram API** yordamida ishlaydigan eng oddiy **Echo Bot** hisoblanadi.  
Bot foydalanuvchidan kelgan har qanday xabarni qaytarib yuboradi.  

## ⚡ Texnologiyalar  
- Python 🐍  
- Requests 📡  
- python-dotenv
- Telegram API 🤖  

## 📥 O‘rnatish va sozlash  

1. **Virtual muhit yaratish va faollashtirish:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

2. **Kerakli kutubxonalarni o‘rnatish:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **`.env` faylini yaratish va bot tokenini kiritish:**  
   `.env` fayl ichida quyidagi qatordan iborat bo‘lishi kerak:  
   ```ini
   BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
   ```

4. **Botni ishga tushirish:**  
   ```bash
   python bot.py
   ```

## 🎯 Foydalanish  
- Botga **start** bering: `/start`
- Istalgan matnni yuboring, bot uni **aynan shunday** qaytaradi.

## 🛠 Tuzilishi  
```
01_requests_echo_bot/
│── bot.py                # Asosiy bot kodi
│── .env                  # Bot tokeni (maxfiy ma'lumot)
│── requirements.txt       # Kutubxonalar ro‘yxati
│── README.md              # Loyihaning tavsifi
```

## 📚 Qo‘shimcha manbalar  
- [Telegram API rasmiy hujjatlar](https://core.telegram.org/bots/api)  
- [Python Requests kutubxonasi](https://docs.python-requests.org/en/latest/)  

## 📩 Muallif  
**ZiyoCamp** jamoasi tomonidan tayyorlangan 🚀  
Agar savollaringiz bo‘lsa, biz bilan bog‘laning:  
📧 **Email:** support@ziyocamp.uz  
📢 **Telegram:** [@ziyocamp_networking](https://t.me/ziyocamp_networking)  
