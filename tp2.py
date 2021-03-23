import yaml
import io

# ===============
# Fonctions globales
# ===============

def list_from_yaml(data):
    stream = io.StringIO(data)
    liste_data = yaml.load(stream)
    resultat = dict()
    resultat["box"] = []
    resultat["thing"] = []
    for data in liste_data:
        if data["type"] == "Box":
            resultat["box"].append(Box.from_yaml(data))
        elif data["type"] == "Thing":
            resultat["thing"].append(Thing.from_yaml(data))
    return resultat

# ===============
# Classes
# ===============

class Box:

    # ===============
    # Constructeur
    # ===============

    def __init__(self, is_open = False, capacity = None):
        self._contents = []
        self._ouvert = is_open
        self._capacity = capacity
        self._cle = None
    
    @staticmethod
    def from_yaml(data):
        is_open = data.get("is_open", False)
        capacity = data.get("capacity", None)
        return Box(is_open, capacity)

    # ===============
    # Getter
    # ===============

    def __contains__(self,valeur):
        return valeur in self._contents

    def capacity(self):
        return self._capacity
    
    def is_open(self):
        return self._ouvert

    # ===============
    # Setter
    # ===============

    def add(self, truc):
        self._contents.append(truc)
    
    def remove(self,truc):
        self._contents.remove(truc)

    def close(self):
        self._ouvert = False
    
    def open(self):
        if self._cle == None:
            self._ouvert = True
    
    def set_capacity(self,nouveau_volume):
        self._capacity = nouveau_volume

    def set_key(self, objet):
        self._cle = objet

    # ===============
    # Méthodes
    # ===============

    def action_look(self):
        resultat = "La boite contient: "
        if self._ouvert is True:
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

    def find(self,nom):
        resultat = None
        if self._ouvert is True:
            for objet in self._contents:
                if objet.has_name(nom):
                    resultat = objet
        return resultat
    
    def __repr__(self):
        return str(self._contents) +" "+ str(self._ouvert) +" "+ str(self._capacity)

    def open_with(self, objet):
        if self._cle == None or self._cle == objet:
            self._ouvert = True


class Thing:

    # ===============
    # Constructeur
    # ===============

    def __init__(self,volume,name=None):
        self._volume = volume
        self._name = name

    @staticmethod
    def from_yaml(data):
        volume = data.get("volume", None)
        name = data.get("name", None)
        return Thing(volume, name)

    # ===============
    # Getter
    # ===============

    def volume(self):
        return self._volume

    def set_name(self,nom):
        self._name = nom
    
    def __repr__(self):
        return self._name

    def has_name(self,nom):
        if self._name == nom:
            resultat = True
        else:
            resultat = False
        return resultat

    