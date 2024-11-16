#Diego Ellwanger e Johann Schneider
from Process import Processo
from Classes import ComputingProcess

class ReadingProcess(Processo):
    def __init__(self, pid, process_pool):
        #pid = Process ID (identificador do processo)
        #process_pool = Lista dos processos
        
        super().__init__(pid)
        self.process_pool = process_pool
    
      #Função para carregar/ler o arquivo e dar append em uma lista
    def execute(self):
          with open("computation.txt", "r") as file:
                lines = file.readlines()

          for line in lines:
                expression = line.strip()
                if expression:
                      new_pid = len(self.process_pool) + 1
                      computing_process = ComputingProcess(new_pid, expression)
                      self.process_pool.append(computing_process)

          #Limpa o arquivo apos ler
          with open ("computation.txt", 'w') as file:
                file.truncate(0)