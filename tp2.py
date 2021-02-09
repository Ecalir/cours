class Box:
    def __init__(self):
        self._contents = []
        self._ouvert = False

    def __contains__(self,valeur):
        return valeur in self._contents

    def add(self, truc):
        self._contents.append(truc)
    
    def remove(self,truc):
        self._contents.remove(truc)
    
    def is_open(self):
        return self._ouvert
    
    def close(self):
        self._ouvert = False
    
    def open(self):
        self._ouvert = True