belanja = input("total: ")
uang = input("tunai: ")
kembalian = int(uang) - int(belanja)

def new_func(belanja, uang):
    print(f"total: {belanja}")
    print(f"uang: {uang}")

print(f"kembalian: Rp{kembalian:,.2f}")
