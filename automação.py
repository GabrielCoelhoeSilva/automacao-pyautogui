# IMPORTAR AS BIBLIOTECAS
import pandas as pd
import time
import pyautogui


# IMPORTAR A BASE DE DADOS
tabela = pd.read_csv('produtos.csv')
print(tabela)

pyautogui.PAUSE = 1
# ABRIR O SISTEMA DA EMPRESA
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.click(x=696, y=473, duration=1)
pyautogui.write('emaildeexemplo@gmail.com')
pyautogui.press('tab')
pyautogui.write('senhanaoreal')
pyautogui.press('tab')
pyautogui.press('enter')

#CADASTRO DOS PRODUTOS
for linha in tabela.index:
    pyautogui.click(x=754, y=327, duration=1)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'custo']): # VERIFICA SE EXISTE INFORMAÇÃO EM OBS, CASO CONTRÁRIO NÃO PREENCHE
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)
