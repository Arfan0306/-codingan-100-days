# Date and time (latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2003,3,6)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")
