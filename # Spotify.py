# Spotify.py


import pyautogui

# ira clicar no botao windows
pyautogui.press('win')
# o dois significa o tempo de espera em segundos
pyautogui.sleep(2)
# digitar este texto 
pyautogui.write("chrome")
pyautogui.sleep(2)
# apertar a tecla enter
pyautogui.press('enter')
pyautogui.sleep(2)
# digitar este texto 
pyautogui.write("spotify login e senha")
pyautogui.sleep(1)
# apertar o espaço para nao tem erro na pesquisa
pyautogui.press('space')
pyautogui.sleep(1)
# apertar a tecla enter
pyautogui.press('enter')
pyautogui.sleep(2)
# clicar no link 
pyautogui.click(pyautogui.position())
pyautogui.sleep(1)
# rolagem do mouse para baixo
pyautogui.scroll(-600, x=0, y=0) 
pyautogui.sleep(1)
pyautogui.click(pyautogui.position())
pyautogui.sleep(2)
# ira digitar o usuario
pyautogui.write("")
pyautogui.sleep(1)
# ira pressionar a tecla tab
pyautogui.press('tab')
pyautogui.sleep(1)
# ira digitar a senha
pyautogui.write("")
pyautogui.sleep(1)
# ira apertar o botao para não lembrar do usuario 
pyautogui.click(pyautogui.position())
pyautogui.sleep(1)
# ira pressionar a tecla tab
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(2)
# clicar para deixar o site em modo Web Player
pyautogui.click(pyautogui.position())