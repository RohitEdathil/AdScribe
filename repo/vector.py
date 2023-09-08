from abc import ABC, abstractmethod
from models.product import Product
from langchain.embeddings.base import Embeddings
from langchain.vectorstores.base import VectorStore


class VectorRepository(ABC):
    def __init__(self, embedding: Embeddings) -> None:
        self.embedding = embedding

    @property
    @abstractmethod
    def vectorstore(self) -> VectorStore:
        pass

    @abstractmethod
    def ingest(self, product: Product) -> None:
        pass
