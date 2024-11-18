#Diego Ellwanger e Johann Schneider
import os
import time
from Processo import Processo

#Subclasse para processos de cálculo
class ComputingProcess(Processo):
    def __init__(self, pid, expressao):
        
        #Inicializa o processo de cálculo com um PID e uma expressão.
        
        super().__init__(pid)  #Chama o construtor da classe base
        self.expressao = expressao  # tribui a expressão ao processo

    def execute(self):
        
        #Executa a expressão aritmética fornecida.
        #A expressão é quebrada em operandos e operador, e o cálculo é realizado com base no operador.
        
        try:
            #Adiciona espaços ao redor dos operadores para lidar com expressões sem espaçamento
            operadores = "+-*/"
            expressao_formatada = ""
            
            for char in self.expressao:
                if char in operadores:
                    expressao_formatada += f" {char} "
                else:
                    expressao_formatada += char
            
            #Remove espaços desnecessários e divide a expressão
            partes = expressao_formatada.strip().split()
            if len(partes) != 3:
                raise ValueError("Expressão inválida.")
            
            operando1, operador, operando2 = partes
            operando1, operando2 = int(operando1), int(operando2)

            #Realiza o cálculo com base no operador
            resultado = {
                '+': operando1 + operando2,
                '-': operando1 - operando2,
                '*': operando1 * operando2,
                '/': operando1 / operando2 if operando2 != 0 else "Erro: Divisão por zero"
            }.get(operador, "Operador inválido")

            #Imprime o resultado do cálculo
            print("\n|------------------------------------------------------|")
            print(f"| Resultado da expressão {self.expressao}: {resultado}                      |")
            print("|------------------------------------------------------|\n")
            

        except ValueError:
            #Captura erro de formato na expressão (ex.: falta de espaços ou valores inválidos)
            print("Erro na expressão! Use o formato 'operando operador operando'.")
        time.sleep(1.5)
