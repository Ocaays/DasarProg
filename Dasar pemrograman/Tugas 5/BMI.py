def hitung_BMi (berat,tinggi):
    bmi = berat / (tinggi **2)
    if bmi > 18.5 :
        return f"BMI:{bmi:.2f} (kekurangan berat badan)"
    elif bmi > 25.0 :
        return f"BMi:{bmi:.2f} (normal)"
    elif bmi > 30.0 :
        return f"BMI:{bmi:.2f} (kelebihan berat badan)"
    else:
        return f"BMI:{bmi:.2f} (obesitas)"
    
berat =float(input("masukan berat badan (kg): "))
tinggi =float(input("masukan tinggi badan (m): "))

print(hitung_BMi(berat,tinggi))