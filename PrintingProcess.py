#Diego Ellwanger e Johann Schneider
import time
from Processo import Processo  #Importa a classe base Processo, que será estendida pela classe PrintingProcess

class PrintingProcess(Processo):
    def __init__(self, pid, fila_processos):
        #Inicializa um processo de impressão.
        super().__init__(pid)  #Chama o construtor da superclasse para inicializar o PID
        self.fila_processos = fila_processos  #Armazena a referência para a fila de processos
    
    def execute(self):
        #Executa o processo de impressão, exibindo todos os processos atualmente na fila.
        #Para cada processo na fila, imprime o PID, o tipo do processo e seus atributos.

        print("\nFila de Processos:")  # Título para a exibição dos processos
        for processo in self.fila_processos.processos:  # Itera sobre todos os processos na fila
            #Exibe o PID, o nome da classe (tipo de processo) e os atributos do processo
            print(f"PID: {processo.pid}, Tipo: {type(processo).__name__}, Dados: {vars(processo)}")
        print()
        time.sleep(2)