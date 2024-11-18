#Diego Ellwanger e Johann Schneider
import os
from Processo import Processo
from ComputingProcess import ComputingProcess



class ReadingProcess(Processo):
    def __init__(self, pid, fila_processos):
        
        #Inicializa o processo de leitura com um PID e a fila de processos.
        
        super().__init__(pid)
        self.fila_processos = fila_processos

    def execute(self):
        
        #Lê o arquivo 'computation.txt', cria e executa processos de cálculo para cada expressão.
        #Adiciona os processos à fila de processos e limpa o arquivo após a execução.
        
        if os.path.exists("computation.txt"):
            with open("computation.txt", "r") as file:
                for linha in file:
                    expressao = linha.strip()  #Remove espaços em branco da linha
                    if expressao:  #Ignora linhas vazias
                        #Gera um novo PID baseado na fila de processos
                        novo_pid = max([p.pid for p in self.fila_processos.processos], default=0) + 1
                        
                        #Cria um ComputingProcess para a expressão
                        processo_calculo = ComputingProcess(novo_pid, expressao)
                        
                        #Executa o cálculo do processo
                        processo_calculo.execute()
                        
                        # diciona o processo na fila de processos
                        self.fila_processos.adicionar_processo(processo_calculo)

            #Limpa o arquivo após a leitura e processamento
            open("computation.txt", "w").close()
            print("Expressões processadas, calculadas e arquivo computation.txt limpo.")
        else:
            print("Arquivo computation.txt não encontrado.")

