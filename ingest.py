from repo.business import BusinessRepository
from repo.vector import VectorRepository

bussiness_repo = BusinessRepository()
vector_repo = VectorRepository()

for product in bussiness_repo.get_products():
    vector_repo.ingest(product)
