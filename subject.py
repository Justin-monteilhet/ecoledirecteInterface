from typing import List
from dataclasses import dataclass

@dataclass
class Subject:
    def __init__(self, id_:str, code:str, name:str, averages:dict=None, coeff:int=None, teachers:List[str]=[]) -> None:
        self.id = id_
        self.code = code
        self.name = name
        self.averages = averages
        self.coeff = coeff
        self.teachers = teachers