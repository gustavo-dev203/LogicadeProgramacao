# for

#laço for, ele é finito: quando eu sei o numero de repetições

#frutas = ['melancia', 'abacaxi', 'melão', 'pera']
#fruta = 'melancia'

# for f in frutas:
   #print(f)

#for range (inicio, fim, salto)

#for _ in range(1, 20, 2):
    #print('Repeti')
'''
num = int(input("Escolha um número: "))
print(30*"=", f"Tabuada do {num}", 30*"=")

for i in range(11):
    print(f"{i} X {num} = {i * num}")

'''

lista_nomes = ['Gustavo Campos', 'Nicollas Sanches', 'Maria Eduarda', 'Alexandre Fialho', 'Fábio Dorminhoco','Ana Silva', 'Bruno Souza', 'Carla Oliveira', 'Diego Santos', 'Elena Costa', 'Felipe Pereira', 'Giovana Lima', 'Hugo Ribeiro', 'Isabela Melo', 'João Rocha','Karen Alves', 'Leonardo Dias', 'Marcos Pires', 'Nathalia Cruz', 'Otávio Guerra', 'Paula Vicari', 'Quiteria Lins', 'Rafael Montenegro', 'Sabrina Paiva', 'Thiago Mendes', 'Ursula Bittencourt', 'Vitor Hugo', 'Wagner Moura', 'Xavier Nunes', 'Yago Fernandes', 'Zilda Cardoso', 'Alice Nogueira', 'Beto Carrero', 'Caio Castro', 'Duda Beat']

for i, nome in enumerate(lista_nomes):
    print(f'{i+1}° {nome}')

nome_buscar = input("Digite um nome completo para buscar: ").title()

if nome_buscar in lista_nomes:
    print ("Usuário encontrado!")
else:
    print("Usuário não encontrado!")