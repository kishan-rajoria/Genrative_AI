from langchain import OpenAIembeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIembeddings(model="text-embedding-3-small", dimensions=1024)   

results = embeddings.embed_query("What is the capital of india?")

print(str(results))