'''
    Programa 01 - Aula04 - 28/04/2026
    Prof: Karython Gomes
    Turma 2° Desenvolvimento de Sitemas

    Sistema de sorteios 1.0
'''

import time
import random

lista_nomes = ['Gustavo Campos', 'Nicollas Sanches', 'Maria Eduarda', 'Alexandre Fialho', 'Fábio Dorminhoco','Ana Silva', 'Bruno Souza', 'Carla Oliveira', 'Diego Santos', 'Elena Costa', 'Felipe Pereira', 'Giovana Lima', 'Hugo Ribeiro', 'Isabela Melo', 'João Rocha','Karen Alves', 'Leonardo Dias', 'Marcos Pires', 'Nathalia Cruz', 'Otávio Guerra', 'Paula Vicari', 'Quiteria Lins', 'Rafael Montenegro', 'Sabrina Paiva', 'Thiago Mendes', 'Ursula Bittencourt', 'Vitor Hugo', 'Wagner Moura', 'Xavier Nunes', 'Yago Fernandes', 'Zilda Cardoso', 'Alice Nogueira', 'Beto Carrero', 'Caio Castro', 'Duda Beat']

lista_sorteados = []

sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    time.sleep(5)
    print(f'\nSorteado: {nome_sorteado}!')
    lista_sorteados.append(nome_sorteado)
    print(f'Lista antes de remover {len(lista_nomes)}')
    lista_nomes.remove(nome_sorteado)
    print(f'Lista atualizada {len(lista_nomes)}')
    sorteados +=1

print('Fim do Programa.')
