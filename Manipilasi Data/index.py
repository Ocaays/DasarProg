import pandas as pd

data = pd.read_excel('data_penjualan.xlsx')

print("Data 5 baris pertama: ")
print(data.head())

data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']

print("\nData dengan kolom Total Harga: ")
print(data.head())

data_elektronik = data['Jumlah'] * data['Harga Satuan'] 

data_elektronik.to_excel('data_elektronik.xlsx', index=False) 

print("\nData elektronik telah disimpan")

rekap = data.groupby('Kategori')['Total Harga'].sum().reset_index()

rekap.columns = ['Kategori', 'Total Pendapatan']

print("\nRekap pendapatan per kategori: ")
print(rekap)

data_sorted = data.sort_values(by='Total Harga', ascending=False)

data_sorted.to_excel('data_sorted.xlsx', index=False)

print("\nData telah diurutkan berdasarkan Total Harga dan disimpan sebagai data_sorted.xlsx")
