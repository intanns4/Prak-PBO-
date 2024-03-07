class Mahasiswa:

    def __init__(self, nim, nama, angkatan, isMahasiswa=None):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        if isMahasiswa == None:
            self.isMahasiswa = True
        else:
            self.isMahasiswa = isMahasiswa

    def set_nama(self, __nama):
        self.nama = nama

    def set_nim(self, __nim):
        self.nim = nim

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def __str__(self):
        return f'nama : {self.__nama}\nnim : {self.__nim}\nangkatan : {self.angkatan}\nmahasiswa : {self.is_mahasiswa_aktif()}'

    def is_mahasiswa_aktif(self):
        if self.isMahasiswa == True:
            return "Mahasiswa aktif"
        else:
            return "Mahasiswa tidak aktif"

    def bandingkan(self, other):
        if self.angkatan > other.angkatan:
            return f'{self.__nama} senior dari {other.__nama}'
        elif self.angkatan < other.angkatan:
            return f'{self.__nama} junior dari {other.__nama}'
        else:
            return f'{self.__nama} dan {other.__nama} di angkatan yang sama'
        
    def kapan_sempro(self):
        return f'{self.get_nama()} harus Sempro di tahun {self.angkatan + 3}'
      


mhs1 = Mahasiswa(122140204, "Amri", 2025, True)
mhs2 = Mahasiswa(122140207, "Aril", 2025)

print(mhs1)
print(mhs2)

print(mhs1.bandingkan(mhs2))
print(mhs1.kapan_sempro())
