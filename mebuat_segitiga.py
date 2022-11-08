angka = ""
a = 1

nilai = int(input("Masukkan angka :"))

# Looping Baris
while a <= nilai:
    var = a
    # Looping Kolom
    while var > 0:
        angka = angka + " * "
        var = var - 1	
    angka = angka+ "\n"
    a = a + 1
print (angka)
