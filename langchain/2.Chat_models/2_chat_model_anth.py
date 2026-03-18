from langchain_anthropic import Anthropic
from dotenv import load_dotenv      
import os

model = Anthropic(model="claude-2", temperature=0.9)    

results = model.invoke("What is the capital of india?") 

print(results)