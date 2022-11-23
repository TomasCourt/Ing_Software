import pandas as pd
import numpy as np


ipath = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/Ventas.xlsx'

df = pd.read_excel(ipath)
print(df["codigo"].size)

ipath2= 'C:/Users/ASUS/Desktop/Informática/Ing_Software/listaProductos.xlsx'

df2 = pd.read_excel(ipath2)
print(df2.size)


Productos=pd.DataFrame()
Productos["cantidad"]=None
Productos["codigo"]=None


for a in df["codigo"].unique():
    #print("Hay ",df[df["codigo"]==a].size," productos del codigo: ",a)
    Productos=pd.concat([Productos,(pd.DataFrame({"cantidad":df[df["codigo"]==a].size,"codigo":a}, index=[0]))])

#ordenamos la el dataframe segun la cantidad de veces comprado, y nos enfocamos en esos productos para mejorar el funcionamiento del stock
#De esta forma lograr un impacto mayor

by_cantidadVentas = Productos.sort_values('cantidad',ascending=False)

print(by_cantidadVentas.head(5))

for a in range(0,6):    
    df3=df2[df2["codigo"]==by_cantidadVentas["codigo"][a]] 
    print("Aquel producto vendido ",by_cantidadVentas["cantidad"][a]," veces, es: ",df3["producto"]," y vence en: ",df3["duracion"])

