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
    assert "truc1" not in b

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

def test_thing_create():
    b = Thing(3)

def test_volume():
    b = Thing(3)
    assert b.volume() == 3

def test_capacity():
    b = Box()
    assert b.capacity() == None

def test_set_capacity():
    b = Box()
    b.set_capacity(5)
    assert b.capacity() == 5

def test_has_room_for():
    b = Box()
    t = Thing(3)
    assert b.has_room_for(t)
    b.set_capacity(2)
    assert not b.has_room_for(t)

def test_action_add():
    b = Box()
    t = Thing(3)
    assert b.action_add(t) # Test si capacity = None (illimité)
    b.set_capacity(2)
    assert not b.action_add(t) # Test si capacity < taille de l'objet
    b.set_capacity(5)
    b.action_add(t)
    assert not b.action_add(t) # Test si la place restante est inférieure à la taille de l'objet
    
