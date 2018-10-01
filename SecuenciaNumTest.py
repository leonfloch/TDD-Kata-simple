from unittest import TestCase
from SecuenciaNum import SecuenciaNum

class SecuenciaNumTest(TestCase):

    def test_elementos_vacio(self):
        result = SecuenciaNum().procesar_secuencia("")
        self.assertEqual(result[0], 0, "numero de elementos cadena vacia")


    def test_elementos_1_numero(self):
        result = SecuenciaNum().procesar_secuencia("1")
        self.assertEqual(result[0], 1, "numero de elementos 1 numero")


    def test_elementos_2_numeros(self):
        result = SecuenciaNum().procesar_secuencia("1,3")
        self.assertEqual(result[0], 2, "numero de elementos 2 numeros")

    def test_elementos_N_numeros(self):
        result = SecuenciaNum().procesar_secuencia("1,3,5,2,8")
        self.assertEqual(result[0], 5, "numero de elementos N numeros")