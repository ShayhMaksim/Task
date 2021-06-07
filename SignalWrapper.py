from Emitted import Emitted
from Signal import Signal
from typing import List
from MediatorWrapper import MediatorWrapper

class SignalWrapper(MediatorWrapper):
    
    def __init__(self, signal: Signal,num_signals: int, ) -> None:
        super().__init__(num_signals, signal.statistic(), signal.category, signal)

    def reflect(self, b: List[float]) -> None:
        try:
            if isinstance(self.signal,Emitted):
                print("signal является сущностью класса Emitted")
            else:
                raise TypeError
        except TypeError:
            print("signal не является сущностью класса Emitted")
            
    def gain(self, a: int) -> float:
        if self.signal.hazardous == True:
            print("Опасно выполнять данную операцию!")
        else:
            self.signal.length=self.signal.length*a
            self.signal.hazardous=True
        return self.signal.length

    def suppress(self) -> None:
        None

    def run(self):
        self.checkSanity()
        self.absorb()
        self.reflect([])
        self.gain(4)
        self.suppress()
