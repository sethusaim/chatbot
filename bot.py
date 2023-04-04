import os

import telebot
from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.memory import ConversationBufferMemory

bot = telebot.TeleBot(os.environ["API_KEY"])

template = """You are a chatbot having a taking a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)

memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=OpenAI(model_name="gpt-3.5-turbo", temperature=0),
    prompt=prompt,
    verbose=True,
    memory=memory,
)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Hello! I'm a question answering bot powered by OpenAI and built by Sethu Sai M. Send me a question and I'll do my best to answer it!",
    )


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
def handle_message(message):
    user_message = message.text

    bot_response = llm_chain.predict(human_input=user_message)

    bot.send_message(message.chat.id, bot_response)


print("Hey, I am up....")

bot.polling()
