import pandas as pd

df = pd.read_excel('Size_ikan.xlsx', sheet_name='Lele')
pjg = df['panjang']
print(pjg)