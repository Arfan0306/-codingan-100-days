class mahasiswa():

    jurusan ="teknik informatika"
    __nilai = 0 #private
    def __init__(self, nama,nim):
        self.nama = nama
        self.nim = nim

    def ujian(self,nilai1):
        self.__nilai += nilai1

    def uts(self,nilai1):
        self.__nilai += nilai1

    def cek_status(self):
        if self.__nilai <50:
            print(self.nama,"tdk lulus")
        else:
            print(self.nama,"lulus")
    
kaco = mahasiswa("arfan muhadir","D0221530")
cicci = mahasiswa("resky","D0221030")

kaco.ujian(10)
kaco.uts(50)
kaco.cek_status()

cicci.ujian(5)
cicci.uts(25)
cicci.cek_status()




