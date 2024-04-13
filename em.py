# relogio
Relógio em python
from tkinter
from tkinter.ttk import Label importLabel, 
import tkinter
from datatime import datatime 

###### cores #####
cor1 = '#3d3d3d' #preta
cor2 = '#fafvff'  #branca
cor3 = '#21c25c'  #verde
cor4 = '#ed463d'  #vermelho
cor5 = '#dedcdc'  #cinza
cor6 = '#3080f0'  #azul

fundo = cor1
cor = cor3
janela = Tk()
janela.title('')
janela.geometry('440x180')
janela.resizable(width = False, height=False)
janela.configure(bg=cor1)


def relogio():
    tempo = datatime.now() 

    hora = tempo.strtfime('%H:%M:%S')
    dia_semana = tempo.strtfime('%A')
    dia = tempo.day
    mes = tempo.strftime('%b')
    ano = tempo.strftime("%Y")
    
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + str(dia) + '/' + str(mes) + '/' +  str(ano))

l1 = Label(janela, text='', font=('Arial 80'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l1 = Label(janela, text='', font=('Arial 20'), bg=fundo, fg=cor)
l1.grid(row=1, column=0, sticky=NW, padx=5)

relogio()

janela.mainloop()
