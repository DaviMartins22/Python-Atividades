def analisar_lista(numeros):
    maior = max(numeros)
    menor = min(numeros)
    soma = sum(numeros)
    
    return maior, menor, soma


lista = []

# pedindo 5 números ao usuário
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    lista.append(num)

# chamando a função
maior, menor, soma = analisar_lista(lista)

print("\nResultados:")
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma total:", soma)