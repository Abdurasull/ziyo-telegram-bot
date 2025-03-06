import logging
import config

from telegram import Update, ForceReply, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    bot = context.bot

    chat_id = update.message.from_user.id
    text = """```python
    print("hello world)
    ```
    """

    bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="exit"), KeyboardButton(text="exit"), KeyboardButton(text="exit")
                ],
                [
                    KeyboardButton(text="bosh sahifa"), KeyboardButton(text="Mahsulotlar")
                ],
                [
                    KeyboardButton(text="location", request_location=True), KeyboardButton(text='contact', request_contact=True)
                ]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        ),
        parse_mode=ParseMode.MARKDOWN
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('nima yordam!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def echo_dice(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    bot = context.bot

    chat_id = update.message.from_user.id
    emoji = update.message.dice.emoji

    bot.send_dice(chat_id, emoji)

def boshla(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="boshlandi!",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Uzbek", callback_data="uz")
                ],
                [
                    InlineKeyboardButton(text="English", callback_data="en")
                ]
            ]
        )
    )

def echo_photo(update: Update, context: CallbackContext) -> None:
    update.message.reply_photo(
        update.message.photo[0]
    )

def get_contact(update: Update, context: CallbackContext) -> None:
    print(update.message.contact)

def get_location(update: Update, context: CallbackContext) -> None:
    print(update.message.location)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("boshla", boshla))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.dice, echo_dice))
    dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))
    dispatcher.add_handler(MessageHandler(Filters.location, get_location))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()