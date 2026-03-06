"""
# soal dicoding perulangan
evenNumber = [i for i in range(0,501,2)]

print(evenNumber)

# soal dicoding array

var_arr = [i for i in range(101)]

result = sum(var_arr) / len(var_arr)
print(result)

# soal dicoding fungsi

TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
def minimal(a, b):
    return a if a <= b else b

# Contoh penggunaan
print(minimal(5, 10))  # Output: 5
print(minimal(10, 10)) # Output: 10
print(minimal(20, 15)) # Output: 15


# Kuis Coding: Object-oriented Programming

TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.
# Mendefinisikan kelas Animal
class Animal:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species

# Mendefinisikan kelas Cat yang merupakan turunan dari kelas Animal
class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self):
        return "meow!"

# Membuat instance dari kelas Cat
myCat = Cat(name="Neko", age=3, species="Persian")

# Contoh penggunaan
print(myCat.deskripsi())  # Output: Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun
print(myCat.suara())      # Output: meow!