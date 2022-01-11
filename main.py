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

listaCnpj = [
    79114450000165,
79114450000408,
79114450000599,
79114450000750,
79114450000831,
79114450000912,
79114450001056,
79114450001137,
79114450001480,
79114450001560,
79114450001722,
79114450001803,
79114450002028,
79114450002370,
79114450002532,
79114450002613,
79114450002702,
79114450003008,
79114450003342,
79114450003423,
79114450004071,
79114450004314,
79114450004403,
79114450004586,
79114450004748,
79114450006520,
79114450007763,
79114450009200,
79114450010390,
79114450010470,
79114450012929,
79114450013305,
79114450013577,
79114450013658,
79114450013739,
79114450013810,
79114450014034,
79114450014115,
79114450014620,
79114450014700,
79114450014891,
79114450014972,
79114450015197,
79114450015278,
79114450015359,
79114450015510,
79114450015600,
79114450015944,
79114450016169,
79114450016320,
79114450016401,
79114450016592,
79114450016673,
79114450016754,
79114450016835,
79114450017050,
79114450017130,
79114450017211,
79114450017807,
79114450017998,
79114450018021,
79114450018102,
79114450018293,
79114450018374,
79114450018455,
79114450018536,
79114450018960,
79114450019001,
79114450019184,
79114450019265,
79114450019427,
79114450019850,
79114450020000,
79114450020190,
79114450020271,
79114450020352,
79114450020514,
79114450020603,
79114450020786,
79114450020867,
79114450020948,
79114450021081,
79114450021162,
79114450021405,
79114450021596,
79114450021677,
79114450021839,
79114450022053,
79114450022134,
79114450022215,
79114450022304,
79114450022487,
79114450022568,
79114450022649,
79114450022720,
79114450022800,
79114450022991,
79114450023025,
79114450023106,
79114450023297,
79114450023378,
79114450023459,
79114450023530,
79114450023610,
79114450023700,
79114450023963,
79114450024005,
79114450024188,
79114450024269,
79114450024340,
79114450024420,
79114450024692,
79114450024935,
79114450025079,
79114450025311,
79114450025400,
79114450025583,
79114450025664,
79114450025745,
79114450025826,
79114450025907,
79114450026121,
79114450026202,
79114450026393,
79114450026474,
79114450026555,
79114450026636,
79114450026717,
79114450026806,
79114450026989,
]

cnpj = ''
comp = ''
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
        winsound.PlaySound("Ring01.wav", winsound.SND_ALIAS)
        
    

def firstTime() :
    some_path = 'C:\\Users\\Jhon\\Desktop\\' + str(cnpj) + '.xlsx'
    name = Path(some_path)
    df = pd.DataFrame(gpr, columns=list(gpr.keys()))
    df.to_excel (name, index = False, header=True)
    navegador.back()
    navegador.refresh()
    

    
def my_function():  
    contar1 = 1
    contar2 = 1    
    
    for i in range(1) :
        time.sleep(2)
        texto = navegador.find_element_by_xpath('//table[@class="tbbody"]/tbody/tr[' + str(contar1) + ']/td[1]').text
        t1 = navegador.find_element_by_xpath('//*[@id="j_idt13"]/table[2]/tbody/tr[' + str(contar1) + ']/td[1]/a').text
        if t1 == '13SL':
            if save == 0 : 
                firstTime()
            else :
                secondTime() 
            break
        else :
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
        firstTime()
        
    else :
        secondTime() 
               
                

print("digite CNPJ: ")
cnpj = input()
print('Digite a competencia')
comp = input()
print('Digite a senha')
senha = input()
# print('primeira vez? digite sim ou nao')
# save = input()
navegador = webdriver.Chrome()
navegador.get("http://gps.receita.fazenda.gov.br/")
navegador.find_element_by_id('formInicio:identificador').send_keys(cnpj)
navegador.find_element_by_id('formInicio:competencia').send_keys(comp)
navegador.find_element_by_id('formInicio:senha').send_keys(senha)
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



my_function()


    
  








