class ReadingProcess:
    def __init__(self):
        pass
    
      #Função para carregar/ler o arquivo e dar append em uma lista
    def carregar_arquivo(self):
        lista = []
        with open('computation.txt', 'r') as arquivo:
                    for linha in arquivo:
                        pid, expressao = linha.strip().split(',')
                        lista.append(int(pid), expressao)