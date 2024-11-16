#Diego Ellwanger e Johann Schneider
from Process import Processo

class WritingProcess(Processo):
    def __init__(self, pid, expression):
        
        super().__init__(pid)
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, new_expression):
        if isinstance(new_expression, str):
            self._expression = new_expression  # Corrige a atribuição
        else:
            raise ValueError("A expressão deve ser uma string.")

        


    def execute(self):
        with open("computation.txt", "a") as file:
            file.write(self.expression + "\n")
        print(f"WritingProcess (PID {self.pid}): Expressão '{self.expression}' gravada com sucesso.")

    
    #Função para escrever no arquivo
    def escrever_arquivo(self, pid, expressao):
        process = f"{pid},{expressao}\n"
        with open('computation.txt', 'a') as arquivo:
            arquivo.write(process)  #Adiciona o processo no final do arquivo
    