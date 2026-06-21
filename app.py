from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv 

load_dotenv();


llm = ChatMistralAI(model="mistral-large-latest", temperature=0.7)

messages = [
    SystemMessage(content="You are a helpful coding assistant."),
    HumanMessage(content="Write a JAVA function to reverse a string.")
]

response = llm.invoke(messages)
print(response.content)