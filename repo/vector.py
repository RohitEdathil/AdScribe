from abc import ABC, abstractmethod
from ..models import Product


class VectorRepository(ABC):
    @abstractmethod
    def ingest(self, product: Product) -> None:
        pass
