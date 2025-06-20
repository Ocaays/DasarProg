harga_mesin = int(input("masukkan harga mesin:"))
masa = int(input("masukkan masa manfaat:"))
nilai_sisa = int(input("nilai sisa:"))
penyusutan = int(input("masukkan berapa lama digunakan:"))

penyusutan_tahun = (harga_mesin - nilai_sisa) / masa

penyusutan_selama = (penyusutan_tahun * penyusutan)

hitung_nilai_aset = (harga_mesin - penyusutan_selama)

print("penyusutan_tahun: ", int(penyusutan_tahun))
print("penyusutan_selama: ", int(penyusutan_selama))
print("hitung_nilai_aset: ", int(hitung_nilai_aset))

