angka1=int(input("masukan angka1 : "))
angka2=int(input("masukan angka2 : "))

pilihann="pilihan :\n1. penjumlahan\n2. pengurangan\n3. perkalian\n4. pembagian\n"
print(pilihann)

pilihan=int(input("masukan pilihan : "))
if pilihan == 1:
    hasil = angka1 + angka2
    print(angka1,"+",angka2,"=",hasil)
elif pilihan == 2:
    hasil = angka1 - angka2
    print(angka1,"-",angka2,"=",hasil)
elif pilihan == 3:
    hasil = angka1 * angka2
    print(angka1,"X",angka2,"=",hasil)
elif pilihan == 4:
    hasil = angka1 / angka2
    print(angka1,"/",angka2,"=",hasil)
else:
    print("pilihan yang anda masukan tidak ada")
