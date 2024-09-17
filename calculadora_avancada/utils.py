def validacao_numerica(valor):
    """Verifica se o valor é um número."""
    if not isinstance(valor, (int, float)):
        raise ValueError("O valor deve ser um número.")
    return True