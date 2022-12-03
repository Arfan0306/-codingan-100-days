# operator dalam bentuk string

## merubah case dari string

# merubah semua ke upper case

salam = "halo bro!"
print("normal : "+salam)
salam = salam.upper()
print("upper : "+salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeeZzzzZZ"
print("normal : "+alay)
alay = alay.lower()
print("lower : "+alay)

## mengecek dengan isX method

# contoh pengecekan lower case
salam = "list"
apakah_lower = salam.islower() #hasilnya bool
print(salam + "is lower : " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + "is upper : " + str(apakah_upper))
