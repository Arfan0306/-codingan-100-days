#input output file

"""

w = write mode / mode tulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = oppending mode / menambahkan data di akhir baris
r+ write and read mode

"""

#membuat file text
file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nini baris ke dua")
file.write("\nini baris ke tiga")
file.write("\nini baris ke empat")
file.close()

#membaca file text
file2 = open("data.txt",'r')

#cara pertama bisa menampilkan seluruh baris dan juga bisa menampilkan karakter dengan cara print(file2.read(10)) jika dimasukan 10 maka akan muncul 10 karakter 
print(file2.read())
#cara kedua menampilkan satu baris jika ingin menampilakn dua baris maka lakukan dengan cara yg sama seperti di bawah
#print(file2.readline())
file2.close()

#oppending mode
file3 = open("data.txt",'a')

file3.write("\nbaris ini dibuat dengan menggunakan mode append")
file3.close()

