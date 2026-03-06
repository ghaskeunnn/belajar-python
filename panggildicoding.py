import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal lahir Anda (DD-MM-YY)")
args = parser.parse_args()
 
print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2025, Kakak "+args.nama)