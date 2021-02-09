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
    assert not "truc2" in b
    assert "truc1" in b

def test_remove():
    b = Box()
    b.add("truc1")
    b.remove("truc1")

def test_ouverture_fermeture():
    b = Box()
    assert not b.is_open()
    b.open()
    assert b.is_open()
    b.close()
    assert not b.is_open()

def test_action_look():
    b = Box()
    b.add("truc1")
    b.add("truc2")
    assert b.action_look() == "La boite est fermée."
    b.open()
    assert b.action_look() == "La boite contient: truc1, truc2"