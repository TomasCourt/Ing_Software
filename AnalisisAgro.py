import pandas as pd

ipath = 'C:/Users/ASUS/Desktop/Informática/Ing_Software/BBDDagro.xlsx'

df = pd.read_excel(ipath)
print(df.head())

