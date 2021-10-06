# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:09:27 2021

@author: erick
"""

#Procedimento para a execução de arquivos não-executaveis
import subprocess 
import pyautogui
   

path_to_notepad = "C:/Program Files/Notepad++/notepad++.exe"
path_to_file = "C:/Users/erick/Projects/Toyota/appcrawler/teste.txt"

p = subprocess.Popen([path_to_notepad, path_to_file]) #Executa programa

pyautogui.moveTo(100, 150) #Sera executado independente de programa estar aberto

returncode = p.wait() #Processo aguarda ate fechamento da janela
