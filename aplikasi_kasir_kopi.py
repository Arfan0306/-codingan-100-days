pilihan ="y"
while pilihan == "y":
    print("""
==================================
1. Kopi hitam :Rp.10.000
2. Kopi susu :Rp.5.000
    ==================================
""")
    pesan=int(input("masukan no pesanan :"))
    jumlah_pesanan = int(input("masukan jumlah pesanan :"))
    if pesan == 1:
        list_nama ="kopi hitam"
        harga=(10000*jumlah_pesanan)
        ppn = int(harga*0.1)
        if jumlah_pesanan >= 5:
            diskon=int(harga*0.2)
            total_harga = int(harga-diskon+ppn)
        else:
            diskon=0
            total_harga = int(harga+ppn)
    elif pesan == 2:
        list_nama ="kopi susu"
        harga=5000*jumlah_pesanan
        ppn = int(harga*0.1)
        if jumlah_pesanan >5:
            diskon =int(harga*0.2)
            total_harga =int(harga-diskon+ppn)
        else:
            diskon=0
            total_harga=int(harga+ppn)
    else:
        print("pesanan yang anda masukan tdk ada")
        pilihan =input("menu tdk tersedia silahkan masuk ulang dengan menu y/n")

    print("===========================================")
    print("selamat datang di mesin kasir saya")
    print("menu :",list_nama)
    print("jumlah pesanan :",jumlah_pesanan)
    print("harga :",harga)
    print("diskon :",diskon)
    print("ppn :",ppn)
    print("===========================================")
    print("jumlah bayar :",total_harga)
    print("===========================================")
    pilihan=input("apakah anda ingin order lagi ? jika ya pipih y, jika tdk pilih n :")
    
    
    
            
