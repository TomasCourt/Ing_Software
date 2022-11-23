
import pandas as pd
import random as rd
import numpy as np


ipath2 = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/BBDDagro.xlsx'

df2 = pd.read_excel(ipath2)
print(df2["codigo_producto"].size)

ipath3= 'C:/Users/ASUS/Desktop/Informática/Ing_Software/Ventas.xlsx'

df3 = pd.read_excel(ipath3)
print(df3["codigo"].size)

#codigo,numero_cliente,dia,mes,anio
#5772 filas

for a in range(0,6850,24):
    df3["codigo"][a]=18016004
    df3["codigo"][a+1]=18016005
    df3["codigo"][a+8]=18016008
    df3["codigo"][a+12]=7803403002229
    df3["codigo"][a+16]=78926974


df3.to_excel('Ventas.xlsx', sheet_name='Ventas')



