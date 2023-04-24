# Importando modulo ttinker.
from tkinter import *
from tkinter import ttk

# Cores
cor1 = '#1e1f1e' # Preto
cor2 = '#ffffff' # Branco
cor3 = '#120a8f' # Azul Marinho
cor4 = '#0000ff' # Azul Claro

# Nome e tamanho do aplicativo.
janela = Tk()
janela.title("Calculadora")
janela.geometry('318x360')
janela.config(bg=cor1)


# Visor (visor de resultado e números clicados).
frame_tela = Frame(janela, width=318, height=60, bg=cor4)
frame_tela.grid(row=0, column=0)
app_label = Label(frame_tela, text= '123456789', width=18, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 20 bold'))
app_label.place(x=0,y=0)

# Criando funções
def calcular():
    resultado = eval('9/9')
    print(resultado)
    # passando o valor para tela
    app_label.set(resultado)

# Parte dos botões (sem os botões).
frame_corpo = Frame(janela, width=318, height=230, bg=cor2)
frame_corpo.grid(row=1, column=0)

# Botões da calculadora.
b_1 = Button(frame_corpo, text='C', width=11, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)

b_2 = Button(frame_corpo, text='%', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=84,y=0)

b_3 = Button(frame_corpo, text='/', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=162,y=0)

b_4 = Button(frame_corpo, text='*', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=240,y=0)

b_18 = Button(frame_corpo, text='+', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=240,y=114)

# Botões de memoria.
b_5 = Button(frame_corpo, text='M*', width=11, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0,y=38)

b_6 = Button(frame_corpo, text='MR', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=84,y=38)

b_7 = Button(frame_corpo, text='M+', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=162,y=38)

b_8 = Button(frame_corpo, text='M-', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=240,y=38)

b_17 = Button(frame_corpo, text='MC', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=240,y=76)

b_16 = Button(frame_corpo, text='=', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=162,y=191)

b_19 = Button(frame_corpo, text='-', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=240,y=152)

b_20 = Button(frame_corpo, text=',', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_20.place(x=240,y=191)

# Números
b_9 = Button(frame_corpo, text='7', width=11, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0,y=76)

b_10 = Button(frame_corpo, text='8', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=84,y=76)

b_11 = Button(frame_corpo, text='9', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=162,y=76)

b_12 = Button(frame_corpo, text='4', width=11, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0,y=114)

b_13 = Button(frame_corpo, text='5', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=84,y=114)

b_13 = Button(frame_corpo, text='6', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=162,y=114)

b_13 = Button(frame_corpo, text='1', width=11, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0,y=152)

b_14 = Button(frame_corpo, text='2', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=84,y=152)

b_15 = Button(frame_corpo, text='3', width=10, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=162,y=152)

b_16 = Button(frame_corpo, text='0', width=22, height=2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0,y=191)

# Sei lá.
janela.mainloop()

calcular ()
