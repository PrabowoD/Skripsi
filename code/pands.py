import pandas as pd
import os 
import numpy as np

# folder = "Output/Rotated/UjiCoba"
# excel_file = "Size_ikan.xlsx"
# df = pd.read_excel(excel_file, sheet_name='Nila')
# df["nama_file"] = df["nama_file"].astype(str).str.strip().str.lower()
# df = df.set_index('nama_file')

def transform_size(excel_file, panjang_deteksi, lebar_deteksi, folder):
    df = pd.read_excel(excel_file, sheet_name='Nila')
    df["nama_file"] = df["nama_file"].astype(str).str.strip().str.lower()
    # df = df.set_index('nama_file')
    
    panjang_transformed = 0
    lebar_transformed = 0

    for files in os.listdir(folder):
        if files.lower().endswith((".jpg", ".png", ".jpeg")):
            filename = os.path.basename(files)
            filename = os.path.splitext(filename)[0]
            filename = filename.lower()
            # print(filename)
    
    if filename in df['nama_file'].values:
        panjang_Gt = df.loc[df['nama_file'] == filename, "panjang"].iloc[0]
        print(panjang_Gt)
        
        panjang_transformed = panjang_deteksi * (panjang_Gt / panjang_deteksi)
        lebar_transformed = lebar_deteksi * (panjang_Gt / panjang_deteksi)
        
    return panjang_transformed, lebar_transformed
    
    




# check = df.loc[df['nama_file'] == filename]
# if not check.empty:
#     panjang = check.iloc[0]['panjang']
#     lebar = check.iloc[0]['lebar']
#     print(panjang, lebar)

