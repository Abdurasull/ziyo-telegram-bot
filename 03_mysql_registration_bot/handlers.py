import config
from telegram import Update
from telegram.ext import CallbackContext
from db import DB

db = DB(
    host=config.DB_HOST,
    port=config.DB_PORT,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db_name=config.DB_NAME
)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user

    result = db.add_user(
        telegram_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username
    )

    if result:
        update.message.reply_html(
            f'Hi <b>{user.full_name}</b>!\n\nWelcome to our bot!'
        )
    else:
        update.message.reply_html(
            f'Hi <b>{user.full_name}</b>!\n\nUpon your return!'
        )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
