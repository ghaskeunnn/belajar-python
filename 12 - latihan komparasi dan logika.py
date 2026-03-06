# mmebuat gabungan area rentang dari angka

# +++++3------10+++++++
inputUser = float(input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 \n:"))

# +++++3----------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# -----10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++3--------10++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ",isCorrect)

# -----3++++++10-----
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukkan angka yang bernilai \nlebih dari 3 \natau \nkurang dari 10 \n:"))

# +++++3----------
# memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print("lebih dari 3 =", isLebihDari)

# -----10+++++++
# memeriksa angka lebih dari 10
isKurangDari = (inputUser < 10)
print("Lebih dari 10 =", isKurangDari)

# +++++3--------10++++++
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ",isCorrect)