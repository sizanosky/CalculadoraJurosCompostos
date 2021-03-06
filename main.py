"""
* Módulo 20 - Calculadora de juros compostos
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 27/05/2021
  Programa em Python 3 para calcular juros compostos.
"""

import locale
from mortgage import Loan
from helpers import *

locale.setlocale(locale.LC_MONETARY, 'pt_br')

print("Hello World!!!")

if __name__ == '__main__':
    print()
    cabecalho("Calculadora de Juros Compostos")

    valor = float(input("\nQual o valor do empréstimo desejado? "))
    taxa = float(input("Qual a taxa de juros anual? "))
    prazo = int(input("Qual é o prazo de pagamento? "))

    valor_final_a_pagar = juros_compostos(valor, taxa, prazo)
    # https://docs.python.org/3/library/locale.html
    print(f"\nO montante calculado: "
          f"{locale.currency(valor_final_a_pagar, grouping=True)}")

    # https://mortgage.readthedocs.io/en/latest/
    print('\nUsando o modulo "mortgage", Classe "Loan".')

    # Instanciando a Classe Loan
    financiamento = Loan(valor, taxa/100, prazo, currency='R$')

    print(financiamento.summarize)  # print(obj.metodo)
