#Este estudo é um teste para fazer uma calculadora em Python

nome = input("Digite seu nome: ")
print(f"Olá,Sr.{nome}, seja Bem-vindo à: Calculadora")

import math


def somar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    return x / y


def calculator():
    print("Selecione a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite sua escolha (1/2/3/4): ")

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if operacao == '1':
        print(num1, "+", num2, "=", somar(num1, num2))

    elif operacao == '2':
        print(num1, "-", num2, "=", subtrair(num1, num2))

    elif operacao == '3':
        print(num1, "*", num2, "=", multiplicar(num1, num2))

    elif operacao == '4':
        print(num1, "/", num2, "=", dividir(num1, num2))

    else:
        print("Opção inválida!")


calculator()







