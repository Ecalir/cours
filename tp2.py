class Box:
    def __init__(self):
        self._contents = []
        self._ouvert = False
        self._capacity = None

    # ===============
    # Get
    # ===============

    def __contains__(self,valeur):
        return valeur in self._contents

    def capacity(self):
        return self._capacity
    
    def is_open(self):
        return self._ouvert

    # ===============
    # Set
    # ===============

    def add(self, truc):
        self._contents.append(truc)
    
    def remove(self,truc):
        self._contents.remove(truc)

    def close(self):
        self._ouvert = False
    
    def open(self):
        self._ouvert = True
    
    def set_capacity(self,nouveau_volume):
        self._capacity = nouveau_volume

    # ===============
    # Méthodes
    # ===============

    def action_look(self):
        resultat = "La boite contient: "
        if self._ouvert == True:
            resultat += ", ".join(self._contents)
        else:
            resultat = "La boite est fermée."
        return resultat

    def has_room_for(self,objet):
        if self._capacity == None or self._capacity >= objet.volume():
            resultat = True
        else:
            resultat = False
        return resultat

    def action_add(self,valeur):
        if self._ouvert == False:
            resultat = False
        else:
            resultat = True
            if self._capacity == None:
                self.add(valeur)
            elif self._capacity >= valeur.volume():
                self.add(valeur)
                self._capacity -= valeur.volume()
            else:
                resultat = False
        return resultat


class Thing:
    def __init__(self,volume):
        self._volume = volume
        self._name = ""
    
    def volume(self):
        return self._volume
    
    def set_name(self,nom):
        self._name = nom
    
