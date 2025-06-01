def jenis_segitiga (a,b,c):
    if a + b > c and a + c > b and b + c > a :
        if a == b == c :
            return "segitiga sama sisi"
        elif a == b or a == c or b == c:
            return "segitiga sama kaki"
        else:
            return "segitiga sembarang"
    return "bukan segitiga"

a = float(input("masukan sisi pertama: "))
b = float(input("masukan sisi kedua: "))
c = float(input("masukan input ketiga: "))

print(jenis_segitiga(a, b, c))
        