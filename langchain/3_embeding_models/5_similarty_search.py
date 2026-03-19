from langchain import openaiembeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

emdeddings = openaiembeddings(model="text-embedding-3-small", dimensions=1024)

documents = [
    "Delhi is the capital of india?",
    "What is the capital of USA?",
    "What is the capital of UK?"
]

query = 'tell me the capital of india'

doc_embeddings = emdeddings.embed_documents(documents)
query_embedding = emdeddings.embed_query(query) 

similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

print("Similarities:", similarities)

print(sorted(list(enumerate(similarities)), key=lambda x: x[1], reverse=True))

print("Most similar document:", documents[np.argmax(similarities)])

print(query)
