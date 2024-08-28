from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
import getpass
import os


os.environ["OPENAI_API_KEY"] = ""

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

# Template
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability {input}.",
        ),
        
    ]
)

chain = prompt | model

response = chain.invoke(
    [HumanMessage(content="how tall is the average person")],
)

print(response)
