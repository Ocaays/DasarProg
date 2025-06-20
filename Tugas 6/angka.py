a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka: "))
c = int(input("Masukkan angka: "))

terbesar = a

if (a >= b) and (a >= c):
    terbesar = a
elif (b >= a) and (b >= c):
    terbesar = b
else:
    terbesar = c

print("Angka terbesar adalah", terbesar)
