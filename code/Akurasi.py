import numpy as np



def hitung_akurasi(prediksi, referensi):
    prediksi = np.array(prediksi)
    referensi = np.array(referensi)
    
    Ei = prediksi - referensi
    akurasi = np.mean(1 / (1 + np.abs(Ei))) * 100
    
    return akurasi