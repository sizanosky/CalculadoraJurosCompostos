def cabecalho(texto):
    titulo = f"***** {texto} *****"
    print("*" * len(titulo))
    print(titulo)
    print("*" * len(titulo))


def juros_compostos(principal, taxa, periodo):
    """
    Função para calcular juros compostos.

    Exemplo:
    Juros compostos = P (1 + R / 100)t

    - P é a quantidade do principal
    - R é a taxa
    - T é o período de tempo

    :param principal: float
    :param taxa: int/float
    :param periodo: int
    :return: float (resultado)
    """

    calculo_juros = (principal * (pow((1 + taxa / 100), periodo)))
    return calculo_juros
