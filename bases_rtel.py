from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

import time


def baixar_arquivos():
    # Campanhas
    carteira_id = [14, 19, 18, 10]
    carteira_rtel = [62, 75, 74, 69]

    # Data e nome do arquivo que será baixado
    data_atual = datetime.today()
    dia_anterior = data_atual - timedelta(6)
    data_nome = dia_anterior.strftime('%Y%m%d')

    # Acessando o site e baixando os arquivos
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://172.26.0.166/Atom/')
    time.sleep(1)
    driver.find_element(By.ID, 'login').send_keys('edgar.lima')
    driver.find_element(By.ID, 'password').send_keys('254580ea')
    driver.find_element(By.ID, 'efetuar_login').click()
    time.sleep(1)
    driver.get('http://172.26.0.166/Atom/campanhas/painel')

    # Download do RTEL
    for i in carteira_rtel:
        driver.get(
            'http://172.26.0.166/Atom/campanhas/devolucoes/downloadFile/{}/2//Devolucao_{}_{}.zip'.format(
                carteira_id[carteira_rtel.index(i)], i, data_nome))
        # print('Devolucao_{}_{}.zip'.format(i, data_nome))
        time.sleep(2)

    print(data_atual.strftime('%d/%m/%Y %H:%M:%S') +
          ' - Processo de download de arquivo RTEL concluido.')

    time.sleep(10)
