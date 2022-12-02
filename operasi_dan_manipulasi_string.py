# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "arfan"
nama_tengah = "m"
nama_belakan = "uhadir"

nama_lengkap = nama_pertama+" "+nama_tengah+"'"+nama_belakan
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dadri "+nama_lengkap+" : " + str(panjang))

# 3. operator untuk string
# mengecek apalah ada komponen char atau string di string

a ="a"
status = a in nama_lengkap
print( a + "ada di "+nama_lengkap + " :"+str(status))


A ="A"
status = A in nama_lengkap
print( A + "ada di "+nama_lengkap + " :"+str(status))

a ="a"
status = a not in nama_lengkap
print( a + "ada di "+nama_lengkap + " :"+str(status))

# mengulang string
print("ha"*10)
print(15*"ha")


