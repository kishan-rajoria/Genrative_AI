from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

model = ChatOpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9) 

result = model.invoke("What is the capital of india?")

print(result)
