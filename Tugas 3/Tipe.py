def cek_tipe(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3,float):
        return "Tipe input valid!!"
    else:
        return "Tipe input tidak valid!!"
    
print(cek_tipe(2006, 6, 0.2))
print(cek_tipe("ocax", 2, 0.2))
print(cek_tipe("mocca", 5, 0.5))
print(cek_tipe(2006, 10, "3.14"))
print(cek_tipe(06.05 , -5, 2.25))