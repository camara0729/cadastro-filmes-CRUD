# Importanto bibliotecas do tkinter

from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

# Cores do projeto

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

frameMeio = Frame(janela, width=1043, height=303, bg=x2, pady=20, relief=FLAT)
frameMeio.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Definir imagem logo

app_img = Image.open('logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameSuperior, image=app_img, text=' Cadastro Filmes', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=x2, fg=x5)
app_logo.place(x=0, y=0) 

janela.mainloop()
