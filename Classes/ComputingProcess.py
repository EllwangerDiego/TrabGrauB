
import os  # Módulo para operações relacionadas ao sistema de arquivos
from Process import Processo

# Subclasse para processos de cálculo
class ComputingProcess(Processo):
    def __init__(self, pid, expressao):

        #Inicializa o processo de cálculo com um PID e uma expressão.

        super().__init__(pid)  # Chama o construtor da classe base
        self.expressao = expressao  # Atribui a expressão ao processo

    def execute(self):
        #Executa a expressão aritmética fornecida. A expressão é quebrada em operandos e operador, e o cálculo é realizado com base no operador.
        try:
            # Divide a expressão em operandos e operador
            operando1, operador, operando2 = self.expressao.split()
            # Converte os operandos de string para inteiros
            operando1, operando2 = int(operando1), int(operando2)
            
            # Realiza o cálculo com base no operador
            resultado = {
                '+': operando1 + operando2,  # Soma
                '-': operando1 - operando2,  # Subtração
                '*': operando1 * operando2,  # Multiplicação
                '/': operando1 / operando2 if operando2 != 0 else "Erro: Divisão por zero"  # Divisão
            }.get(operador, "Operador inválido")  # Retorna "Operador inválido" se o operador for desconhecido
            
            # Imprime o resultado do cálculo
            print(f"Resultado da expressão {self.expressao}: {resultado}")
        except ValueError:
            # Captura erro de formato na expressão (ex.: falta de espaços ou valores inválidos)
            print("Erro na expressão! Use o formato 'operando operador operando'.")