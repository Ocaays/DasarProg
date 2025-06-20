from eccommerce.pricing import hitung_diskon, hitung_total, hitung_pajak
from eccommerce.order import generate_order_id


def main():
    
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    nama_produk = input("Masukkan nama produk: ")
    harga_produk = float(input("Masukkan harga produk: "))
    persentase_diskon = float(input("Masukkan persentase diskon: "))
    persentase_pajak = float(input("Masukkan persentase pajak: "))

    diskon = harga_produk * (persentase_diskon / 100)

    total = hitung_total(harga_produk, persentase_diskon, persentase_pajak)
    order_id = generate_order_id()

    print("=" * 40)
    print("         RINCIAN PEMBELIAN")
    print("=" * 40)
    print(f"{'ID Pesanan':20}: {order_id}")
    print(f"{'Nama Pelanggan':20}: {nama_pelanggan}")
    print(f"{'Nama Produk':20}: {nama_produk}")
    print(f"{'Harga Produk':20}: Rp {harga_produk:,.2f}")
    print(f"{'Diskon':20}: Rp {diskon:,.2f}")
    print(f"{'Pajak':20}: Rp {hitung_pajak(harga_produk, persentase_pajak):,.2f}")
    print("-" * 40)
    print(f"{'Total':20}: Rp {total:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()