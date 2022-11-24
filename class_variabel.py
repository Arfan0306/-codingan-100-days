class mahasiswa():

    jurusan = "teknik informatika"
    jumlah_mhs = 0
    
    def __init__(self, nama,nim):
        self.nama = nama
        self.nim = nim
    
        mahasiswa.jumlah_mhs +=1
    
kaco = mahasiswa("arfan muhadir","D0221530")
cicci = mahasiswa("resky","D0221030")
dinda = mahasiswa ("dian","D0221821")

kaco.hobby = "berenang"

print(mahasiswa.jurusan)
print(kaco.jurusan)
print(kaco.hobby)
print(cicci.jurusan)
print("jumlah mhs adalah",mahasiswa.jumlah_mhs)

print(mahasiswa.__dict__)
print(kaco.__dict__)







