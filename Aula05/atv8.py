#Questão08
"""
nome1 = input("Digite o primeiro nome: ")
sobrenome1 = input("Digite o sobrenome correspondente: ")

nome2 = input("Digite o segundo nome: ")
sobrenome2 = input("Digite o sobrenome correspondente: ")

print(nome1,sobrenome2 ,",", nome2,sobrenome1)
"""

nome1 = input("Digite o primeiro nome completo: ")
nome2 = input("Digite o segundo nome completo: ")

#separando o nome do sobrenome 
parte1 = nome1.split()
parte2 = nome2.split()

#pegar o primeiro nome e sobrenome
primeiroNome1 = parte1[0]
sobrenome1 = parte1 [-1]

primeiroNome2 = parte2[0]
sobrenome2 = parte2 [-1]

novoNome1 = primeiroNome1 + " " + sobrenome2
novoNome2 = primeiroNome2 + " " + sobrenome1

print(novoNome1)
print(novoNome2)