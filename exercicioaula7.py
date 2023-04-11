#QUESTÃO 1
num1 = 4
num2 = 8

if num1 > num2:
    print("O número {} é maior que o {}".format(num1,num1))
else:
    print("O número {} é maior que o {}".format(num2,num1))

#QUESTÃO 2

nome = int(input("Digite sua idade: "))
print(nome)

if nome > 18:
    print(f"Você é maior de idade")
else:
    print(f"Você é menor de idade")

#QUESTÃO 3

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade"))
print(nome)
print(idade)
if idade > 18:
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")

#QUESTÃO 4
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))
soma = (n1+n2+n3+n4)/4
print(soma)
if soma >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

#QUESTÃO 5

numero = 8
if numero %2==0:
    print("Este numero é par")
else:
    print("Este número é ímpar")

#QUESTÃO 6
aumento = 1.1
salario=float(input("Digite o seu salário: "))
salarionovo = (salario*aumento)
print(salarionovo)
if salarionovo > 1500:
    print("O aumento do seu salário foi de 10%")
else:
    print("Valor inválido")
aumento2 = 1.5
salario2=float(input("Digite seu salário: "))
salarionovo2=(salario2*aumento2)
print(salarionovo2)
if salarionovo2 < 1500:
    print("Seu salário teve um aumento de 15%")
else:
    print("Valor inválido")

#QUESTÃO 7
lists = [0,1,2,3,4,5,6,11]

maior = lists[0]
menor = lists[0]
for numero in lists:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(maior)
print(menor)

#QUESTAO 8

string = input("Digite uma palavra: ")
string_invertida = string[::-1]

if string == string_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")

#QUESTÃO 9

# Solicita ao usuário um número para gerar sua tabuada
numero = int(input("Digite um número para gerar sua tabuada: "))

# Loop para gerar a tabuada
for i in range(1, 11):
  print(numero, "x", i, "=", numero*i)

#QUESTÃO 10


nomes = input("Digite uma lista de nomes, separados por vírgula: ").split(",") 

lista_sem_duplicados = list(set(nomes))

print("Lista sem nomes duplicados:", lista_sem_duplicados)








