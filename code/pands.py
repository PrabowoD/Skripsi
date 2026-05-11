
from importlib.metadata import files

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

    Fls = folder
    imps = [os.path.join(Fls, f) for f in os.listdir(Fls)
            if f.lower().endswith((".jpg", ".png", ".jpeg"))
            ]
    files = []
    for idx, img in enumerate(imps):
            img = os.path.basename(img)
            img = os.path.splitext(img)[0]
            img = img.lower()
            img = img.strip()
            

            file = df[df["nama_file"] == img]
            panjang_Gt = file.iloc[0]["panjang"]

        #     print(panjang_Gt)
                
            panjang_transformed = panjang_deteksi * (panjang_Gt / panjang_deteksi)
            lebar_transformed = lebar_deteksi * (panjang_Gt / panjang_deteksi)
            transformed_values = [img, int(panjang_transformed), int(lebar_transformed)]
            files.append(transformed_values)
    return files
    






# check = df.loc[df['nama_file'] == filename]
# if not check.empty:
#     panjang = check.iloc[0]['panjang']
#     lebar = check.iloc[0]['lebar']
#     print(panjang, lebar)

