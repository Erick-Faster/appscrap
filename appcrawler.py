# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 08:36:43 2021

@author: erick
"""

import pyautogui
import pywinauto
import pyperclip
import sys

def scrap_data():
    
    #Path
    path_exe = "C:/Program Files/Notepad++/notepad++.exe"
    path_file = "C:/Users/erick/Projects/Toyota/appcrawler/teste.txt"
    app = pywinauto.Application().start(f"{path_exe} {path_file}")
    
    #Parameters
    pyautogui.PAUSE = 1.0
    
    #Selecao do texto
    pyautogui.click(100, 200)
    pyautogui.press(['pageup', 'home', 'down','down'])
    
    with pyautogui.hold('shift'):
        pyautogui.press(['pagedown', 'home', 'up'])
    
    pyautogui.hotkey('ctrl', 'c')
    
    #Armazenamento
    paste = pyperclip.paste()
    
    #Encerramento de aplicação
    pyautogui.press(['pagedown'])
    pyautogui.write('Success! =)', interval=0.10)
    app.kill()
    
    #Tratamento dos dados
    elements = paste.split('\n')
    elements = elements[:-1]
    
    #Transformacao em Dicionario
    results = dict((x.strip(), y.strip()) 
        for x, y in (element.split(': ') 
        for element in elements))

    return results

def main():
    
    screen_size = pyautogui.size()
    mouse_position = pyautogui.position()
    
    confirm = pyautogui.confirm(text='Os dados serão processados. Recomenda-se não interagir com o computador até o termino da operação. Deseja continuar?', title='Mensagem', buttons=['OK', 'Cancel'])

    if confirm == 'OK':
        data = scrap_data()
        pyautogui.alert(text='Dados extraídos com sucesso =)', title='Mensagem', button='OK')
        print(data)
    else:
        sys.exit()
        
main()

