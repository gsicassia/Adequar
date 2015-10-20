from tkinter import *

app = Tk()
app.title("teste de janela")
app.geometry('300x100+100+200')

quant_botao01 = IntVar()
quant_botao01.set(0)
quant_botao02 = IntVar()
quant_botao02.set (0)

def apertou01():
    quant_botao01.set(quant_botao01.get() + 1)

def apertou02():
    quant_botao02.set(quant_botao02.get() + 1)

lab1 = Label(app, text='Aperte os botoes')
lab1.pack()

lab1 = Label(app, textvariable = quant_botao01)
lab1.pack(side = "left")

lab2 = Label(app, textvariable = quant_botao02)
lab2.pack(side = "right")

b1 = Button(app, text = "Botao 01", width = 10, command = apertou01)
b1.pack(side = "left", padx = 10, pady = 10)

b2 = Button(app, text = "Botao 02", width = 10, command = apertou02)
b2.pack(side = "right", padx = 10, pady = 10)


app.mainloop()
