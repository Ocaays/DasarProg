inventaris = {}

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    try:
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
        inventaris[nama] = (harga, stok)
        print(f"Barang '{nama}' berhasil ditambahkan.\n")
    except ValueError:
        print("Input harga atau stok tidak valid.\n")

def tampilkan_barang():
    if not inventaris:
        print("Inventaris kosong.\n")
        return
    print(f"{'Nama Barang':<20}{'Harga':<10}{'Stok':<10}")
    print("-" * 40)
    for nama, (harga, stok) in inventaris.items():
        print(f"{nama:<20}{harga:<10}{stok:<10}")
    print()

def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    if nama in inventaris:
        harga, stok = inventaris[nama]
        print(f"Detail barang '{nama}': Harga = {harga}, Stok = {stok}\n")
    else:
        print(f"Barang '{nama}' tidak ditemukan.\n")

def perbaharui_stok():
    nama = input("Masukkan nama barang yang ingin diperbarui: ")
    if nama in inventaris:
        try:
            stok_baru = int(input("Masukkan jumlah stok baru: "))
            harga = inventaris[nama][0]
            inventaris[nama] = (harga, stok_baru)
            print(f"Stok barang '{nama}' berhasil diperbarui.\n")
        except ValueError:
            print("Input stok tidak valid.\n")
    else:
        print(f"Barang '{nama}' tidak ditemukan.\n")

def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    if nama in inventaris:
        del inventaris[nama]
        print(f"Barang '{nama}' berhasil dihapus dari inventaris.\n")
    else:
        print(f"Barang '{nama}' tidak ditemukan.\n")

def analisis_data():
    if not inventaris:
        print("Inventaris kosong.\n")
        return
    harga_tertinggi = max(inventaris.items(), key=lambda x: x[1][0])
    harga_terendah = min(inventaris.items(), key=lambda x: x[1][0])
    total_nilai_stok = sum(harga * stok for harga, stok in inventaris.values())

    print(f"Barang dengan harga tertinggi: {harga_tertinggi[0]} (Rp{harga_tertinggi[1][0]})")
    print(f"Barang dengan harga terendah: {harga_terendah[0]} (Rp{harga_terendah[1][0]})")
    print(f"Total nilai seluruh stok: Rp{total_nilai_stok}\n")

def menu():
    while True:
        print("===== SISTEM MANAJEMEN INVENTARIS =====")
        print("1. Tambah Barang Baru")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang")
        print("4. Perbaharui Stok Barang")
        print("5. Hapus Barang")
        print("6. Analisis Data")
        print("7. Keluar Program")
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            cari_barang()
        elif pilihan == '4':
            perbaharui_stok()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            analisis_data()
        elif pilihan == '7':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-7.\n")

menu()
