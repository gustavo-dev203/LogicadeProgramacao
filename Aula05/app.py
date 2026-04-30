# Questão 01:
'''
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
divi = num2/num1
print(f'O resultado da divisão ente {num1} e {num2} é {divi:.2f}')

'''

nome1 = input('Digite o primeiro nome completo: ')
nome2 = input('Digite o segundo nome completo: ')

parte1 = nome1.split()
parte2 = nome2.split()

primeiro_nome = parte1[0]
sobrenome1 = parte1[-1]

segundo_nome = parte2[0]
sobrenome2 = parte2[-1]

novo_nome1 = primeiro_nome + ' ' + sobrenome2
novo_nome2 = segundo_nome + ' ' + sobrenome1

print(novo_nome1)
print(novo_nome2)
