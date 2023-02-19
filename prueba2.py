zona1={'Largo':500,'Ancho':150}
zona2={'Largo':480,'Ancho':101}
zona3={'Largo':309,'Ancho':480}
zona4={'Largo':90,'Ancho':220}
hab1=[zona1,zona2,zona3,zona4]
velocidad=32 #metros_cuadrados/hora o cm/segundo

def area_hab(lista_zonas):
    a=0
    for i in lista_zonas:
        a+=(i['Largo']*i['Ancho'])
    return a/10000

def tiempo_limp(area_hab,vel_rob):
    t=area_hab/vel_rob
    return t*60

print(f'{area_hab(hab1)} m2')
print(f'{tiempo_limp(area_hab(hab1),velocidad)} min')

