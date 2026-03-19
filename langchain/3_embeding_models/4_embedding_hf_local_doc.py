from langchain import hugggingfaceembeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = hugggingfaceembeddings(model="sentence-transformers/all-MiniLM-L6-v2", dimensions=384) 

documents = [
    "What is the capital of india?",
    "What is the capital of USA?",
    "What is the capital of UK?"
]

results = embeddings.embed_documents(documents)

print(str(results))