#string
nama="arfan muhadir"
format_str = f"halo  {nama}"
print(format_str)

#angka
angka= 19
format_str = f"anga :{angka :d}"
#d menandakan bilangan bulat
print(format_str)

#boolean
boolean = True
format_str = f"ini adalah boolean : {boolean}"
print(format_str)

#bilangan dengan ordo ribuan
ribuan = 1000000
format_str = f"jutaan :{ribuan :,}"
print(format_str)

#bilngan desimal
desimal = 2003.1903
format_str =f"desimal : {desimal:.2f}"
#.2 untuk menampilkan 2 angka dibelakan koma dan f menandakan tipe data float
print(format_str)
