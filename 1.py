# conversor de metros para cm e mm

# pede o valor pro usuário
metros = float(input("Digite a distância em metros: "))

# faz as contas
centimetros = metros * 100
milimetros = metros * 1000

# mostra o resultado
print("\nResultado:")
print(f"{metros} metro(s) = {centimetros} cm")
print(f"{metros} metro(s) = {milimetros} mm")