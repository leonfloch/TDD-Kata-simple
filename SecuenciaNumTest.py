from unittest import TestCase
from SecuenciaNum import SecuenciaNum

class SecuenciaNumTest(TestCase):

    def test_elementos_vacio(self):
        result = SecuenciaNum().procesar_secuencia("")
        self.assertEqual(result[0], 0, "numero de elementos cadena vacia")