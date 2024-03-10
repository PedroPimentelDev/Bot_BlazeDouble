from Telegram import send_message

def estrategia(lista):
    bOperacao = 0
    minha_posicao = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]

    def bOrelinha_Preta():
        nonlocal bOperacao, minha_posicao
        if lista[0] == "WHITE" and lista[1] == "BLACK":
            msg = "🤑 ENTRE AGORA! 🤑\n➡️ Entrar no ⚫(Preto) Após o branco \n➡️ Com proteção no ⚪(Branco)\n🚨 Realizar até 2 gale"
            send_message(msg)
            bOperacao = 1
        return(bOperacao)

    def bOrelinha_Vermelha():
        nonlocal bOperacao, minha_posicao
        if lista[0] == "WHITE" and lista[1] == "RED":
            msg = "🤑 ENTRE AGORA! 🤑\n➡️ Entrar no 🔴(Vermelho) Após o branco\n➡️ Com proteção no ⚪(Branco)\n🚨 Realizar até 2 gale"
            send_message(msg)
            bOperacao = 2
        return(bOperacao)

    def bDobradinha_Preto():
        nonlocal bOperacao, minha_posicao
        if lista[0] == "BLACK" and lista[1] == "BLACK" and lista[2] == "RED" and lista[3] == "RED":
            msg = "🤑 ENTRE AGORA! 🤑\n➡️ Entrar no 🔴(Vermelho) Após o: ⚫" + str(lista[0]) + "\n➡️ Com proteção no ⚪(Branco)\n🚨 Realizar até 2 gales"
            send_message(msg)
            bOperacao = 2
        return(bOperacao)


    def bDobradinha_Vermelho():
        nonlocal bOperacao, minha_posicao
        if lista[0] == "RED" and lista[1] == "RED" and lista[2] == "BLACK" and lista[3] == "BLACK":
            msg = "🤑 ENTRE AGORA! 🤑\n➡️ Entrar no ⚫(Preto) Após o: 🔴" + str(lista[0]) + "\n➡️ Com proteção no ⚪(Branco)\n🚨 Realizar até 2 gales"
            send_message(msg)
            bOperacao = 1
        return(bOperacao)


    def bDoisUmDois_Preto():
        nonlocal bOperacao, minha_posicao
        if lista[0] == "BLACK" and lista[1] == "BLACK" and lista[2] == "RED" and lista[3] == "BLACK" and lista[4] == "BLACK":
            msg = "🤑 ENTRE AGORA! 🤑\n➡️ Entrar no 🔴(Vermelho) Após o: ⚫" + str(lista[0]) + "\n➡️ Com proteção no ⚪(Branco)\n🚨 Realizar até 2 gales"
            send_message(msg)
            bOperacao = 2
        return(bOperacao)
    

    def bDoisUmDois_Vermelho():
        nonlocal bOperacao, minha_posicao
        if lista[0] == "RED" and lista[1] == "RED" and lista[2] == "BLACK" and lista[3] == "RED" and lista[4] == "RED":
            msg = "🤑 ENTRE AGORA! 🤑\n➡️ Entrar no ⚫(Preto) Após o: 🔴" + str(lista[0]) + "\n➡️ Com proteção no ⚪(Branco)\n🚨 Realizar até 2 gales"
            send_message(msg)
            bOperacao = 1
        return(bOperacao)

    bOrelinha_Preta()
    bOrelinha_Vermelha()
    bDobradinha_Preto()
    bDobradinha_Vermelho()
    bDoisUmDois_Preto()
    bDoisUmDois_Vermelho()

    return (bOperacao, minha_posicao)  