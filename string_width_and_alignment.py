# width and multiline

#data
data_nama ="kaco tiwe"
data_umur=15
data_tinggi=130.1
data_nomor_sepatu = 37

#string
data_string=f"nama ={data_nama}, umur ={data_umur},tinggi ={data_tinggi},sepatu ={data_nomor_sepatu}"
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

# string multiline ( dengan menggunakan enter, newline, \n)
data_string=f"nama ={data_nama}, \numur ={data_umur},\ntinggi ={data_tinggi},\nsepatu ={data_nomor_sepatu}"
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string =f"""
nama = {data_nama}
umur = {data_umur}
tinggi ={data_tinggi}
nomor sepatu ={data_nomor_sepatu}
"""
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

# mengatur lebar
data_string =f"""
nama         ={data_nama:>10}
umur         ={data_umur}
tinggi       ={data_tinggi}
nomor sepatu ={data_nomor_sepatu}
"""
print("\n"+5*"="+"data string"+5*"=")
print(data_string)
