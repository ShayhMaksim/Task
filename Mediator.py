from abc import ABC, abstractmethod
from typing import List

class Mediator(ABC):
    
    def __init__(self,num_signals:int,  characteristics:List,  num_targets:int):
        self.num_signals=num_signals
        self.characteristics=characteristics
        self.num_targets=num_targets

    @abstractmethod
    def absorb(self) -> None:
        pass

    @abstractmethod
    def reflect(self, b:List[float]) ->None:
        pass

    @abstractmethod
    def gain(self, a:int) ->float:
        pass

    @abstractmethod
    def suppress(self) ->None:
        pass