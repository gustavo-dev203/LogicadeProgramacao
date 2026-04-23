# NOTE: Boletim Escolar 2.0

print(30*"=", "Boletim Esolar", 30*"=")
lista_notas = []
Nome = input("Digite o nome do aluno: ").title()
curso = input("Digite o curso: ").upper()
while True:
    nota = input("Digite uma nota: ")
    nota = float (nota)
    lista_notas.append(nota)
    print(lista_notas)
    opcao = input("Deseja adicionar mais notas? (s - Sim | s - Não): ").lower()
    if opcao == "n":
        break 
media = sum(lista_notas) / len(lista_notas)
print("Sua média é: ", media)