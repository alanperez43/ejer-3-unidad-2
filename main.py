from clase_camiones import camiones
from clase_cosecha import bi
from clase_menu import menu
import csv
import re
if __name__=="__main__":
    lista=[]
    camion=open("camiones.csv")
    reader=csv.reader(camion,delimiter=";")
    for fila in reader:
        
        lista.append(camiones(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4])))  
         
    camion.close()    
    cosecha=open("cosechas.csv")
    reader=csv.reader(cosecha,delimiter=";")
    a=bi()
    ban=0
    longi=len(lista)
    for fila in reader:
        if(ban==0):
            ban=1
        else:
            x=int(fila[0])
            
            i=0
            while((i < longi) and (lista[i].getid()!=x)):   
                i+=1
            if (i < longi):
                kg=float(fila[2])-lista[i].getpesovacio()
                print(kg)
                a.registrar(kg,int(fila[0]),int(fila[1]))
            else:
                print("no se encontro")
    print("MENU")
    MENU=menu()
    op=None
    while(op!=4):
        print("|-----------------------------------------------------|")
        print("| Ingresar 1 para mostrar cantidad de kg de un camion |")
        print("| Ingresar 2 para mostrar listado segun dia ingresado |")
        print("| Ingresar 3 para ejecutar test                       |")
        print("|-----------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        
        
        MENU.opcion(op,lista,a) 
    