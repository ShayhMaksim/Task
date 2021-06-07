from abc import abstractmethod
from typing import List
from Mediator import Mediator
from Signal import Signal

class MediatorWrapper(Mediator):
    
    def __init__(self, num_signals:int ,  characteristics:List,  num_targets:int, signal:Signal) -> None:
        super().__init__(num_signals,characteristics,num_targets)
        self.signal=signal

    def checkSanity(self) -> bool:
        try:
            if hasattr(self.signal, 'category') and hasattr(self.signal, 'length'):
                return True 
            else:
                raise AttributeError
        except AttributeError:
            print("Аттрибуты category и/или length отсутсвуют")

    def absorb(self) -> None:
        if self.signal.nature=="audio":
            self.signal.length=self.signal.length/4

    @abstractmethod
    def reflect(self, b:List[float]) ->None:
        pass

    @abstractmethod
    def gain(self, a:int) ->float:
        pass

    @abstractmethod
    def suppress(self) ->None:
        pass