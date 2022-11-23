import pandas as pd
import numpy as np


ipath = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/Ventas.xlsx'

df = pd.read_excel(ipath)
#print(df["codigo"].size)

ipath2= 'C:/Users/ASUS/Desktop/Informática/Ing_Software/listaProductos.xlsx'

df2 = pd.read_excel(ipath2)
#print(df2.size)


Productos=pd.DataFrame()
Productos["cantidad"]=None
Productos["codigo"]=None

#print(df["codigo"].unique())

for a in df["codigo"].unique():
    df3=df[df["codigo"]==a]
    #print("Hay ",df3["codigo"].size," productos del codigo: ",a)
    Productos=pd.concat([Productos,(pd.DataFrame({"cantidad":df3["codigo"].size,"codigo":a}, index=[0]))])

#ordenamos la el dataframe segun la cantidad de veces comprado, y nos enfocamos en esos productos para mejorar el funcionamiento del stock
#De esta forma lograr un impacto mayor

by_cantidadVentas = Productos.sort_values('cantidad',ascending=False).reset_index()

#print(by_cantidadVentas.head(5))

for f in range(0,6):
    cont=0
    for a in df2["codigo"]:
        if (a == str(by_cantidadVentas["codigo"][f])):
            print("Aquel producto vendido ",by_cantidadVentas["cantidad"][f]," veces, es: ",df2["producto"][cont]," y vence en: ",df2["duracion"][cont])
        cont+=1

#Con lo anterior pudimos notar que hay productos que se venden en gran cantidad y que ademas, vencen muy rapido

# ACOTAREMOS EL PROBLEMA A PRODUCTOS QUE VENCEN RAPIDO

dfEmpanaPino=df[df["codigo"]==(by_cantidadVentas["codigo"][0])].reset_index()
#print(dfEmpanaPino)

for dia in range(0,7):
    df5=dfEmpanaPino[dfEmpanaPino["dia"]==dia]
    df6=dfEmpanaPino[dfEmpanaPino["dia"]==dia+7]
    promedioVentas=df5["dia"].size+df6["dia"].size
    print(promedioVentas, " Empanadas de pino son vendidas el dia ",dia+1," de la semana")


dfEmpanaQueso=df[df["codigo"]==(by_cantidadVentas["codigo"][3])].reset_index()
#print(dfEmpanaQueso)

for dia in range(0,7):
    df5=dfEmpanaQueso[dfEmpanaQueso["dia"]==dia]
    df6=dfEmpanaQueso[dfEmpanaQueso["dia"]==dia+7]
    promedioVentas=df5["dia"].size+df6["dia"].size
    print(promedioVentas, " Empanadas de queso son vendidas el dia ",dia+1," de la semana")


dfhayulla=df[df["codigo"]==(by_cantidadVentas["codigo"][4])].reset_index()
#print(dfhayulla)

for dia in range(0,7):
    df5=dfhayulla[dfhayulla["dia"]==dia]
    df6=dfhayulla[dfhayulla["dia"]==dia+7]
    promedioVentas=df5["dia"].size+df6["dia"].size
    print(promedioVentas, " Pan hayulla 480 grs son vendidos el dia ",dia+1," de la semana")


