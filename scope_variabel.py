#sifatnya global
nama="arfan"
def a():
    #sifatnya local
    nama="muhadir"
    print(nama)
a()
print(nama)
