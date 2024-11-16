#Diego Ellwanger e Johann Schneider
from abc import ABC, abstractmethod

# Classe base para representar um processo genérico
class Processo:
    def __init__(self, pid):

        #Inicializa o processo com um identificador único (PID)
        self.pid = pid

    @property
    def pid(self):
        return self.pid

    @abstractmethod
    def execute(self):
        pass