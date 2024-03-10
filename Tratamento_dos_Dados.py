from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

lista = []
preto = "|11|10|9|8|14|13|12|"
vermelho = "|5|6|7|1|2|3|4|"

def PegarHistorico():
    # Acessando o site
    
    # service = Service(executable_path=r"") Até o momento da criação desse código não havia um chromedriver disponivel para download

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # Alternativa para o erro de cima
    driver.get("https://kitblaze.com/double/")
    lista = driver.find_element(By.XPATH, '//*[@id="listagem_giros"]').text.replace('\n', "|")
    lista = lista.split('|')
    lista_revertida = list(reversed(lista))
    
    #Filtrando os dados contidos na lista
    i = 0
    while i < len(lista_revertida):
        if ':' in lista_revertida[i]:
            lista_revertida.pop(i)
        else:
            i += 1  

    #Adicionando cores a lista
    for i in range(10):
        if preto.find("|"+lista_revertida[i]+"|") > -1:
            lista_revertida[i] = "BLACK"

        elif vermelho.find("|"+lista_revertida[i]+"|") > -1:
            lista_revertida[i] = "RED"

        else:
            lista_revertida[i] = "WHITE"
    return(lista_revertida)