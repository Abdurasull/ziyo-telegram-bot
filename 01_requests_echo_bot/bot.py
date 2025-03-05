import config
from mytelegrambot.bot import Bot


bot = Bot(config.TOKEN)

if __name__ == '__main__':
    bot.run()
