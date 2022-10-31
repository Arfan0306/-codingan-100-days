#menginputkan panjang dan lebar tanah
panjang= int(input("masukan panjang tanah : "))
lebar= int(input("masukan lebar tanah : "))
harga_per_meter = 500000

#mengengethui luas tanah
luas = panjang*lebar

#mencari harga keseluruhan tanah
hasil= luas*harga_per_meter

#hasil dari jual tanah
print("luas keseluruhan tanah :",luas,"cm")
print("harga jual tanah adalah :Rp.",hasil)


