#Diego Ellwanger e Johann Schneider
import time
import sys
import os
from Classes import ReadingProcess
from Classes import WritingProcess
from Classes import ComputingProcess
from Classes import PrintingProcess
from FilaDeProcessos import FilaDeProcessos

def main():

    pid_counter = 1  # Controla os IDs únicos dos processos
    fila = FilaDeProcessos()

    while True:
        print()
        print("|------------------------------------------------|")
        print("|                                                | ") 
        print("|             O que você deseja?                 | ") 
        print("|                                                | ") 
        print("|    1) Criar Processo                           | ")              
        print("|    2) Executar próximo                         |")
        print("|    3) Executar processo específico             |")
        print("|    4) Salvar a fila de processos               |")
        print("|    5) Carregar do arquivo a fila de processos  |")
        print("|    6) Imprimir fila de processos               | ") 
        print("|    0) Sair                                     |")
        print("|                                                |")
        print("|------------------------------------------------|")
        print()
        print()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nTipos de processos:")
            print("1. Processo de Cálculo")
            print("2. Processo de Gravação")
            print("3. Processo de Leitura")
            print("4. Processo de Impressão")
            
            tipo = input("Escolha o tipo de processo: ")
            
            if tipo == "1":
                expressao = input("Digite a expressão (exemplo: '2 + 2'): ")
                processo = ComputingProcess(pid_counter, expressao)
                fila.adicionar_processo(processo)
                print(f"Processo de cálculo criado com PID {pid_counter}.")
            elif tipo == "2":
                expressao = input("Digite a expressão a ser gravada: ")
                processo = WritingProcess(pid_counter, expressao)
                fila.adicionar_processo(processo)
                print(f"Processo de gravação criado com PID {pid_counter}.")
            elif tipo == "3":
                processo = ReadingProcess(pid_counter, fila)
                fila.adicionar_processo(processo)
                print(f"Processo de leitura criado com PID {pid_counter}.")
            elif tipo == "4":
                processo = PrintingProcess(pid_counter, fila)
                fila.adicionar_processo(processo)
                print(f"Processo de impressão criado com PID {pid_counter}.")
            else:
                print("Opção inválida.")
                continue
            
            pid_counter += 1
        
        elif opcao == "2":
            fila.executar_proximo()
        
        elif opcao == "3":
            pid = input("Digite o PID do processo a ser executado: ")
            if pid.isdigit():
                fila.executar_por_pid(int(pid))
            else:
                print("PID inválido.")
        
        elif opcao == "4":
            fila.salvar_fila()
        
        elif opcao == "5":
            fila.carregar_fila()
        
        elif opcao == "6":
            printing_process = PrintingProcess(pid_counter, fila)
            printing_process.execute()
        
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()