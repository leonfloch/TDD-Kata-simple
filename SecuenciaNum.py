

class SecuenciaNum:
    def procesar_secuencia(self, secuencia):

        numero_elementos = 0
        minimo = 0

        if len(secuencia) > 0:
            arraySecuencia = list(map(int, secuencia.split(",")))
            numero_elementos = len(arraySecuencia)
            minimo = min(arraySecuencia)

        return [numero_elementos, minimo]



