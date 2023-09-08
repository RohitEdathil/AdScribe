from repo.business import BusinessRepository
from repo.vector import VectorRepository
from generator.generator import Generator
from delivery.delivery import Delivery

business_repo = BusinessRepository()
vector_repo = VectorRepository()
delivery = Delivery()

generator = Generator(business_repo)

for user in business_repo.get_users():
    content = generator.generate(user)
    delivery.deliver(user, content)
