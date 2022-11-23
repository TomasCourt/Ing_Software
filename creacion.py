
import pandas as pd
import random as rd
import numpy as np

ipath = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/listaProductos.xlsx'
ipath2 = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/BBDDagro.xlsx'

df = pd.read_excel(ipath)
print(df["codigo"].size)

df2 = pd.read_excel(ipath2)
print(df2["codigo_producto"].size)

"""
11 am a 9 pm

de 70 a 140 clientes al dia

maximo 50 lucas de compra
"""

dias=14

cliente=pd.DataFrame()
cliente["codigo"]=None
cliente["numero_cliente"]=None
cliente["dia"]=None
cliente["mes"]=None
cliente["anio"]=None
print(cliente)


numerocliente=0
fila=0
for a in range(0,dias):
    clientediario=rd.randint(70,130)
    #print("el dia ",a," hay ",clientediario," clientes")
    for b in range(0,clientediario+1):
        for d in range(0, rd.randint(2,7)):
            e=rd.randint(0,90)
            cliente=pd.concat([cliente,(pd.DataFrame({"codigo":df2["codigo_producto"][e],"numero_cliente":numerocliente,"dia":a+7,"mes":"nov","anio":"2022"}, index=[0]))])
        numerocliente+=1
print(cliente)
print(cliente.size)


cliente.to_excel('Ventas.xlsx', sheet_name='Ventas')




#Agregar los 20 clientes de Pan y Empanada
#Agregar los 20 clientes por día de lunes a viernes de papas, bebidas, chicles y dulces.

