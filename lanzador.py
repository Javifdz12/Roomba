from tkinter import Tk,LabelFrame,Text,Label
from obstaculo import Obstaculo
from prueba import Texto

"""
def lanzar():
    print('#####-ROOMBA-#####')
    z=float(input('¿Cuál es la velocidad de tu rumba(m2/h o cm/s)? '))
    a=int(input('¿Cuál es el largo de la habitacion(cm)? '))
    s=int(input('¿Cuál es el ancho de la habitacion(cm)? '))
    a1=a*s
    mi_ventana = Tk()
    mi_ventana.geometry(f'{a}x{s}')
    mi_ventana.title('Habitación')
    b=int(input('¿Cuántos obstáculos tiene la habitacion? '))
    print('Si la habitación es la siguiente:')
    print(f'{a}')
    print('  ^')
    print('y |\n')
    print('  |\n')
    print('  |\n')
    print('  |\n')
    print('  |')
    print(f'   -- -- -- -- -- -- --  > {s}\n                      x')
    colores=['blue','yellow','red']
    a2=0
    i=0
    while i<b:
        c=float(input(f'¿Cuál es la posicion x de la esquina superior derecha obstaculo {i+1}? '))
        d=float(input(f'¿Cuál es la posicion y de la esquina superior derecha obstaculo {i+1}? '))
        e=float(input(f'¿Cuál es el largo del obstaculo {i+1}?(cm) '))
        f=float(input(f'¿Cuál es el ancho del obstaculo {i+1}?(cm) '))
        obs=Obstaculo(c,d,e,f,mi_ventana,bg='black')
        obs.colocar_ob()
        a2+=(e*f)
        i+=1
    mi_ventana.mainloop()
    af=a1-a2
    print(f'El area a limpiar es {af/10000} m2')
    print(f'Como la velocidad de la roomba es de {z} m2/h...')
    print(f'El tiempo de limpieza será de {tiempo_limp((af/10000),z)} minutos')
"""

#Funcion para calcular tiempo de limpieza.
def tiempo_limp(area_hab,vel_rob):
    #Conociendo el area de la habitacion en donde la roomba va a poder limpìar(m2) y la velocidad de esta(m2/h o cm/s),
    #podemos calcular una estimacion del tiempo de limpieza(en este caso lo hago en min).
    t=area_hab/vel_rob
    return t*60

def lanzar():
    #Esta seria la ventana principal del ejercicio.
    ventana=Tk()
    ventana.title('Habitación')
    marco=LabelFrame(ventana,width=560,height=690)
    marco.pack(padx=30,pady=30)
    #Asi quedaria el obstaculo
    obs=Obstaculo(101,150,260,90,marco,'grey','sunken')
    #Colocamos el obstaculo
    obs.colocar_ob()
    #Visualizamos la habitacion
    ventana.mainloop()
    #Area de la habitacion
    a1=31
    a2=(obs.largo*obs.ancho)/10000
    a=a1-a2
    v=30
    print(f'El tiempo de limpieza será de {tiempo_limp((a),v)} minutos')
