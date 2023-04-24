import sys
from typing import Dict

from langchain.chains.llm import LLMChain
from langchain.chat_models.openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import read_bot_config

template: str = """You are a chatbot having a taking a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt: PromptTemplate = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)

memory: ConversationBufferMemory = ConversationBufferMemory(memory_key="chat_history")


def get_llm_chain() -> LLMChain:
    """
    This function returns an instance of the LLMChain class with specified parameters, using the OpenAI
    API and a bot configuration file.

    Args:
      bot_type (str): a string representing the type of bot to be used for generating text. This is used
    to read the corresponding configuration from the bot configuration file.

    Returns:
      an object of type LLMChain.
    """
    logging.info("Entered get_llm_chain method of chain.py file")

    try:
        bot_config: Dict = read_bot_config()

        llm_chain = LLMChain(
            llm=ChatOpenAI(**bot_config), prompt=prompt, verbose=True, memory=memory
        )

        logging.info(f"LLM chain prompt template is {prompt.template}")

        logging.info(f"Memory type of LLM chain is {memory}")

        logging.info(f"Got llm chain object with {bot_config} as parameters")

        logging.info("Exited get_llm_chain method of chain.py file")

        return llm_chain

    except Exception as e:
        raise CustomException(e, sys)
