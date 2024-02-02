from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

import pandas as pd


# os.system("clear")

i = 10
id_c = 7

driver = webdriver.Firefox()
driver.get("http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/spabr.def")
arquivo = driver.find_element("name","Arquivos")
box_arquivo = Select(arquivo)
tam = len(box_arquivo.options)

while i<tam:
    original_window = driver.current_window_handle
    "Selecionando Município"
    linha = driver.find_element("name","Linha")
    box_linha = Select(linha)
    opt_linha = box_linha.options[0]
    opt_linha.click()
    opt_linha.click()

    "Selecionando Conteúdo"
    incremento = driver.find_element("name","Incremento")
    box_incremento = Select(incremento)
    ActionChains(driver).double_click(box_incremento.options[0]).perform()
    # opt_incremento = box_incremento.options[0]
    # opt_incremento.click()
    # opt_incremento = box_incremento.options[2]
    # opt_incremento.click()
    

    "Selecionando Coluna"
    coluna = driver.find_element("name","Coluna")
    box_coluna = Select(coluna)
    opt_coluna = box_coluna.options[id_c]
    opt_coluna.click()

    "Selecionando Arquivos"
    arquivo = driver.find_element("name","Arquivos")
    box_arquivo = Select(arquivo)
    opt_arquivo =  box_arquivo.options[i]
    # ActionChains(driver).double_click(opt_arquivo).perform()
    if i != 0:
        ActionChains(driver).key_down(Keys.CONTROL).click(box_arquivo.options[0]).key_up(Keys.CONTROL).perform()
    opt_arquivo =  box_arquivo.options[i]
    opt_arquivo.click()
    if i ==0:
        opt_arquivo.click()
    

    #Botão linhas vazias
    botao = driver.find_element('name','zeradas')
    botao.click()

    ano = '20'+opt_arquivo.text[6:8]
    mes = opt_arquivo.text[0:3]

    "Encontrando o botão"
    button = driver.find_element("name", "mostre")
    button.click()


    sleep(20)

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # elem = driver.find_element(By.CLASS_NAME,"botao_opcao")
    # print(elem.text)
    elem = driver.find_element(By.XPATH,"(//a)[1]")
    # Obtém o valor do href
    href = elem.get_attribute("href")

    # Imprime o valor do href

    df = pd.read_csv(href,sep=';', encoding='latin-1',skiprows=3,on_bad_lines='skip')
    df["ano"] = ano
    df["mes"] = mes
    nome_arqui = "Municipio_"

    nome_arqui+= "Subgrupo_Procedimento_"
    
    nome_arqui+= mes+ano+".csv"

    df.to_csv(nome_arqui)
    i+=1
    driver.quit()
    
    # os.system("clear")


    driver = webdriver.Firefox()
    driver.get("http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/spabr.def")




