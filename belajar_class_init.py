class mahasiswa():
    nama="nama"

    def __init__(self, nama,nim):
        self.nama = nama
        self.nim = nim

    def belajar(self, kondisi):
        print(self.nama,"sedang belajar",kondisi)
    def bermain(self):
        print(self.nama,"sedang bermain")
    
kaco = mahasiswa("arfan muhadir","D0221530")
print(kaco.nama)
print(kaco.nim)

kaco.belajar("dengan rajin")
