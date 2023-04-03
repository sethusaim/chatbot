import os

import telebot

from utils import generate_answer

bot = telebot.TeleBot(os.environ["API_KEY"])


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Hello! I'm a question answering bot powered by OpenAI and built by Sethu Sai M. Send me a question and I'll do my best to answer it!",
    )


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(
        message,
        "I support the following commands: \n /start \n /info \n /help \n /status",
    )


@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(
        message,
        "I am a simple Telegram bot created by Sethu Sai M for iNeuron.",
    )


@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(message, "I am up and running.")


@bot.message_handler(func=lambda message: True)
def ask_question(message):
    ans = generate_answer(message.text)

    bot.reply_to(message, ans)


print("Hey, I am up....")

bot.polling()
