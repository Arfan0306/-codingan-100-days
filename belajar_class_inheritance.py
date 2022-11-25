class orang():
    def __init__(self,nama,transmisi,daerah):
        self.nama=nama
        self.transmisi = transmisi
        self.daerah = daerah
    def cek_id_nama(self):
        print("nama :",self.nama,"\nmotor :",self.transmisi,"\ndaerah :",self.daerah)

class manusia(orang):
    def cek_id_nama(self):
        print("cek id nama")
    
orang1 = orang("randi","manual","majene")
orang2 = manusia("sulham","otomatis","sendana")

orang1.cek_id_nama()
orang2.cek_id_nama()
