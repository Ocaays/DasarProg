a = int(input("Masukan bilangan a: "))
b = int(input("Masukan bilangan b: "))
c = int(input("Masukan bilangan c: "))

if (a > b or b > c) and (a % 5 == 0 and c % 5 == 1) and (b != c):
    print("Kondisi terpenuhi")
else:
    print("Kondisi tidak terpenuhi")