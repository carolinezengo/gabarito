#Passo a passo
#Passo1: Entrar no sitema da empresa 
#"https://dlp.hashtagtreinamentos.com/python/intensivao/login")
import pyautogui
import time

#pyautogui.write -> escrever um texto
#pyautogui.press -> aperta 1 tecla
#pyautogui.click -> clicar em algum lugar tela
#pyautogui.hotkey -> junçao de teclas 
pyautogui.PAUSE = 0.5
#abrir p navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)


#Passo2:Fazser Login
pyautogui.click(x=757, y=478)
pyautogui.write("carolzinha_blue@hotmail.com")
pyautogui.press("tab")
pyautogui.write("050404")
pyautogui.click(x=640, y=633)
time.sleep(3)

#Passo3: Importar a base Produto
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#Passo 4: Cadastrar um produto
#Passo5: Repetir o processo de cadastro ate o fim 


