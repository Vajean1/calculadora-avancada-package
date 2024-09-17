import math

def raiz_quadrada(x):
    """Retorna a raiz quadrada de um número."""
    if x < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(x)

def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return math.pow(base, expoente)
