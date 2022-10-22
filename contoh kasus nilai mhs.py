nama =input("masukan nama :")
nilai = int(input("masukan nilai mhs :"))

if nilai >= 80 and nilai < 100:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
elif nilai >= 50:
    print("D")
else:
    print("E")
