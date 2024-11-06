#Diego Ellwanger e

class WritingProcess:
    def __init__(self,pid):
        self.__pid = pid

    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid):
        self.__pid = pid

  
    
    #Função para escrever no arquivo
    def escrever_arquivo(self, pid, expressao):
        process = f"{pid},{expressao}\n"
        with open('computation.txt', 'a') as arquivo:
            arquivo.write(process)  #Adiciona o processo no final do arquivo
    