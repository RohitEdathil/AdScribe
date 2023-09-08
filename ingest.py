from repo.business import BusinessRepository
from repo.pinecone import VectorRepository
from dotenv import load_dotenv

load_dotenv()

bussiness_repo = BusinessRepository()
vector_repo = VectorRepository()

for product in bussiness_repo.get_products():
    vector_repo.ingest(product)
