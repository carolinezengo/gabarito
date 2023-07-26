#Passo a passo
#Passo1: Entrar no sitema da empresa 
#"https://dlp.hashtagtreinamentos.com/python/intensivao/login")
import pyautogui
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


#Passo2:Fazer Login
#Passo3: Importar a base Produto
#Passo 4: Cadastrar um produto
#Passo5: Repetir o processo de cadastro ate o fim 


