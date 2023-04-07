import os

from discord import Client, Intents
from langchain import LLMChain

from src.api.chain import get_llm_chain

discord_token = os.environ["DISCORD_TOKEN"]

llm_chain: LLMChain = get_llm_chain(bot_type="discord")


class MyClient(Client):
    async def on_ready(self):
        """
        The `on_message` function is an async function that listens for messages, checks for specific
        commands, and responds with a bot-generated message using a language model.
        """
        print("Successfully logged in as: ", self.user)

    async def on_message(self, message):
        """
        This is an async function that listens for messages, checks for specific commands, and responds with
        a bot-generated message using a language model.

        Args:
          message: The message object that is received by the bot when a user sends a message in a Discord
        server.

        Returns:
          The `on_message` function is an asynchronous function that takes a `message` object as input. It
        prints the content of the message and checks if the author of the message is the bot itself. If the
        author is the bot, it returns.
        """
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None

        for text in ["/ai", "/bot", "/chatgpt", "/chatgpt-turbo", "/turbo"]:
            if message.content.startswith(text):
                command = message.content.split(" ")[0]
                user_message = message.content.replace(text, "")
                print(command, user_message)

        if command == "/chatgpt-turbo" or command == "/turbo":
            bot_response = llm_chain.predict(user_message)

            await message.channel.send(f"Answer: {bot_response}")


intents = Intents.default()

intents.message_content = True

client = MyClient(intents=intents)
