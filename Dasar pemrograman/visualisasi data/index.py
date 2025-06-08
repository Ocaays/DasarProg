import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data_penjualan.xlsx'  
df = pd.read_excel(file_path, sheet_name='Penjualan')

df["Total Penjualan"] = df["Jumlah"] * df["Harga Satuan"]

def klasifikasi_nilai(total):
    if total >= 10000000:
        return 'A'
    elif total >= 7000000:
        return 'B'
    elif total >= 4000000:
        return 'C'
    else:
        return 'D'

df["Kelompok Nilai"] = df["Total Penjualan"].apply(klasifikasi_nilai)

nilai_counts = df["Kelompok Nilai"].value_counts().sort_index()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.pie(nilai_counts, labels=nilai_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribusi Persentase Kelompok Nilai')

plt.subplot(1, 2, 2)
plt.bar(nilai_counts.index, nilai_counts.values, color=plt.cm.Paired.colors)
plt.title('Jumlah Data per Kelompok Nilai')
plt.xlabel('Kelompok Nilai')
plt.ylabel('Jumlah Data')

plt.tight_layout()
plt.show()
