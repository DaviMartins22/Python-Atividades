cadeia = input("Digite uma cadeia de 0 e 1: ")

for c in cadeia:
    if c != '0' and c != '1':
        print("Cadeia inválida! Use apenas 0 e 1.")
        exit()

estado = False

for simbolo in cadeia:
    if simbolo == '1':
        estado = True
    else: # simbolo == '0'
        estado = False

if estado:
    print("Estado final: q1")
    print("Cadeia Aceita! ")
else:
    print("Estado final: q0")
    print("Cadeia Rejeitada ")



