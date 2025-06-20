import random

def ambil_pilihan_komputer():
    return random.choice(['batu', 'gunting', 'kertas'])

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_pemain == pilihan_komputer:
        return "Seri"
    elif (pilihan_pemain == 'batu' and pilihan_komputer == 'gunting') or \
         (pilihan_pemain == 'gunting' and pilihan_komputer == 'kertas') or\
         (pilihan_pemain == 'kertas' and pilihan_komputer == 'batu'):
         return "Pemain Menang"
    else:
        return "Komputer Menang"
    
def main():
    skor_pemain = 0
    skor_komputer = 0
    
    while True:
        print("\nPilihan: batu, gunting, kertas")
        pilihan_pemain = input("Masukan pilihan anda: ").lower()
        
        if pilihan_pemain not in ['batu', 'gunting', 'kertas']:
            print("Pilihan tidak valid. Silahkan coba lagi.")
            continue
        
        pilihan_komputer = ambil_pilihan_komputer()
        print(f"pilihan komputer: {pilihan_komputer}")
        
        hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
        print(hasil)
        
        if hasil == "Pemain Menang":
            skor_pemain += 1
        elif hasil == "Komputer Menang":
            skor_komputer += 1
            
        print(f"Skor - pemain: {skor_pemain}, komputer: {skor_komputer}")
        
        lanjutkan = input("Apakah anda ingin melanjutkan permainan? (ya/tidak): ").lower()
        if lanjutkan != 'ya':
            break
        
    print("Terimakasih telah bermain!")
    print(f"skor akhir.  pemain: {skor_pemain}, komputer: {skor_komputer}")
    
if __name__ == "__main__":
    main()