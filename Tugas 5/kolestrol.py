def hitung_kolesterol_total(ldl, hdl, trigliserida):
    """
    Fungsi untuk menghitung kadar kolesterol total.
    Kolesterol Total = LDL + HDL + (Trigliserida / 5)
    """
    return ldl + hdl + (trigliserida / 5)

def kategori_kolesterol(total_kolesterol):
    """
    Fungsi untuk menentukan kategori kolesterol berdasarkan nilai total.
    """
    if total_kolesterol < 200:
        return "Normal"
    elif 200 <= total_kolesterol <= 239:
        return "Borderline High"
    else:
        return "High"

def main():
    print("Program Penghitung Kolesterol")
    try:
        ldl = float(input("Masukkan kadar LDL (mg/dL): "))
        hdl = float(input("Masukkan kadar HDL (mg/dL): "))
        trigliserida = float(input("Masukkan kadar Trigliserida (mg/dL): "))
        
        total_kolesterol = hitung_kolesterol_total(ldl, hdl, trigliserida)
        kategori = kategori_kolesterol(total_kolesterol)
        
        print(f"\nHasil Perhitungan:")
        print(f"Kolesterol Total: {total_kolesterol:.2f} mg/dL")
        print(f"Kategori: {kategori}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()