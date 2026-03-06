import argparse
from datetime import datetime

def hitung_usia(tanggal_lahir):
    # Mengonversi string tanggal lahir ke objek datetime
    tgl_lahir = datetime.strptime(tanggal_lahir, "%d-%m-%Y")
    # Menghitung usia
    hari_ini = datetime.now()
    usia = hari_ini.year - tgl_lahir.year - ((hari_ini.month, hari_ini.day) < (tgl_lahir.month, tgl_lahir.day))
    return usia

def main(nama, tanggal_lahir):
    # Menghitung usia
    usia = hitung_usia(tanggal_lahir)
    
    # Menentukan panggilan berdasarkan usia
    if usia < 30:
        panggilan = "Kakak"
    else:
        panggilan = "Bapak"
    
    # Menampilkan hasil
    print(f"Selamat datang, {panggilan} {nama}!")

if __name__ == "__main__":
    # Membuat parser untuk argumen
    parser = argparse.ArgumentParser(description="Program untuk menyapa pengguna.")
    parser.add_argument('-n', '--nama', type=str, required=True, help='Nama pengguna')
    parser.add_argument('-t', '--tanggallahir', type=str, required=True, help='Tanggal lahir (dd-mm-yyyy)')

    # Mem-parsing argumen
    args = parser.parse_args()

    # Memanggil fungsi utama
    main(args.nama, args.tanggallahir)