import tkinter

text = []
arquivo = open('C:\\Users\\Jhon\Desktop\\listacocamar.txt', 'r')
for linha in arquivo:
    text.append(linha.rstrip("\n"))
    
arquivo.close()
print(text)

cnpj = 'nome'
#print("\n")
#texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('C:\\Users\\Jhon\Desktop\\listaFeitosCocamar.txt','a')
arquivo.write(cnpj + "\n")
arquivo.close()



main_window = tkinter.Tk()
tkinter.mainloop()
