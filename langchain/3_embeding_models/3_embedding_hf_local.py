from langchain import hugggingfaceembeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = hugggingfaceembeddings(model="sentence-transformers/all-MiniLM-L6-v2", dimensions=384) 

text = "What is the capital of india?"

results = embeddings.embed_query(text)

print(str(results))