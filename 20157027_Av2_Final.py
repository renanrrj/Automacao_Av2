# David Renan
# Pedro Corrêa

# OBS instalar openpyxl, webdriver-manager e selenium

# Importação de módulos
import openpyxl as opx
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
import csv


# Seleciona o driver mais atualizado do webdriver e instala para previnir erros de atualização e versão do navegador.
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Acessando site
navegador.get('https://www.google.com/')


#Acessando a busca
navegador.find_element(By.NAME, 'q').send_keys('tempo agora Itatiaia-RJ')

# Tempo para carregamento da pagina completa
time.sleep(3)

# Acessando o botao
navegador.find_element(By.NAME, 'btnK').click()

# Encontrar temperatura
texto = navegador.find_element(By.ID, 'wob_tm').text
data = date.today()



# ------------------------------------------------------------------------------------------------

#! VERIFICANDO SE O ARQUIVO EXISTE OU NÃO

plan = ""
try : #EXISTE ===> EDITAR
    plan = opx.load_workbook(filename = 'Planilha de temperaturas.xlsx')

    # Selecionando uma página
    pag_tempo = plan['Temperaturas']
except: #NÃO EXISTE ===> CRIAR
    # Criando planilha
    plan = opx.Workbook()

# Renomeando aba
    plan.active.title = "Temperaturas"   

    # Selecionando uma página
    pag_tempo = plan.active

    # Inserindo registros
    pag_tempo.append(['Data', 'Temperatura'])
pag_tempo.append([data, texto])

# Salvar planilha
plan.save ('Planilha de temperaturas.xlsx')