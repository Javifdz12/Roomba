
from tkinter import Frame, Tk, Scale,Entry
from tkinter import LEFT, HORIZONTAL 
"""
mi_ventana=Tk()
mi_ventana.geometry('600x500')
mi_ventana.title('HAB')

class MiVentana(Frame): 
    # Cada widget tiene un primer parámetro de constructor 
    # que es su widget 'maestro', es decir, el que lo 
    # contiene. Si no se especifica este parámetro, y si el 
    # widget en cuestión es un frame, entonces este estará 
    # contenido automáticamente en la ventana de la aplicación. 
    def __init__ (self,master,x,y,width,height,bg): 
        # Llamamos al constructor de la clase madre 
        # de MiVentana, es decir, Frame. Además del widget maestro, 
        # especificamos las dimensiones de la ventana, es decir, un 
        # ancho de 320 píxeles y un alto de 240. 
        self.master=master
        self.width=width
        self.height=height
        self.bg=bg
        self.x=x
        self.y=y
    
        # pack() permite consolidar la geometría del frame 
        # en la ventana. Sin esta llamada, el dimensionamiento 
        # dado en el constructor de Frame no tendría lugar.
    def colocar(self):
        self.place(x=self.x,y=self.y,width=self.width,height=self.height)
    
frame1=MiVentana(mi_ventana,100,50,400,220,'blue')
frame1.colocar()
mi_ventana.mainloop()

class MiVentana(Frame): 
    def __init__(self, master=None): 
        super(MiVentana, self).__init__(master) 
        self.master.title("Conversor C <-> F") 
        self.pack()
 
    def initWidgets(self): 
        # Declaración de una etiqueta que muestra el texto 'F'. 
        # El primer argumento es el widget 'padre' 
        # que contendrá esta etiqueta, es decir, self, 
        # el frame principal. 
        self.FTexto = Label(self, text = 'F') 
 
        # Declaración de un cursor que mostrará los grados 
        # Fahrenheit. Los parámetros llamados del constructor 
        # permiten personalizar el widget: su orientación 
        # es horizontal y los valores que recorre van 
        # de -148 a 212. 
        self.FCursor = Scale(self, orient=HORIZONTAL, from_=-148, 
                             to=212) 
 
        # Idem aquí para los grados Celsius. 
        self.CTexto = Label(self, text='C') 
        self.CCursor = Scale(self, orient=HORIZONTAL, from_=-100, 
                             to=100) 
 
        # Creamos una lista de widgets sobre la que hacemos un bucle ... 
        for widget in [self.CTexto, self.CCursor, self.FTexto, 
                       self.FCursor]: 
            # El widget actual está "pegado" a la izquierda 
            # en la ventana de la aplicación. 
            widget.pack(side=LEFT)

# Instanciación de la ventana. 
mi_ventana = MiVentana() 
# Inicialización de los widgets. 
mi_ventana.initWidgets() 
# Lanzamiento del bucle principal. 
mi_ventana.mainloop()


class MiVentana(Frame): 
    def __init__(self, master=None): 
        super(MiVentana, self).__init__(master) 
        self.master.title("Conversor C <-> F") 
        self.pack()
 
    def initWidgets(self): 
        self.FTexto = Label(self, text='F') 
        # En el constructor del cursor, asignamos 
        # al evento command el método convertirFEnC(). 
        self.FCursor = Scale(self, orient=HORIZONTAL, from_=-148, 
                             to=212, command=self.convertirFEnC) 
 
        # Idem aquí para los grados Celsius.
        self.CTexto = Label(self, text='C')
        self.CCursor = Scale(self, orient=HORIZONTAL, from_=-100, 
                             to=100, command=self.convertirCEnF) 
 
        for widget in [self.CTexto, self.CCursor, self.FTexto, 
                       self.FCursor]: 
            # El widget actual está "pegado" a la izquierda 
            # en la ventana de la aplicación. 
            widget.pack(side=LEFT) 
 
    # Método llamado cuando el cursor de grados Celsius 
    # se ha movido. Calcula la equivalencia en grados Fahrenheit 
    # y modifica el valor del cursor de esta escala de 
    # grados en consecuencia. 
    def convertirCEnF(self, valor): 
        C = float(valor) 
        F = C * 9/5 + 32 
        self.FCursor.set(F) 
 
    # Como convertirCEnF(), pero en el sentido opuesto 
    # de conversión de escalas de grados. 
    def convertirFEnC(self, valor): 
        F = float(valor) 
        C = (F - 32) * 5/9 
        self.CCursor.set(C)

mi_ventana = MiVentana() 
# Inicialización de los widgets. 
mi_ventana.initWidgets() 
# Lanzamiento del bucle principal. 
mi_ventana.mainloop()

mi_ventana = Tk()
mi_ventana.geometry('3000x3000')
mi_ventana.title('Salon')
mi_ventana3=Frame(mi_ventana,bg='yellow')
mi_ventana3.place(x=500,y=150,width=480,height=101)


class Obstaculo:
    def __init__(self,x,y,largo,ancho,ventana,bg):
        self.x=x
        self.y=y
        self.largo=largo
        self.ancho=ancho
        self.ventana=ventana
        self.bg=bg
    def colocar_ob(self):
        self.frame=Frame(self.ventana,bg=self.bg)
        self.frame.place(x=self.x,y=self.y,width=self.ancho,height=self.largo)
obs1=Obstaculo(10,20,10,20,mi_ventana,'brown')
obs1.colocar_ob()
obs2=Obstaculo(100,200,150,2000,mi_ventana,'green')
obs3=Obstaculo(1000,2000,100,20,mi_ventana,'black')
mi_ventana.mainloop()
obs=[obs1,obs2,obs3]

class Habitacion:
    def __init__(self,nombre,largo,ancho,obs):
        self.nombre = nombre
        self.largo = largo
        self.ancho=ancho
        self.obs=obs
    def crear(self):
        self.ventana=Tk()
        self.ventana.geometry(f'{self.largo}x{self.ancho}')
        self.ventana.title(self.nombre)
    def añadir_obs(self):
        for i in self.obs:
            i.colocar_ob()
hab=Habitacion('salon',630,500,obs)
hab.crear()"""

class Texto:
    def __init__(self,vent,text):
        self.text = text
        self.vent = vent
    def crear_y_añadir(self):
        self.texto=Frame(self.vent,text=self.text)
        self.texto.pack()



