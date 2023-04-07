import sys

from src.components.discord_bot import client, discord_token
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
    This function runs a Discord bot using a provided token and raises a custom exception if an error
    occurs.
    """
    try:
        client.run(discord_token)

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
