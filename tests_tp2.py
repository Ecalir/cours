from tp2 import *
def test_box_create():
    b = Box()

def test_box_add():
    b = Box()
    b.add("truc1")
    b.add("truc2")

def test_contains():
    b = Box()
    b.add("truc1")
    "truc2" in b

def test_remove():
    b = Box()
    b.add("truc1")
    b.remove("truc1")

def test_ouverture_fermeture():
    b = Box()
    b.is_open()
    b.close()
    b.open()