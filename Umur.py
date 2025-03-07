# Mengimpor modul datetime untuk mendapatkan tahun saat ini
from datetime import datetime

# Fungsi untuk menghitung umur
def hitung_umur(tahun_lahir):
    # Mendapatkan tahun saat ini
    tahun_sekarang = datetime.now().year
    # Menghitung umur
    umur = tahun_sekarang - tahun_lahir
    return umur

# Meminta input dari pengguna
try:
    nama = input("Masukkan nama Anda: ")
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    
    # Memastikan tahun lahir tidak lebih dari tahun sekarang
    if tahun_lahir > datetime.now().year:
        print("Tahun lahir tidak valid. Silakan masukkan tahun yang benar.")
    else:
        umur = hitung_umur(tahun_lahir)
        print(f"Halo, {nama}! Umur Anda adalah {umur} tahun.")
except ValueError:
    print("Input tidak valid. Silakan masukkan angka yang benar.")
