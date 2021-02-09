class Box:
    def __init__(self):
        self._contents = []
        self._ouvert = False
        self._capacity = None

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
    
    def action_look(self):
        resultat = "La boite contient: "
        if self._ouvert == True:
            resultat += ", ".join(self._contents)
        else:
            resultat = "La boite est fermée."
        return resultat

    def set_capacity(self,nouveau_volume):
        self._capacity = nouveau_volume
    
    def capacity(self):
        return self._capacity

class Thing:
    def __init__(self,volume):
        self._volume = volume
    
    def volume(self):
        return self._volume
    
