from datetime import datetime, timedelta

import os
import time


def criarPasta():
    # variaveis de tempos
    data_atual = datetime.today()
    dia_anterior = data_atual - timedelta(1)
    anoAtual = dia_anterior.strftime('%Y')
    mesAtual = dia_anterior.strftime('%m')
    diaAtual = dia_anterior.strftime('%d')

    print(data_atual.strftime('%d/%m/%Y %H:%M:%S') +
          ' - Processo de criação de pasta iniciada.')

    try:
        # tenta criar os diretorios
        os.makedirs('./temp/{}/{}/{}'.format(anoAtual, mesAtual, diaAtual))
    except OSError:
        # em caso de erro criar somente a ultima pasta
        os.mkdir('./temp/{}/{}/{}'.format(anoAtual, mesAtual, diaAtual))

    print(data_atual.strftime('%d/%m/%Y %H:%M:%S') +
          ' - Processo de criação de pasta concluido.')

    time.sleep(5)
