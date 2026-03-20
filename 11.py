# dicionário com produtos e preços
produtos = {
    "arroz": 5.50,
    "feijao": 7.20,
    "leite": 4.30,
    "pao": 1.00,
    "cafe": 9.90
}

# pede o nome do produto
busca = input("Digite o nome do produto: ").lower()

# verifica se existe no dicionário
if busca in produtos:
    print(f"Preço do {busca}: R$ {produtos[busca]:.2f}")
else:
    print("Não Encontrado")