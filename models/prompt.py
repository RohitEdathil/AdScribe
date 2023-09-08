from dataclasses import dataclass
from .user import User
from typing import List
from jinja2 import Template


@dataclass
class Prompt:
    user: User

    __template__ = Template(open("templates/prompt.template.txt").read())

    def __str__(self):
        return self.__template__.render(user=str(self.user))

    def __repr__(self) -> str:
        return self.__str__()
