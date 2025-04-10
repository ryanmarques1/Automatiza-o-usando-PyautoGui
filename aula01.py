#Aula 01 Automações de Tarefas
#Passo a Passo:
    #Passo1: Entrar e Logar no sistema da empresa    https://dlp.hashtagtreinamentos.com/python/intensivao/login
    #Passo2: Importar a base de dados(planilhas excel ou arquivos .csv)
    #Passo3: Cadastrar um produto.
    #Passo4: Repetir o passo3 para o n-1 (produtos restantes)
    #produtos.
import pyautogui
import time
import pandas
pyautogui.PAUSE = 0.4 #COLOCANDO UM DELAY (em segundos) das chamadas de função.
#abrir o chrome
pyautogui.press("win") #Apertando uma tecla;
pyautogui.write("Brave") #Escrevendo um texto;
pyautogui.press("enter") #entrando no browser
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #escrevendo a url
pyautogui.press("enter") #entrando no site
#pyautoguMOLO000251 Logitech    Mouse   1   25.95   6.5 i.hotkey("ctrl", "c")

#esperar o site carregar
time.sleep(2.5) #delay de 2.5 segundos no código.


#Fazendo login no site

pyautogui.click(x=788, y=468) #pos x,y do campo email
pyautogui.write("ryan123@gmail.com") #digitando no campo email
#uma outra forma seria apertando a tecla tab para ir pro campo senha
#pyautogui.press("tab")
pyautogui.click(x=664, y=581) #pos x,y do campo senha
pyautogui.write("ryan123") #digitando no campo senha
pyautogui.click(x=965, y=660) #pos x,y, para clique no logar

time.sleep(2.5)

#importando a base de dados


tabela = pandas.read_csv("produtos.csv") #lendo o arquivo csv

#print(tabela)

#colocando os dados no form do site cadastrando os produtos


for linha in tabela.index: #.index para ir pegando os campos da tabela.
    pyautogui.click(x=670, y=308)
    codigo = tabela.loc[linha, "codigo"]  #localizar codigo na tabela. <var>.loc(linha,coluna)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000) #realizar rolagem do scroll, > 0 scroll para cima, < 0 scroll para baixo


#Encerrar automação
pyautogui.click(x=0, y=0)
print("Encerrando!")
    