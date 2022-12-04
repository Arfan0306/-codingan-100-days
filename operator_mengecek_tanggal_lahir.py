# check date of birth

import datetime as dt

print("silahkan masukan tanggal, \nbulan dan lahir anda \n")

tanggal =int(input("tanggal \t : "))
bulan =int(input("bulan \t\t : "))
tahun =int(input("tahun \t\t : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"hari lahir anda adalah : {tanggal_lahir:%A}")
