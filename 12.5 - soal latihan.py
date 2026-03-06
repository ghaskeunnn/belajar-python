# soal 1
# ----0++++5-----8++++++11------
inputUser = float(input("Masukkan angka :"))
KD1 = inputUser < 5
KD2 = inputUser < 11
LD1 = inputUser > 0
LD2 = inputUser > 8
hasil = (KD1 and LD1) or (KD2 and LD2)
print(hasil)

# soal 1
# ++++0----5++++8----11++++
inputUser = float(input("Masukkan angka :"))
KD1 = inputUser < 0
KD2 = inputUser < 8
LD1 = inputUser > 5
LD2 = inputUser > 11
hasil = KD1 or (KD2 and LD1) or LD2
print(hasil)