from func_usuarios import *
from func_senha import *

def test_valida():
    #testa usuário:
    assert True == letramaiuscula("Rafael")
    assert False == letramaiuscula("rafael")

    assert True == espacouser("Rafael")
    assert False == espacouser("Ra fael")

    assert True == maxuser("Rafael")
    assert False == maxuser("RafaelRafaelRafaelRafaelRafaelRafaelRafaelRafaelRafaelRafaelRafaelRafaelRafael")

    assert True == userx("Rafael")
    assert False == userx("Raf@el")

    #testa senha:

    assert True == minpass("Olamundo26!!")
    assert False == minpass("Ola26!!")

    assert True == passx("Olamundo26!!")
    assert False == passx("Olamundo2626")

    assert True == numpass("Olamundo26!!")
    assert False == numpass("Olamundo!!!!")

    assert True == passmaiuscula("Olamundo26!!")
    assert False == passmaiuscula("olamundo26!!")

    assert True == passminuscula("Olamundo26!!")
    assert False == passminuscula("OLAMUNDO26!!")