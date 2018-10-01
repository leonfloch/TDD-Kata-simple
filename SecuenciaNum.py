

class SecuenciaNum:
    def procesar_secuencia(self, secuencia):
        numero_elementos = 0

        if len(secuencia) > 0:
            numero_elementos = 1
        if len(secuencia) > 1:
            numero_elementos = 2

        return [numero_elementos]



