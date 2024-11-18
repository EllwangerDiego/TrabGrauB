#Diego Ellwanger e Johann Schneider
import os  # Biblioteca para operações relacionadas ao sistema de arquivos
from Classes import ComputingProcess, WritingProcess, ReadingProcess, PrintingProcess
# Importa as classes específicas de processos de um módulo externo chamado "Classes"

class FilaDeProcessos:
    def __init__(self):
        #Inicializa uma fila de processos vazia.
        self.processos = []  # Lista que armazena os processos na fila
    
    def adicionar_processo(self, processo):
        #Adiciona um processo à fila, desde que a fila não esteja cheia.

        if len(self.processos) < 100:  # Limita o tamanho máximo da fila a 100 processos
            self.processos.append(processo)
        else:
            print("Erro: Fila de processos cheia.")  # Mensagem de erro se a fila estiver cheia
    
    def executar_proximo(self):
        #Executa o próximo processo na fila (primeiro da lista) e o remove.
        if self.processos:  # Verifica se há processos na fila
            processo = self.processos.pop(0)  # Remove o primeiro processo da fila
            processo.execute()  # Executa o método `execute` do processo
            print(f"Processo {processo.pid} executado e removido da fila.")
        else:
            print("Nenhum processo na fila.")  # Mensagem caso a fila esteja vazia
    
    def executar_por_pid(self, pid):
        #Executa e remove um processo específico da fila, identificado pelo seu PID.

        for i, processo in enumerate(self.processos):  # Percorre a fila procurando o PID
            if processo.pid == pid:  # Se encontrar o processo com o PID informado
                processo.execute()  # Executa o processo
                del self.processos[i]  # Remove o processo da fila
                print(f"Processo {pid} executado e removido da fila.")
                return
        print("Processo não encontrado.")  # Mensagem caso o PID não seja encontrado
    
    def salvar_fila(self):
        #Salva o estado atual da fila de processos em um arquivo de texto.
        with open("fila_processos.txt", "w") as file:  # Abre ou cria o arquivo para escrita
            for processo in self.processos:  # Para cada processo na fila
                # Salva o nome da classe, PID e, se disponível, o atributo 'expressao'
                file.write(f"{type(processo).__name__},{processo.pid},{getattr(processo, 'expressao', '')}\n")
        print("Fila de processos salva em fila_processos.txt.")  # Confirmação da operação
    
    def carregar_fila(self):
       # Carrega a fila de processos de um arquivo de texto e recria os objetos na memória.
        self.processos = []  # Limpa a fila antes de carregar
        if os.path.exists("fila_processos.txt"):  # Verifica se o arquivo existe
            with open("fila_processos.txt", "r") as file:  # Abre o arquivo para leitura
                for linha in file:  # Lê o arquivo linha por linha
                    # Divide a linha em tipo, PID e expressão
                    tipo, pid, expressao = linha.strip().split(",")
                    pid = int(pid)  # Converte o PID para inteiro
                    # Cria e adiciona o processo correspondente com base no tipo
                    if tipo == "ComputingProcess":
                        self.adicionar_processo(ComputingProcess(pid, expressao))
                    elif tipo == "WritingProcess":
                        self.adicionar_processo(WritingProcess(pid, expressao))
                    elif tipo == "ReadingProcess":
                        self.adicionar_processo(ReadingProcess(pid, self))
                    elif tipo == "PrintingProcess":
                        self.adicionar_processo(PrintingProcess(pid, self))
            print("Fila de processos carregada de fila_processos.txt.")  # Confirmação da operação