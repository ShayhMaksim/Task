
from typing import List
import copy
import random

class Signal:
    
    codes : List = None
    strength : float = 1.0

    def __init__(self,category : int,  length:float,  nature: str,  hazardous: bool):
        self.category=category
        self.length=length
        self.nature=nature
        self.hazardous=hazardous
        self._speed=0

    @property
    def speed(self):
        """
        Устанавливаем геттер
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Устанавливаем сеттер
        """
        self._speed=value

    def statistic(self) -> List:
        if self.length>=0:
            return [self.length,self.nature,self.hazardous]

    def show(self,str:str):
        pass

    def launch(self, a:List[int]):
        try:
            if isinstance(a, List):
                self.codes = copy.deepcopy(a)
            else:
                raise ValueError
        except ValueError: 
            print("Несоответствующее значение")

    def respond(self) -> int:
        return self.strength*random.rand()