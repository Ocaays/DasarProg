data_mahasiswa = {}

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    if nim in data_mahasiswa:
        print("Data dengan NIM tersebut sudah ada.\n")
        return
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    try:
        ipk = float(input("Masukkan IPK: "))
        data_mahasiswa[nim] = {
            "Nama": nama,
            "Jurusan": jurusan,
            "IPK": ipk
        }
        print("Data mahasiswa berhasil ditambahkan.\n")
    except ValueError:
        print("IPK harus berupa angka desimal (contoh: 3.5).\n")

def tampilkan_semua_mahasiswa():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.\n")
        return
    print(f"{'NIM':<10}{'Nama':<20}{'Jurusan':<20}{'IPK':<5}")
    print("-" * 55)
    for nim, info in data_mahasiswa.items():
        print(f"{nim:<10}{info['Nama']:<20}{info['Jurusan']:<20}{info['IPK']:<5}")
    print()

def cari_mahasiswa():
    nim = input("Masukkan NIM mahasiswa yang dicari: ")
    if nim in data_mahasiswa:
        info = data_mahasiswa[nim]
        print(f"\nData Mahasiswa NIM {nim}:")
        print(f"Nama    : {info['Nama']}")
        print(f"Jurusan : {info['Jurusan']}")
        print(f"IPK     : {info['IPK']}\n")
    else:
        print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.\n")

def hapus_mahasiswa():
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.\n")
    else:
        print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.\n")

def menu():
    while True:
        print("===== MENU PENGELOLAAN DATA MAHASISWA =====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data Mahasiswa")
        print("3. Cari Data Mahasiswa Berdasarkan NIM")
        print("4. Hapus Data Mahasiswa Berdasarkan NIM")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_mahasiswa()
        elif pilihan == '2':
            tampilkan_semua_mahasiswa()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            hapus_mahasiswa()
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.\n")

menu()
