#Diego Ellwanger e Johann Schneider
import os
import time
from ComputingProcess import ComputingProcess
from WritingProcess import WritingProcess
from ReadingProcess import ReadingProcess
from PrintingProcess import PrintingProcess
from FilaDeProcessos import FilaDeProcessos


#Função main/ principal
def main():
    print("=== Simulador de Execução de Processos ===")
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
        
        #Pede ao usuário escolher uma opção entre (0-6)
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print()
            print("|------------------------------------------------|")
            print("|                                                | ") 
            print("|             Tipos de Processos:                | ") 
            print("|                                                | ") 
            print("|    1) Processo de Cálculo                      | ")              
            print("|    2) Processo de Gravação                     |")
            print("|    3) Processo de Leitura                      |")
            print("|    4) Processo de Impressão                    |")                             
            print("|                                                |")
            print("|------------------------------------------------|")
            print()

            tipo = input("Escolha o tipo de processo: ")
            
            if tipo == "1":
                expressao = input("Digite a expressão (exemplo: '2 + 2'): ")
                print()
                processo = ComputingProcess(fila.pid_counter, expressao)
                fila.adicionar_processo(processo)
                print(f"Processo de cálculo criado com PID {fila.pid_counter}.")
            elif tipo == "2":
                expressao = input("Digite a expressão a ser gravada: ")
                print()
                processo = WritingProcess(fila.pid_counter, expressao)
                fila.adicionar_processo(processo)
                print(f"Processo de gravação criado com PID {fila.pid_counter}.")
            elif tipo == "3":
                processo = ReadingProcess(fila.pid_counter, fila)
                fila.adicionar_processo(processo)
                print(f"Processo de leitura criado com PID {fila.pid_counter}.\n")
            elif tipo == "4":
                processo = PrintingProcess(fila.pid_counter, fila)
                fila.adicionar_processo(processo)
                print(f"Processo de impressão criado com PID {fila.pid_counter}.\n")
            else:
                print("Opção inválida.\n")
                continue
            
            fila.pid_counter += 1  #Incrementa o PID para o próximo processo
        
        elif opcao == "2":
            fila.executar_proximo()
        
        elif opcao == "3":
            pid = input("Digite o PID do processo a ser executado: ")
            print()
            if pid.isdigit():
                fila.executar_por_pid(int(pid))
            else:
                print("PID inválido.")
        
        elif opcao == "4":
            fila.salvar_fila()
        
        elif opcao == "5":
            fila.carregar_fila()  #Carrega a fila e ajusta o pid_counter
        
        elif opcao == "6":
            printing_process = PrintingProcess(fila.pid_counter, fila)
            printing_process.execute()
        
        elif opcao == "0":
            print("Encerrando o sistema...")
            time.sleep(1.5)
            break
        
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()