

class SecuenciaNum:
    def procesar_secuencia(self, secuencia):

        numero_elementos = 0

        if len(secuencia) > 0:
            arraySecuencia = list(map(int, secuencia.split(",")))
            numero_elementos = len(arraySecuencia)

        return [numero_elementos]



