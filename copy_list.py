## teknik menduplikat list

a = ["arfan","ekki"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list

a [1] = "bangban"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f" address a = {hex(id(a))}")
print(f" address b = {hex(id(b))}")

# menduplikat list dengan copy c dengan a.copy()
c = a.copy()

print(f" address a = {hex(id(a))}")
print(f" address b = {hex(id(b))}")
print(f" address c = {hex(id(c))}")

print(" kita rubah data 0")
c[0] = "ekki"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(" kita rubah data 1")
a[1] = "reski"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


