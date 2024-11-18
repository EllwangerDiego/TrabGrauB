#Diego Ellwanger e Johann Schneider
from abc import ABC, abstractmethod

class Processo(ABC):
    def __init__(self, pid):
        self.pid = pid
    
    @abstractmethod
    def execute(self):
        pass  # A subclasse precisa implementar o método


