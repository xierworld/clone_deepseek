from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv, find_dotenv
import os

# load_dotenv(find_dotenv())

def get_chat_response(prompt, memory, api_key):
    model = ChatOpenAI(model="deepseek-reasoner", api_key=api_key,
                       base_url="https://api.deepseek.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("简单介绍一下你自己，十个字以内", memory, os.getenv("deepseek_api_key")))
# print(get_chat_response("上一个问题是什么", memory, os.getenv("deepseek_api_key")))