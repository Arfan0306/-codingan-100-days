data_product={
    1:"HP        ",
    2:"cas hp    ",
    3:"cesing    ",
    4:"anti gores",

}
harga_product={
    1:3000000,
    2:50000,
    3:25000,
    4:15000

}
dict_trx ={}
daftar_metode_pembayaran={
    1:"tranfer bank   ",
    2:"virtual account",
    3:"cas on deliveri",
    4:"katu kredit    "

}
print("=============List produk=============")
for i in data_product:
    print("id produk :",i,"\tnama_prodak :",
          data_product[i],"\tharga produk :",harga_product[i])
pilihan_id= int(input("pilih id product :"))
if pilihan_id in data_product:
    pilihan_beli = input("ingin beli ? (y/n) : ")
    if pilihan_beli =="y":
        nama_penerima    = input("nama penerima    :")
        alamat_penerima  = input("alamat penerima  :")
        no_hp            = input("no hp            :")
        kurir_pengiriman = input("kurir pengiriman :")
        dict_trx ={
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "no hp":no_hp,
            "kurir pengiriman":kurir_pengiriman,
            "product id":data_product,
        }
    else:
        pass
    if len (dict_trx) > 0:
        print("================= metode pembayaran===============")
        for i in daftar_metode_pembayaran:
            print("id :", i,"\t metode pembayaran :",daftar_metode_pembayaran[i])
        pilih_metode = int(input("pilih id metode pembayaran :"))
        if pilihan_id in daftar_metode_pembayaran :
            print("nama penerima :",dict_trx["nama penerima"])
            print("alamat penerima :",dict_trx["alamat penerima"])
            print("no hp :",dict_trx["no hp"])
            print("kurir pengiriman :",dict_trx["kurir pengiriman"])
            print("product id :",data_product[pilihan_id])
            print("harga :",harga_product[pilihan_id])
            print("pembayaran :",daftar_metode_pembayaran[pilihan_id])
            konfirmasi=input("apakah anda yakin ingin melalukan pembayaran? y/n :")
            if konfirmasi == "y":
                print("anda sudah melakukan pembayaran")
            else:
                print("metode pembayaran tdk tersedia")
    else:
        print("id product tdk teredia")
    
            
