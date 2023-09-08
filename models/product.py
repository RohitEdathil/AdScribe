from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    name: str
    price: float
    description: str

    __template__ = open("templates/product.template.txt").read()

    def __str__(self):
        return self.__template__.format(**self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
