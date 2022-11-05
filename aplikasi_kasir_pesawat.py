nama_pembeli = input("masukan nama pembeli :")
kode_pesawat = input("masukan kode pesawat S/C :")
kode_tujuan = input("masukan kode tujuan L/D:")
jumlah_tiket = int(input("masukan jumlah tiket :"))


if kode_pesawat =="S":
    nama_pesawat="SAUDI ARABIA"
    if kode_tujuan =="L":
        keterangan = "Luar Negri"
        harga=5500000
    elif kode_tujuan =="D":
        keterangan="Dalam Negri"
        harga=5000000
    else:
        harga:0
elif kode_pesawat =="C":
    nama_pesawat="CATHAY PACIFIC"
    if kode_tujuan =="L":
        keterangan = "Luar Negri"
        harga=7500000
    elif kode_tujuan =="D":
        keterangan="Dalam Negri"
        harga=7000000
    else:
        harga:0
else:
    nama_pesawat="Anda Salah Input"
    harga=0
#jumlah tiket
while jumlah_tiket < 5:
    break
#jumlah bayar
jumlah_bayar=harga*jumlah_tiket

#potongan
if jumlah_bayar > 15000000:
    potongan = int(jumlah_bayar/100*1)
else:
    potongan=0
total_bayar = jumlah_bayar - potongan

print(f"NAMA PEMBELI :",nama_pembeli)
print(f"KODE PESAWAT :",kode_pesawat)
print(f"NAMA PESAWAT :",nama_pesawat)
print(f"TUJUAN :",keterangan)
print(f"HARGA TIKET :",harga)
print(f"JUMLAH TIKET :",jumlah_tiket)
print(f"JUMLAH BAYAR:",jumlah_bayar)
print(f"POTONGAN :",potongan)
print(f"TOTAL BAYAR :",total_bayar)


