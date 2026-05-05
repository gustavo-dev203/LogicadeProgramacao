lista = ['gomes', 'fulano', 'cicrano', 'beltrano', 'lucas', 'matheus', 'pedro']

print(lista)

print(lista[0])

print(lista[-1])

print (lista [0:3])

lista.sort()

lista.append('karython')

lista.insert(2, 'joão')

lista.extend(['ana','beatriz','david','roberto'])

num = []
for i in range(10):
    num.append(i*2)
print(num)

print(f'Lista antes de remover: {lista}')

lista.pop(0)

lista.pop()

lista.remove('cicrano')

print(f'Lista depois de remover: {lista}')


lista_num = [n for n in range(1,11)]
print(f'Lista antes de remover: {lista_num}')
del lista_num[2:4]
print(f'Lista depois de remover: {lista_num}')


listanomes = ['gomes', 'fulano', 'cicrano', 'beltrano', 'lucas', 'matheus', 'pedro']
listanomes[1] = 'lucas'

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[i] * 2
print(numeros)



numeros = [n * 2 if n>20 else n for n in numeros]
print(numeros)

#for i in range(len(lista)):
#    print(f'{i+1}° valor da lista: {lista[i]}')
