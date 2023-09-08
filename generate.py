from repo.mongo import MongoRepository
from repo.pinecone import PineconeRepository
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.llms import OpenAI, LlamaCpp

from generator.generator import Generator
from delivery.delivery import Delivery
from os import getenv

if getenv("LLM") == "openapi":
    embedding = OpenAIEmbeddings()
    llm = OpenAI()
else:
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )
    llm = LlamaCpp(
        model_path="./model.bin",
        temperature=0.1,
        n_gpu_layers=43,
        verbose=True,
    )


business_repo = MongoRepository()
vector_repo = PineconeRepository(embedding=embedding)
delivery = Delivery()

generator = Generator(vector_repo=vector_repo, llm=llm)

for user in business_repo.get_users():
    content = generator.generate(user)
    print(content)
    # delivery.deliver(user, content)
