# Program Python untuk menghitung indeks massa tubuh (BMI)

# Mendefinisikan fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
  bmi = berat / (tinggi ** 2)
  return bmi

# Meminta pengguna untuk memasukkan berat dan tinggi
berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))

# Menghitung BMI
bmi = hitung_bmi(berat, tinggi)

# Menampilkan hasil BMI ke pengguna
print("Indeks massa tubuh Anda adalah:", bmi)

# Menampilkan kategori BMI berdasarkan hasil BMI
if bmi < 18.5:
  print("Anda termasuk kategori underweight.")
elif 18.5 <= bmi < 25:
  print("Anda termasuk kategori normal.")
elif 25 <= bmi < 30:
  print("Anda termasuk kategori overweight.")
else:
  print("Anda termasuk kategori obesity.")
