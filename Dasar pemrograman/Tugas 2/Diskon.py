total = float(input("total belanja: "))
diskon = float(input("diskon: "))

def new_func(total, diskon):
    print(f"total belanja: Rp{int(total)}")
    print(f"diskon: {int(diskon)}%")  
    
    total_diskon = total * diskon / 100
    total_bayar = total - total_diskon
    print(f"total bayar: Rp{total_bayar:,.2f}")

new_func(total, diskon)