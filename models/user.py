from dataclasses import dataclass
from typing import List


@dataclass
class User:
    name: str
    email: str
    age: str
    gender: str
    interests: List[str]
    industry: str
    job_title: str

    __template__ = open("templates/user.template.txt").read()

    def __str__(self):
        return self.__template__.format(**self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
