# pede um número ao usuário
numero = int(input("Digite um número: "))

print(f"\nTabuada do {numero}:\n")

# faz a tabuada de 1 até 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")