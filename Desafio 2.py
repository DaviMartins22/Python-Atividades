print("Boa tarde, O que você deseja ?")

estado_luz = "desligado"
estado_ar_condicionado = "desligado"
estado_janela = "fechado"

while True:
    acao = input("Você quer 'ligar luz', 'desligar luz', 'ligar ar condicionado', 'desligar ar condicionado', 'abrir janela', 'fechar janela' ou 'sair':").lower()
    if acao == "ligar luz":
        if estado_luz == "desligado":
            print("Luz ligada")
            estado_luz = "ligado"
        else:
            print("A luz já está ligada")

    elif acao == "desligar luz":
        if estado_luz == "ligado":
            print("Luz desligada")
            estado_luz = "desligado"
        else:
            print("A luz já está desligada")

    elif acao == "abrir janela":
        if estado_janela == "fechado":
            print("Janela aberta")
            estado_janela = "aberto"
        else:
            print("A janela já está aberta")

    elif acao == "fechar janela":
        if estado_janela == "aberto":
            print("Janela fechada")
            estado_janela = "fechado"
        else:
            print("A janela já está fechada")

    elif acao == "ligar ar condicionado":
        if estado_ar_condicionado == "desligado" and estado_janela == "fechado":
            print("Ar condicionado ligado")
            estado_ar_condicionado = "ligado"
        else:
            print("Não ligue o ar condicionado com a janela aberta")

    elif acao == "desligar ar condicionado":
        if estado_ar_condicionado == "ligado":
            print("Ar condicionado desligado")
            estado_ar_condicionado = "desligado"
        else:
            print("O ar condicionado já está desligado")

    if acao == "sair":
        print("Desligando, até já!")
        break