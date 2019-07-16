from tkinter import *


window = Tk()

#-------------- APARENCIA
window.title("CRIANDO")
window.geometry('1000x1000')

#-------------- LABEL
window.title("Bem-vindo")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

#-------------- BUTTON
def clicked():
    response = in_txt.get()
    response_select = select.get()
    response_check = check_box.get()
    response_radio = valor_1.get()
    response_textarea = textarea.get(1.0, END)
    response_caixa_numero = caixa_numero.get()

    lbl.configure(text=response_caixa_numero)

btn = Button(window, command=clicked ,text="Click", bg="black", fg="white")
btn.grid(column=1, row=7)

#-------------- INPUT
in_txt = Entry(window, width=10)
# in_txt = Entry(window, width=10, state='disable') #->DESATIVA O CAMPO
in_txt.grid(column=1, row=1)

in_txt.focus() #Da foco assim que abre

#-------------- SELECT
from tkinter.ttk import *
select = Combobox(window)
select['values'] = (1, 2, 3, 4, 5, "Text")
select.grid(column=1, row=2)

# combo.current(2) #-> Deixa pré-selecionado

#-------------- CHECK BUTTON
from tkinter.ttk import *
check_box = BooleanVar()
# check_box.set(1) #-> Define um valo default

check = Checkbutton(window, text='Teste', var=check_box)
check.grid(column=1, row=3)

#-------------- RADIO BUTTONS
from tkinter.ttk import *
valor_1 = StringVar()

rad1 = Radiobutton(window,text='UM', value='PRIMEIRO VALOR', var=valor_1)
# rad1 = Radiobutton(window,text='UM', value=1) #-> Funciona como um button
rad2 = Radiobutton(window,text='DOIS', value=2)
rad3 = Radiobutton(window,text='TRÊS', value=3)
 
rad1.grid(column=0, row=4)
rad2.grid(column=1, row=4)
rad3.grid(column=2, row=4)

#-------------- TEXT AREA
from tkinter import scrolledtext
textarea = scrolledtext.ScrolledText(window, width=15, height=10)
textarea.grid(column=0, row=5)

textarea.insert(INSERT, 'PLACEHOLDER')
# textarea.delete(1.0, END) #->Sem PLaceholder

#-------------- ALERT

from tkinter import messagebox
def click_alert():
    messagebox.showinfo('TITULO DA CAIXINHA', 'CONTEUDO DA CAIXINHA')
    #messagebox.showwarning('WARNING', 'CONTEUDO DA CAIXINHA')  #shows warning message
    #messagebox.showerror('ERRO', 'CONTEUDO DA CAIXINHA')    #shows error message
    #messagebox.askquestion('DUVIDA','Message content')
    #messagebox.askyesno('SIM NAO','Message content')
    #messagebox.askyesnocancel('SIM NAO CANCELAR','Message content')
    #messagebox.askokcancel('CACELAR','Message content')
    #messagebox.askretrycancel('REPETIR','Message content')

btn_alert = Button(window,text='Alerta', command=click_alert)
btn_alert.grid(column=1, row=9)

#-------------- NUMERO INPUT
caixa_numero = Spinbox(window, from_=0, to=100, width=10)
caixa_numero.grid(column=1, row=10)

# var =IntVar()
# var.set(36)
# caixa_numero = Spinbox(window, from_=0, to=100, width=10, textvariable = var) #->Valor Default

#-------------- PROGRESS BAR
from tkinter.ttk import Progressbar
from tkinter import ttk
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background="black")
progress_bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
progress_bar['value'] = 70
progress_bar.grid(column=0, row=12)

#-------------- UPLOAD ARQUIVOS
from tkinter import filedialog
# file = filedialog.askopenfilename()
# files = filedialog.askopenfilenames()
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*"))) #->Especificando o tipo de arquivo

# from os import path
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__)) #->PATH NATIVO DO ARQUIVO

#-------------- MENU ARQUIVOS
from tkinter import Menu
menu = Menu(window)
menu.add_command(label='File')
window.config(menu=menu)

menu_topo = Menu(window)
menu_cascata = Menu(menu_topo)
menu_cascata.add_command(label='COMANDO CASCATE')
# menu_cascata.add_command(label='COMANDO CASCATE', command=FUNCÇÃO COM O CLICK)

menu_topo.add_cascade(label='COMANDO', menu=menu_cascata)
window.config(menu=menu_topo)

#-------------- GUIAS DE NAVEGAÇÃO - FUNCIONA SEM DEFINIR TODOS OS ITENS NA WINDOW
from tkinter import ttk
controle_navegacao = ttk.Notebook(window)

barra1 = ttk.Frame(controle_navegacao)
barra2 = ttk.Frame(controle_navegacao)

controle_navegacao.add(barra1, text="BARRA UM")
controle_navegacao.add(barra2, text="BARRA DOIS")

barra1_label = Label(barra1, text='AQUI JÁS BARRA 1')
barra1_label.grid(column=0, row=0)
barra2_label = Label(barra2, text='AQUI JÁS BARRA 2')
barra2_label.grid(column=0, row=0)

controle_navegacao.pack(expand=1, fill='both')



window.mainloop()