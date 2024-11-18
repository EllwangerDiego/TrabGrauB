#Diego Ellwanger e Johann Schneider
class Processo:
    def __init__(self, pid):
        self.pid = pid
    
    def execute(self):
        raise NotImplementedError("Subclasse deve implementar este método.")

