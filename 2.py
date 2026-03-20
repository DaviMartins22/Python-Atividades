# Programa para calcular desconto de um produto

preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = (preco * desconto) / 100
novo_preco = preco - valor_desconto

print("Valor do desconto: R$", valor_desconto)
print("Novo preço com desconto: R$", novo_preco)