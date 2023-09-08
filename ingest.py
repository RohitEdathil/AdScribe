from repo.mongo import MongoRepository
from repo.pinecone import PineconeRepository
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

bussiness_repo = MongoRepository()
vector_repo = PineconeRepository(embedding=OpenAIEmbeddings())

for product in bussiness_repo.get_products():
    vector_repo.ingest(product)
