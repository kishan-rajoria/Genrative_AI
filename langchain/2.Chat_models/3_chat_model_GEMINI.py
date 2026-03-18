from langchain_gemini import Gemini
from dotenv import load_dotenv  
import os

model = Gemini(model="gemini-1.5-pro", temperature=0.9)

resutls = model.invoke("What is the capital of india?") 

print(resutls)