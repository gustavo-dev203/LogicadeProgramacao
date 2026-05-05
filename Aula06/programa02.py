'''

Desenvolva um sistema de gerenciamente de Carros com realização do CRUD

'''
import os
import time

carros = []
proximo_id = 1

os.system('cls')
while True:
    print('\n============= Sistema de Carros 🚗 =============')
    print('1 - Cadastrar Carros')
    print('2 - Listar Carros')
    print('3 - Atualizar Carros')
    print('4 - Deletar Carros')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    os.system('cls')

    #create
    if opcao == '1':
        modelo = input('Digite o modelo do carro: ').title()
        preco = float(input('Digite o preço: '))
        marca = input('Digite a marca: ').title()

        carro = {
            "id"         : proximo_id,
            "modelo"    : modelo,
            "preco"      : preco,
            "marca"      : marca
        }

        carros.append(carro)
        proximo_id += 1

        print('✅ Carro Cadastrado com sucesso!')

        time.sleep(3)
        os.system('cls')

    #read
    elif opcao == '2':
        if not carros:
            print('❗Nenhum carro cadastrado.')
        else:
            print('\n 📋 Lista de carros')
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo {carro['modelo']} | Preço {carro['preco']} | Marca {carro['marca']}')


    #update
    elif opcao == '3':
        print('\n 📋 Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo {carro['modelo']} | Preço {carro['preco']} | Marca {carro['marca']}')

        id_busca = int(input('Digite o ID do carro para deletar: '))

        encontrado = False

        for carro in carros:
            if carro ['id'] == id_busca:
                novo_modelo = input('Digite o novo modelo: ').title()
                novo_preco = float(input('Digite o novo preço: ').replace(',', '.'))
                nova_marca = input('Digite a nova marca: ').title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = nova_marca

                print('✅ Carro atualizado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print('❌ Carro não encontrado!')

        time.sleep(3)
        os.system('cls')

    #delete
    elif opcao == '4':
        print('\n 📋 Lista de carros')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo {carro['modelo']} | Preço {carro['preco']} | Marca {carro['marca']}')

        id_busca = int(input('Digite o ID do carro para deletar: '))

        encontrado = False

        for carro in carros:
            if carro ['id'] == id_busca:
                carros.remove(carro)
                print('✅ Carro deletado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print('❌ Carro não encontrado!')

        time.sleep(3)
        os.system('cls')

    #Sair
    elif opcao == '0':
        total = 20
        barra =""
        print('Saindo do Sistema...')
        for i in range(1, total +1):
            barra +="🟩"
            porcentagem = int((i / total *100))
            vazio = "-" * (total -1)
            print(f'\r[{barra}] {porcentagem}%', end="")
            time.sleep(0.2)
        break

    else:
        print('❌ Opção inválida.')