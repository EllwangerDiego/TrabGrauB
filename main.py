import time
import sys

from Classes import ReadingProcess
from Classes import WritingProcess

def main():
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
    print("|    6) Sair                                     |")
    print("|                                                |")
    print("|------------------------------------------------|")
    print()
    print()

    x = 1
    while x == 1:

        escolha = int(input("Digite aqui a opção desejada: "))
        if escolha == 1:
            x = 0
            print("1")
            pass

        elif escolha == 2:
            x = 0
            print("2")
            pass

        elif escolha == 3:
            x = 0
            pass

        elif escolha == 4:
            x = 0
            pass

        elif escolha == 5:
            x = 0
            pass

        elif escolha == 6:
            x = 0
            sys.exit

        else:
            print("Digite um número de 1 a 6 \n")
            time.sleep(1.5)


main()