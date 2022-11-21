class mahasiswa():
    nama="nama"

    def belajar(self, kondisi):
        print(self.nama,"sedang belajar",kondisi)
    def bermain(self):
        print(self.nama,"sedang bermain")
    
kaco = mahasiswa()
cicci = mahasiswa()

kaco.nama ="arfan"
cicci.nama ="resky"

kaco.belajar("sangat rajin")
cicci.bermain()
