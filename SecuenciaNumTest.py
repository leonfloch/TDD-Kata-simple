from unittest import TestCase
from SecuenciaNum import SecuenciaNum

class SecuenciaNumTest(TestCase):

    def test_elementos_vacio(self):
        result = SecuenciaNum().procesar_secuencia("")
        self.assertEqual(result[0], 0, "numero de elementos cadena vacia")


    def test_elementos_1_numero(self):
        result = SecuenciaNum().procesar_secuencia("1")
        self.assertEqual(result[0], 1, "numero de elementos 1 numero")