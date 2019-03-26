from tkinter import *

def ver():
	if ed1.get() == "teste" and ed2.get() == "teste":
		print("LOGADO COM SUCESSO!!!")
		
	else:
		print("LOGIN OU SENHA INVALIDOS!!!")
		
	
	
janela = Tk()
 
janela.title("LOGIN") 
 

lb1 = Label(janela, text="Senha: ")
lb2 = Label(janela, text="Login: ")

ed1 = Entry(janela) 
ed2 = Entry(janela, show="*")

bt1 = Button(janela, text="Confirmar", command= ver)

lb2.grid(row=0, column=0)
lb1.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=1)


janela.geometry("200x100+100+100")

 
janela.mainloop()
