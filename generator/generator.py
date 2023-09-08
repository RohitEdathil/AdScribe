from ..models.user import User
from ..repo.vector import VectorRepository
from langchain.embeddings.base import Embeddings


class Generator:
    def __init__(self, vector_repo: VectorRepository, embeddings: Embeddings):
        self.vector_repo = vector_repo
        self.embeddings = embeddings

    def generate(self, user: User) -> str:
        pass
