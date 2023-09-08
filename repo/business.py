from abc import ABC, abstractmethod
from ..models.product import Product
from ..models.user import User
from typing import List


class BusinessRepository(ABC):
    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_products(self, user_id: int) -> List[Product]:
        pass
