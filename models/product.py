from dataclasses import dataclass
from jinja2 import Template


@dataclass
class Product:
    id: str
    name: str
    price: float
    description: str

    __template__ = Template(open("templates/product.template.txt").read())

    def from_dict(data) -> "Product":
        return Product(
            data["_id"],
            data["name"],
            data["price"],
            data["desc"],
        )

    def __str__(self):
        return self.__template__.render(**self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
