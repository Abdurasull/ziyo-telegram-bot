import config
import handlers
from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters
)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(CommandHandler("help", handlers.help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handlers.echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()