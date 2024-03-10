from Estrategias import estrategia
from Tratamento_dos_Dados import PegarHistorico
from Conferir_Resultado import ConferirResultado
from Telegram import send_message
import time

bOperacao = 0
gale = 0

msg = "Iniciando...!\n'O futuro vai mostrar os resultados e julgar cada um segundo as suas realizações.' ~ Tesla, Nikola"

send_message(msg)

while True:

    lista = PegarHistorico()
    print(lista)
   
    if bOperacao == 0 and gale == 0:
        #Entrando na operação
        bOperacao, minha_posicao = estrategia(lista)
    else:
        #Conferindo o resultado da operação
        bOperacao, gale, minha_posicao = ConferirResultado(bOperacao, lista, minha_posicao, gale)

    time.sleep(2)