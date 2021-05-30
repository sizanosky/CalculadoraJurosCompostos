def cabecalho(texto):
    titulo = f"***** {texto} *****"
    print("*" * len(titulo))
    print(titulo)
    print("*" * len(titulo))


def juros_compostos(valor, taxa, periodo):
    """
    Função para calcular juros compostos.

    Exemplo:
    Juros compostos = P (1 + R / 100)t

    - P é a quantidade do principal
    - R é a taxa
    - T é o período de tempo

    :param valor: float
    :param taxa: int/float
    :param periodo: int
    :return: float (resultado)
    """

    calculo_juros = valor * (pow((1 + taxa / 100), periodo))
    return calculo_juros
