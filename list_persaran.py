data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"ini adalah list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,5,6]
print(f"list 2D = {list_2D}")

# contoh penggunaan

peserta_0 = ["arfan",20,"laki-laki"]
peserta_1 = ["reski",19,"perempuan"]
peserta_2 = ["cicci",10,"kaco"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"list peserta = {list_peserta}")
for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"gender\t : {peserta[2]}\n")
