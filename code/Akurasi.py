import numpy as np



def hitung_akurasi(prediksi_panjang, prediksi_lebar, prediksi_berat, referensi_panjang, referensi_lebar, referensi_berat):
    p_l = np.array(prediksi_lebar)
    r_l = np.array(referensi_lebar)
    p_p = np.array(prediksi_panjang)
    r_p = np.array(referensi_panjang)
    p_b = np.array(prediksi_berat)
    r_b = np.array(referensi_berat)
    
    Ei_l = p_l - r_l
    Ei_p = p_p - r_p
    Ei_b = p_b - r_b
    
    akurasi_l = np.mean(1 / (1 + np.abs(Ei_l))) * 100
    akurasi_p = np.mean(1 / (1 + np.abs(Ei_p))) * 100
    akurasi_b = np.mean(1 / (1 + np.abs(Ei_b))) * 100
    
    return akurasi_l, akurasi_p, akurasi_b