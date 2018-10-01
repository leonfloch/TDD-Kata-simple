

class SecuenciaNum:
    def procesar_secuencia(self, secuencia):

        numero_elementos = 0
        minimo = 0
        maximo = 0
        promedio = 0

        if len(secuencia) > 0:
            arraySecuencia = list(map(int, secuencia.split(",")))
            numero_elementos = len(arraySecuencia)
            minimo = min(arraySecuencia)
            maximo = max(arraySecuencia)
            suma = sum(arraySecuencia)
            promedio = promedio = suma / numero_elementos

        return [numero_elementos, minimo, maximo, promedio]



