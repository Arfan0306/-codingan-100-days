# program list buku
list_buku = []
while True:
    print("\nmasukan data buku\n")
    judul = input("masukan judul buku\t:")
    penulis = input("masukan penullis\t:")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    
    print("\n","="*10,"data buku","="*10)
    print("No.| judul\t   | penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}  | {buku[0]} | {buku[1]}")


    print("\n","="*30)
    isLanjut = input("apakah anda ingin lanjut n/y")

    if isLanjut == "n":
        break

print("PROGRAM SELESAI")
