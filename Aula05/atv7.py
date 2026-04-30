#questao07
import os 
os.system("cls")

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

num1 = float(num1)
num2 = float(num2)

# um dos jeitos --> result = num1 > num2

#operador ternário
result = "num1 é maior" if num1 > num2 else "num1 é menor"

print(result)



"""if num1 > num2:
    print("O segundo número é menor que o primeiro!")
else:
    print("O primeiro número é menor que o segundo!")
"""
