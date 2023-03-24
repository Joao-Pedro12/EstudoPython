#QUESTÃO 1

num =float(input("Digite um número: "))
if num >= 0:
    print(f"Este número,{num} é Positivo")
elif num < 0:
    print(f"Este número,{num} é negativo")

#QUESTÃO 2

num_macas = int(input("Digite o número de maçãs compradas: "))  # lê o número de maçãs compradas

if num_macas < 6:  # verifica se a quantidade é menor que 6
    total = num_macas * 1.30  # calcula o valor total com o preço de R$ 1,30 cada
else:  # se a quantidade for maior ou igual a 12
    total = num_macas * 1.00  # calcula o valor total com o preço de R$ 1,00 cada

print("O valor total da compra é: R$" + str(total))  # exibe o valor total da compra