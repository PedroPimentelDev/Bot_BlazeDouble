from Telegram import send_message

win = 0
loss = 0
gale = 0
white = 0
saldo = 0
porcentagem = float

def ConferirResultado(bOperacao, lista, minha_posicao, gale):
    global win, loss, white, saldo, porcentagem # Declarando todas as variáveis globais
    posicao_atual = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]

    if bOperacao == 1 and minha_posicao != posicao_atual and (lista[0] == "BLACK"):
        bOperacao = 0
        win += 1
        gale = 0
        saldo += 20
        porcentagem = (win/(win+loss)*100) 
        msg = "🏆🏆WIN!🏆🏆\n +1 Sinal pra conta✅\nParcial: " +str(win) + " ✅| " + str(loss) + " ❌|" + str(white) + " ⚪|" + str(round(porcentagem)) + "%" +" de acerto" + "\nEvolução patrimonial: " +str(saldo) + "R$"+ " 📈"
        send_message(msg)
            
    if bOperacao == 2 and minha_posicao != posicao_atual and (lista[0] == "RED"):
        bOperacao = 0
        gale = 0
        win += 1
        saldo += 20
        porcentagem = (win/(win+loss)*100)
        msg = "🏆🏆WIN!🏆🏆\n +1 Sinal pra conta✅\nParcial: " +str(win) + " ✅| " + str(loss) + " ❌|" + str(white) + " ⚪|" + str(round(porcentagem)) + "%" +" de acerto" + "\nEvolução patrimonial: " +str(saldo) + "R$"+ " 📈"
        send_message(msg) 
 

    if (bOperacao == 1 or bOperacao == 2) and minha_posicao != posicao_atual and (lista[0] == "WHITE"):
        white += + 1    
        bOperacao = 0
        gale = 0
        win += 1
        saldo += 40
        porcentagem = (win/(win+loss)*100)
        msg = "🏆🏆WIN!🏆🏆\n +1 Sinal pra conta✅\nParcial: " +str(win) + " ✅| " + str(loss) + " ❌|" + str(white) + " ⚪|" + str(round(porcentagem)) + "%" +" de acerto" + "\nEvolução patrimonial: " +str(saldo) + "R$"+ " 📈"
                        
    if bOperacao == 1 and minha_posicao != posicao_atual and lista[0] == "RED" and gale == 0:
        bOperacao = 1
        gale += 1
        msg = "🚨🚨Vamos para o gale 1!🚨🚨\nSeguindo o gerenciamento✅"
        send_message(msg) 
        minha_posicao = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] 

    if bOperacao == 2 and minha_posicao != posicao_atual and lista[0] == "BLACK" and gale == 0:
        bOperacao = 2
        gale += 1
        msg = "🚨🚨Vamos para o gale 1!🚨🚨\n Seguindo o gerenciamento✅"
        send_message(msg) 
        minha_posicao =  lista[0] + lista[1] + lista[2] + lista[3] + lista[4] 

    if bOperacao == 1 and minha_posicao != posicao_atual and lista[0] == "RED" and gale == 1:
        bOperacao = 1
        gale += 1
        msg = "🚨🚨Vamos para o gale 2!🚨🚨\nSeguindo o gerenciamento✅"
        send_message(msg)
        minha_posicao = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]  

    if bOperacao == 2 and minha_posicao != posicao_atual and lista[0] == "BLACK" and gale == 1:
        bOperacao = 2
        gale += 1
        msg = "🚨🚨Vamos para o gale 2!🚨🚨\n Seguindo o gerenciamento✅"
        send_message(msg)
        minha_posicao = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]      

    if bOperacao == 1 and minha_posicao != posicao_atual and lista[0] == "RED" and gale == 2:
        bOperacao = 0
        gale = 0
        loss += 1
        saldo -= 256
        porcentagem = (win/(win+loss)*100)
        msg = "❌❌LOSS!❌❌\nNão desanime, com o gerenciamento em dia nem sentimos o loss"
        send_message(msg)
        msg = "Parcial: " +str(win) + " ✅| " + str(loss) + " ❌|" + str(white) + " ⚪|" + str(round(porcentagem)) + "%" +" de acerto" + "\nEvolução patrimonial: " +str(saldo) + "R$"+ " 📉\n🦸🏻🦸🏻ATIVANDO MODO DE RECUPERAÇÃO!🦸🏻‍♂️🦸🏻‍♂️"
        send_message(msg)
 

    if bOperacao == 2 and minha_posicao != lista[0] + lista[1] + lista[2] + lista[3] + lista[4] and lista[0] == "BLACK" and gale == 2:
        bOperacao = 0
        gale = 0
        loss += 1
        saldo -= 256
        porcentagem = (win/(win+loss)*100)
        msg = "❌❌LOSS!❌❌\nNão desanime, com o gerenciamento em dia nem sentimos o loss"
        send_message(msg)     
        msg = "Parcial: " +str(win) + " ✅| " + str(loss) + " ❌|" + str(white) + " ⚪|" + str(round(porcentagem)) + "%" +" de acerto" + "\nEvolução patrimonial: " +str(saldo) + "R$"+ " 📉\n🦸🏻🦸🏻ATIVANDO MODO DE RECUPERAÇÃO!🦸🏻‍♂️🦸🏻‍♂️"
        send_message(msg)
    return(bOperacao, gale, minha_posicao)