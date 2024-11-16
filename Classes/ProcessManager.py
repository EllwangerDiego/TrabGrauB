#Diego Ellwanger e Johann Schneider
class ProcessManager:
    def __init__(self, max_size=100):
        self.process_pool = []
        self.max_size = max_size

    def add_process(self, process):
        if len(self.process_pool) >= self.max_size:
            print("A fila de processos está cheia. Não é possível adicionar mais processos.")
        else:
            self.process_pool.append(process)

    def execute_next(self):
        if self.process_pool:
            process = self.process_pool.pop(0)  #Remove o primeiro processo
            process.execute()
        else:
            print("A fila está vazia.")

    def execute_specific(self, pid):
        for i, process in enumerate(self.process_pool):
            if process.pid == pid:
                process.execute()
                self.process_pool.pop(i)  #Remove o processo executado
                return
        print(f"Processo com PID {pid} não encontrado.")
