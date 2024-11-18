#Diego Ellwanger e Johann Schneider
from Processo import Processo

class WritingProcess(Processo):
    def __init__(self, pid, expressao):
        super().__init__(pid)
        self.expressao = expressao
    
    def execute(self):
        with open("computation.txt", "a") as file:
            file.write(self.expressao + "\n")
        print(f"Expressão '{self.expressao}' gravada em computation.txt.")
    