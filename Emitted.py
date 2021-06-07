from typing import List
import abc

class Emitted:
    
    __metaclass__  = abc.ABCMeta
    codes = None
    strength = None

    def __init__(self,category : int,  length:float,  nature: str,  hazardous: bool):
        self.category=category
        self.length=length
        self.nature=nature
        self.hazardous=hazardous

    @abc.abstractmethod
    def statistics(self) -> List[None]:
        pass

    @abc.abstractmethod
    def show(self,str:str):
        pass

    @abc.abstractmethod
    def launch(self,a:List[int]) -> int:
        pass

    @abc.abstractmethod
    def respond(self) -> int:
        pass

