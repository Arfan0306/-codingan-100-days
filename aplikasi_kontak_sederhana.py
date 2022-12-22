# Program Python untuk membuat aplikasi kontak

# Mendefinisikan dictionary untuk menyimpan kontak
while True:
    kontak = {}

    # Meminta pengguna untuk memasukkan kontak baru
    nama = input("Masukkan nama: ")
    nomor_telepon = input("Masukkan nomor telepon: ")

    # Menambahkan kontak baru ke dictionary
    kontak[nama] = nomor_telepon

    # Menampilkan semua kontak yang tersimpan dalam dictionary
    print("Kontak:")
    for nama, nomor_telepon in kontak.items():
      print(nama, ":", nomor_telepon)

    # Meminta pengguna untuk mencari kontak
    cari = input("Cari kontak: ")

    # Mencari kontak yang diminta pengguna
    if cari in kontak:
      print("Nama:", cari)
      print("Nomor telepon:", kontak[cari])
    else:
      print("Kontak tidak ditemukan.")
