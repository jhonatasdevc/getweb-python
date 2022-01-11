import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import urllib
from selenium.webdriver.common.by import By
import pandas as pd
import random
from pathlib import Path
import winsound

listaCnpj = []
arquivo = open('C:\\Users\\Jhon\Desktop\\listacocamar.txt', 'r')
for linha in arquivo:
    listaCnpj.append(linha.rstrip("\n"))
    
arquivo.close()

cnpj = ''
comp = '122017'
senha = ''
navegador = ()
texto = ''
t1 = ''
tx = ''
# cnpj = 79114450000599
# comp = '07' + '2018'
# senha = 32213410

sl = [2.500, 2.300, 2.200, 2.100, 2.600, 2.700, 3.500, 4.100, 3.100, 3.900, 1.800, 5.100, 2.800]

tab1 = []
tab2 = []
tab3 = []
save = 'nao'


gpr = {'codigo pagamento':[], 'competencia':[],'identificador':[],'valor inss':[],'Outras Entidades': [],'Multa e Juros': [],'total':[],'bancaria':[], 'debito': []}
guia = []

def secondTime() : 
        # some_path = 'C:\\Users\\Jhon\\Desktop\\' + str(cnpj) + '.xlsx'
        # name = Path(some_path)  
        some_path = 'C:\\Users\\Jhon\\Desktop\\cocamar.xlsx'
        name = Path(some_path)
        df = pd.read_excel(name)
        dfNew = pd.DataFrame(gpr, columns=list(gpr.keys()))
        df = df.append(dfNew, ignore_index=True)
        df.to_excel (name, index = False, header=True)
        navegador.back()
        navegador.refresh()
        winsound.PlaySound("Ring01.wav", winsound.SND_ALIAS)
        
        
    

def firstTime() :
    some_path = 'C:\\Users\\Jhon\\Desktop\\' + str(cnpj) + '.xlsx'
    name = Path(some_path)
    df = pd.DataFrame(gpr, columns=list(gpr.keys()))
    df.to_excel (name, index = False, header=True)
    navegador.back()
    navegador.refresh()
    
for lc in range (len(listaCnpj)):
    gpr = {'codigo pagamento':[], 'competencia':[],'identificador':[],'valor inss':[],'Outras Entidades': [],'Multa e Juros': [],'total':[],'bancaria':[], 'debito': []}
    tab1 = []
    tab2 = []
    tab3 = []
    navegador = webdriver.Chrome()
    navegador.get("http://gps.receita.fazenda.gov.br/")
    navegador.find_element_by_id('formInicio:identificador').send_keys(listaCnpj[lc])
    navegador.find_element_by_id('formInicio:competencia').send_keys(comp)
    navegador.find_element_by_id('formInicio:senha').send_keys(32213410)
    print('digite captcha')
    cap = input()
    navegador.find_element_by_id('captcha_campo_resposta').send_keys(cap)
    navegador.find_element_by_id('formInicio:botaoConsultar').send_keys(u'\ue007')
    fr = 1
    for i in range(12): 
        tab1.append(navegador.find_element_by_xpath('//table[2]/tbody/tr[' + str(fr) + ']/td[3]').text)
        tab2.append(navegador.find_element_by_xpath('//table[2]/tbody/tr[' + str(fr) + ']/td[2]').text)
        tab3.append(navegador.find_element_by_xpath('//table[2]/tbody/tr[' + str(fr) + ']/td[5]').text)
        fr += 1
    contar1 = 1
    contar2 = 1    
    
    for i in range(12) :
        time.sleep(2)
        texto = navegador.find_element_by_xpath('//table[@class="tbbody"]/tbody/tr[' + str(i + 1) + ']/td[1]').text
        t1 = navegador.find_element_by_xpath('//*[@id="j_idt13"]/table[2]/tbody/tr[' + str(contar1) + ']/td[1]/a').text
        t2 = navegador.find_element_by_xpath('//*[@id="j_idt13"]/table[2]/tbody/tr[' + str(i + 1) + ']/td[2]').text
        if t2 == '': 
            print('vazio')
        else : 
            # if t1 == '13SL':
            #     if save == 0 : 
            #         firstTime()
            #     else :
            #         secondTime() 
            #     break
            tx = navegador.find_element_by_link_text(texto).click()
            r = int(tab2[i]) 
            contar1 += 1
            time.sleep(random.choice(sl))
            contar2 = 1
            for g in range(r) :
                time.sleep(random.choice(sl))
                texto = navegador.find_element_by_xpath('//table/tbody/tr[' + str(contar2) + ']/td[1]').text
                banc = navegador.find_element_by_xpath('//table/tbody/tr[' + str(contar2) + ']/td[4]').text
                tx = navegador.find_element_by_link_text(texto).click()
                time.sleep(random.choice(sl))
                contar2 += 1
                gpr['codigo pagamento'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[1]/td[3]').text)
                gpr['competencia'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]').text)
                gpr['identificador'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[3]/td[2]').text)
                gpr['valor inss'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[4]/td[3]').text)
                gpr['Outras Entidades'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[7]/td[4]').text)
                gpr['Multa e Juros'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[8]/td[3]').text)
                gpr['total'].append(navegador.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr/td/table/tbody/tr[9]/td[2]').text)
                gpr['bancaria'].append(banc)
                gpr['debito'].append(tab3[i])
                time.sleep(random.choice(sl))
                navegador.back()
            navegador.back()

    if save == 'sim' : 
       print('ok')
        
    else :
       some_path = 'C:\\Users\\Jhon\\Desktop\\cocamar.xlsx'
       name = Path(some_path)
       df = pd.read_excel(name)
       dfNew = pd.DataFrame(gpr, columns=list(gpr.keys()))
       df = df.append(dfNew, ignore_index=True)
       df.to_excel (name, index = False, header=True)
       
       #print("\n")
       #texto = input("Digite uma frase para acrescentar ao arquivo:\n")
       arquivo = open('C:\\Users\\Jhon\Desktop\\listaFeitosCocamar.txt','a')
       arquivo.write(listaCnpj[lc] + "\n")
       arquivo.close()
       navegador.back()
       navegador.refresh()
       winsound.PlaySound("Ring01.wav", winsound.SND_ALIAS)



#no google chrome, aperta f12 - crt+shift+p, screenShot

#name = 'nome arquivo'
#save = "C:\\Users\\Jhons\\Desktop\\" + str(name) + ".png"
#navegador.save_screenshot(save)
         

    
  








