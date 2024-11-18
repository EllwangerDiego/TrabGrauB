#Diego Ellwanger e Johann Schneider
import os  
import time
from ComputingProcess import ComputingProcess
from WritingProcess import WritingProcess
from ReadingProcess import ReadingProcess
from PrintingProcess import PrintingProcess
#Importa as classes específicas de processos de um módulo externo chamado "Classes"

class FilaDeProcessos:
    def __init__(self):
        #Inicializa uma fila de processos vazia.
        self.processos = []  #Lista que armazena os processos na fila
        self.pid_counter = 1  #Inicializa o contador de PID
    
    def adicionar_processo(self, processo):
        #Adiciona um processo à fila, desde que a fila não esteja cheia.

        if len(self.processos) < 100:  #Limita o tamanho máximo da fila a 100 processos
            self.processos.append(processo)
        else:
            print("Erro: Fila de processos cheia.")  #Mensagem de erro se a fila estiver cheia
    
    def obter_maior_pid(self):
        #Retorna o maior PID da fila de processos, para não ocorrer problemas de repetição de PIDs
        if not self.processos:
            return 0  #Se a lista estiver vazia, o próximo PID será 1
        return max([p.pid for p in self.processos])
    
    def executar_proximo(self):
        #Executa o próximo processo na fila (primeiro da lista) e o remove.
        if self.processos:  # Verifica se há processos na fila
            processo = self.processos.pop(0)  # Remove o primeiro processo da fila
            processo.execute()  # Executa o método `execute` do processo
            print(f"Processo {processo.pid} executado e removido da fila.")
            time.sleep(1.5)
        else:
            print("Nenhum processo na fila.")  # Mensagem caso a fila esteja vazia
    
    def executar_por_pid(self, pid):
        #Executa e remove um processo específico da fila, identificado pelo seu PID.

        for i, processo in enumerate(self.processos):  #Percorre a fila procurando o PID
            if processo.pid == pid:  #Se encontrar o processo com o PID informado
                processo.execute()  #Executa o processo
                del self.processos[i]  #Remove o processo da fila
                print(f"Processo {pid} executado e removido da fila.")
                return
        print("Processo não encontrado.")  #Mensagem caso o PID não seja encontrado
    
    def salvar_fila(self):
        #Salva o estado atual da fila de processos em um arquivo de texto.
        with open("fila_processos.txt", "w") as file:  #Abre ou cria o arquivo para escrita
            for processo in self.processos:  #Para cada processo na fila
                #Salva o nome da classe, PID e, se disponível, o atributo 'expressao'
                file.write(f"{type(processo).__name__},{processo.pid},{getattr(processo, 'expressao', '')}\n")
        print("Fila de processos salva em fila_processos.txt.")  #Confirmação da operação
    
    def carregar_fila(self):
        try:
            with open('fila_processos.txt', 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:  #Ignorar linhas vazias
                        continue
                    
                    try:
                        #Tenta dividir a linha em 3 partes usando apenas vírgula
                        tipo, pid, dados = line.split(',')
                        pid = int(pid)  #Converte o PID para inteiro
                        
                        if tipo == 'ComputingProcess':
                            #Cria o processo de cálculo com os dados extraídos
                            expressao = dados.strip()
                            self.processos.append(ComputingProcess(pid, expressao))
                        
                    except ValueError:
                        print(f"Formato inválido na linha: {line}. Ignorando.")
            
            print("Fila de processos carregada de fila_processos.txt.")
            
            #Atualiza o pid_counter após carregar os processos
            if self.processos:
                self.pid_counter = max([p.pid for p in self.processos]) + 1
            else:
                self.pid_counter = 1  #Caso não tenha nenhum processo, reinicia o contador
            
        except FileNotFoundError:
            print("Arquivo não encontrado.")
