from tkinter import Frame

class Obstaculo:
    def __init__(self,x,y,largo,ancho,ventana,bg,relief):
        #NOTA:debemos saber que la coordenada (0,0) de la ventana principal correspode a su esquina superior izquierda (no la inferior) para colocar
        #bien los valores de x e y.
        #Coordenada x del obstaculo.
        self.x=x
        #Coordenada y del obstaculo.
        self.y=y
        #Largo del obstaculo.
        self.largo=largo
        #Ancho del obstaculo.
        self.ancho=ancho
        #Ventana en la que se encuentra(o queremos que se encuentre) el obstaculo.
        self.ventana=ventana
        #Color del obstaculo.
        self.bg=bg
        self.relief=relief
    #Funcion para colocar el objeto.
    def colocar_ob(self):
        #Creamos frame el cual estamos haciendo pasar por un obstaculo para poder visualizar el problema.
        #Le pasamos la ventana en la que queremos meterlo y el color que queremos que tenga.
        self.frame=Frame(self.ventana,bg=self.bg,relief=self.relief)
        #En este caso utilizo .place(x,y,width,height) para posicionarlo en la ventana.
        self.frame.place(x=self.x,y=self.y,width=self.ancho,height=self.largo)