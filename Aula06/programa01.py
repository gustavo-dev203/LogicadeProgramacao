'''
1. Crie um programa que o usuário possa digitar quantos número quiser
e ao terminar imprima a lista em ordem crescente.

2. Crie um programa que o usuário possa digitar a quantidade desejada de notas de um determinado aluno (nota minima 0 nota maxima 10) e o programa calcule a media desse aluno, e ao final imprima se o aluno está (aprovado >= 7, reprovado, recuperação >= 5).
'''

# #Programa 01:
import os
lista_num = []

while True:
    num = int(input('Digite o número: '))
    lista_num.append(num)
    opcao = input("Deseja adicionar mais? (s - sim) ou enter para parar!").lower()
    os.system('cls')
    if opcao != 's':
        break

lista_num.sort()
print(lista_num)

#Programa 02:
lista_notas = []

while True:
    nota = float(input('Digite a nota: '))
    if 0 <= nota <= 10:
        lista_notas.append(nota)
    else:
        print('Nota inválida')
        break
    opcao = input("Deseja adicionar mais? (s - sim) ou enter para parar!").lower()
    os.system('cls')
    if opcao != 's':
        break

if lista_notas:
    media = sum(lista_notas) / len(lista_notas)

    print(f'A média do aluno foi: {media}')

    if media >= 7:
        print('APROVADO')
    elif media >=5:
        print('RECUPERAÇÂO')
    else:
        print('REPROVADO')
else:
    print('Nenhuma nota registrada.')



