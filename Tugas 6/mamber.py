data = [{"nama":"Nugraha", "Birtdate":"1989-09-13"},
        {"nama":"John", "Birtdate":"1990-01-01"},
        {"nama":"Jane", "Birtdate":"1992-02-02"},
        {"nama":"Doe", "Birtdate":"1994-03-03"}]

print("+----+---------+------------+")
print("| No | Nama    | Birtdate   |")
print("+----+---------+------------+")
for x , item in enumerate(data, start=1):
     print(f"| {x:<2} | {item['nama']:<7} | {item['Birtdate']} |")
print("+----+---------+------------+")
