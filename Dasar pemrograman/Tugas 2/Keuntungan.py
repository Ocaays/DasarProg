def hitung_keuntungan(jumlah_domba):
    harga_dasar = 2500000
    harga_jual = 3000000

    total_modal = jumlah_domba * harga_dasar
    total_penjualan = jumlah_domba * harga_jual
    keuntungan = total_penjualan - total_modal

    return total_modal, keuntungan

def main():
    jumlah_domba = int(input("Masukkan jumlah domba yang dijual: "))
    total_modal, keuntungan = hitung_keuntungan(jumlah_domba)

    print(f"Total modal yang dikeluarkan: Rp{total_modal:,.2f}")
    print(f"Keuntungan yang didapat: Rp{keuntungan:,.2f}")

if __name__ == "__main__":
    main()