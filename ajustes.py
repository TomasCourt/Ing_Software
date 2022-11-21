import pandas as pd

ipath = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/listaProductos.xlsx'

df = pd.read_excel(ipath)
print(df.size)

df = df.dropna(subset=['codigo'])


print(df.size)

df.to_excel('listaProductos.xlsx', sheet_name='Productos')