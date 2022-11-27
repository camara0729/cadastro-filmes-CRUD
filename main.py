# Importanto bibliotecas necessárias

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from CRUD import *


# Cores utilizadas no projeto

x1 = "#2e2d2b"
x2 = "#feffff"
x3 = "#4fa882"
x4 = "#38576b"
x5 = "#403d3d"
x6 = "#e06636"
x7 = "#038cfc"
x8 = "#3fbfb9"
x9 = "#263238"
x10 = "#e9edf5"

# Criando janela

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=x1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Primeiro frame

frameSuperior = Frame(janela, width=1043, height=50, bg=x2, relief=FLAT)
frameSuperior.grid(row=0, column=0)

# Segundo frame 

frameMeio = Frame(janela, width=1043, height=303, bg=x2, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Terceiro frame

frameInferior = Frame(janela, width=1043, height=303, bg=x2, pady=20, relief=FLAT)
frameInferior.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Criação de funções

global tree

# Função adicionar

def adicionar():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    categoria = e_categoria.get()
    descricao = e_descricao.get()
    duracao = e_dur.get()
    data = e_cal.get()
    imagem = imagem_string

    lista_adicionar = [nome, categoria, descricao, duracao, data, imagem]

    for i in lista_adicionar:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    criar_form(lista_adicionar)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    nome.delete(0, 'end')
    categoria.delete(0, 'end')
    descricao.delete(0, 'end')
    duracao.delete(0, 'end')
    data.delete(0, 'end')
    imagem.delete(0, 'end')

    for widget in frameMeio.winfo_children():
        widget.destroy()
    
    mostrar()

# Função escolher imagem

global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameSuperior, image=imagem, bg=x2, fg=x5)
    l_imagem.place(x=700, y=10) 

# --------------- Frame Superior ---------------

## Definir imagem logo

app_img = Image.open('logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameSuperior, image=app_img, text=' Cadastro Filmes', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=x2, fg=x5)
app_logo.place(x=0, y=0) 

# --------------- Frame do Meio ---------------

## Entradas

l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x2, fg=x5)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_categoria = Label(frameMeio, text='Categoria', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x2, fg=x5)
l_categoria.place(x=10, y=40)
e_categoria = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_categoria.place(x=130, y=41)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x2, fg=x5)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_dur = Label(frameMeio, text='Duração', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x2, fg=x5)
l_dur.place(x=10, y=100)
e_dur = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_dur.place(x=130, y=101)

l_cal = Label(frameMeio, text='Lançamento', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x2, fg=x5)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, Background='darkblue', bordewidth=2)
e_cal.place(x=130, y=131)

## Criação de botões

### Botão carregar

l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x2, fg=x5)
l_carregar.place(x=10, y=160)
b_carregar = Button(frameMeio, width=30, text='carregar'.upper(),compound=CENTER, anchor=CENTER,overrelief=RIDGE, font=('Ivy 8'), bg=x2, fg=x1)
b_carregar.place(x=130, y=161)

### Botão adicionar

img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_adicionar = Button(frameMeio, command=adicionar, image=img_add, width=95, text='   Adicionar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=x2, fg=x1)
b_adicionar.place(x=330, y=10)

### Botão atualizar

img_att = Image.open('att.png')
img_att = img_att.resize((20,20))
img_att = ImageTk.PhotoImage(img_att)

b_atualizar = Button(frameMeio, image=img_att, width=95, text='   Atualizar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=x2, fg=x1)
b_atualizar.place(x=330, y=50)

### Botão deletar

img_del = Image.open('del.png')
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)

b_deletar = Button(frameMeio, image=img_del, width=95, text='   Deletar'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=x2, fg=x1)
b_deletar.place(x=330, y=90)

### Botão item

img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_deletar = Button(frameMeio, image=img_item, width=95, text='   Ver item'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=x2, fg=x1)
b_deletar.place(x=330, y=160)

## Labels Quantidade total 

l_qtd = Label(frameMeio, text='', width=15, height=2, pady=20, anchor=CENTER, font=('Ivy 17 bold'), bg=x8, fg=x2)
l_qtd.place(x=450, y=10)
b_qtd = Label(frameMeio, text='  Quantidade de Filmes  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=x8, fg=x2)
b_qtd.place(x=450, y=10)

# --------------- Frame Inferior ---------------

# Tabela

def mostrar():

    ## Treeview 

    tabela_head = ['Id','Nome', 'Categoria', 'Descrição', 'Duração', 'Lançamento']

    lista_itens = []

    tree = ttk.Treeview(frameInferior, selectmode="extended",columns=tabela_head, show="headings")

    # Scrollbar vertical
    vsb = ttk.Scrollbar(frameInferior, orient="vertical", command=tree.yview)

    # Scrollbar horizontal 
    hsb = ttk.Scrollbar(frameInferior, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameInferior.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[60,150,150,240,130,150,150, 150]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for items in lista_itens:
        quantidade.append(items[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()
