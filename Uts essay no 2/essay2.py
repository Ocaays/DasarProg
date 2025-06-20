nama = "NABILOCA"
if len(nama) < 8:
    print("minimal 7 karakter")
else:
    for i in range(len(nama)):
        
        print(nama[:i + 1] + '*' * (8 - (i + 1)))
