from abc import ABC, abstractmethod
from models.product import Product
from langchain.embeddings.base import Embeddings


class VectorRepository(ABC):
    def __init__(self, embedding: Embeddings) -> None:
        self.embedding = embedding

    @abstractmethod
    def ingest(self, product: Product) -> None:
        pass
