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


if __name__ == "__main__":
    run_telegram_bot()
