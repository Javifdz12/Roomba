from tkinter import Tk
from obstaculo import Obstaculo
def sumar(x,y):
    return x+y
ventana=Tk()
a=Obstaculo(100,200,70,100,ventana,'grey','sunken')
b=Obstaculo(100,200,70,100,ventana,'grey','sunken')
c=Obstaculo(100,200,70,100,ventana,'grey','sunken')
lista=[a,b,c]
lista[0].colocar_ob()
ventana.mainloop()