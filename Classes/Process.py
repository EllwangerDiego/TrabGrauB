#Diego Ellwanger e Johann Schneider
from abc import ABC, abstractmethod

class Process(ABC):
    def __init__(self, pid):
        self._pid = pid

    @property
    def pid(self):
        return self._pid

    @abstractmethod
    def execute(self):
        pass