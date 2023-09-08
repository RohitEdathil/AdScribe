from repo.mongo import MongoRepository
from repo.pinecone import PineconeRepository
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bussiness_repo = MongoRepository()

if getenv("LLM") == "openapi":
    embedding = OpenAIEmbeddings()
else:
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

vector_repo = PineconeRepository(embedding=embedding)

for product in bussiness_repo.get_products():
    vector_repo.ingest(product)
