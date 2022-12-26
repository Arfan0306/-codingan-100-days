# program sederhana untuk menghitung rata-rata dari sejumlah bilangan

# meminta input dari user
n = int(input("Berapa banyak bilangan yang ingin Anda masukkan? "))

# inisialisasi variabel untuk menyimpan jumlah bilangan dan rata-rata
total = 0
average = 0

# meminta input dari user untuk setiap bilangan
for i in range(n):
    number = int(input(f"Masukkan bilangan ke-{i+1}: "))
    total += number

# menghitung rata-rata
average = total / n

# menampilkan hasil
print(f"Rata-rata dari {n} bilangan tersebut adalah {average}")
