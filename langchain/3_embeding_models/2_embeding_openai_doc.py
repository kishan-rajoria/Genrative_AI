from langchain import OpenAIembeddings
from dotenv import load_dotenv

load_dotenv()

emdeddings = OpenAIembeddings(model="text-embedding-3-small", dimensions=24)

documents = [
    "What is the capital of india?",
    "What is the capital of USA?",
    "What is the capital of UK?"
]

results = emdeddings.embed_documents(documents)

print(str(results))