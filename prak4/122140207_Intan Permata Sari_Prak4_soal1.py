class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        return f"{self.__class__.__name__} {self.nama} sedang makan: tulang"

    def minum(self):
        pass

    def __str__(self):
        self.bersuara()
        return self.makan()

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Guk Guk!")

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")
hewan3 = Anjing("Cimua", "Jantan")

print(hewan1.nama)
print(hewan2.nama)  

print("\n==============\n")
print(hewan1)       
print(hewan2)       
print(hewan3)      
