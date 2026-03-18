from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline(model_id= "dfsdds", task='text generation', pipeline_kwargs =dict(temperature=3.5, max_new_tokens=100))

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is capital of india")

print(result.content)
