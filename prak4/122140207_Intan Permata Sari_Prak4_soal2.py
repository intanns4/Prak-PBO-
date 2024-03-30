import math  # Memanggil math bawaan python

class BangunDatar:  # Class abstrak
    def __init__(self, sisi, jari):
        self.sisi = sisi
        self.jari = jari

    def hitungLuas(self):
        pass

class Persegi(BangunDatar):
    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def hitungLuas(self):
        return math.pi * self.jari ** 2

persegi = Persegi(5, None)
lingkaran = Lingkaran(None, 3)

for bangundatar in (persegi,):  # Menggunakan objek yang sudah dibuat
    print(f"Luas Persegi : {bangundatar.hitungLuas()}")  # Memanggil metode hitungLuas()

for bangundatar in (lingkaran,):  # Menggunakan objek yang sudah dibuat
    print(f"Luas Lingkaran : {bangundatar.hitungLuas()}")
