import sys

from src.components.telegram_bot import bot
from src.exception import CustomException


def run_telegram_bot():
    """
    This function runs a Telegram bot and raises a custom exception if an error occurs.
    """
    try:
        bot.polling()

    except Exception as e:
        raise CustomException(e, sys)


def run_discord_bot():
    """
    This is a skeleton function for running a Discord bot with error handling.
    """
    try:
        pass

    except Exception as e:
        raise CustomException(e, sys)


def run_whatsapp_bot():
    """
    This is a Python function that runs a WhatsApp bot and catches any exceptions that occur.
    """
    try:
        pass

    except Exception as e:
        raise CustomException(e, sys)
