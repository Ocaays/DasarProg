from datetime import datetime
tahun_ini = datetime(2025,9,13)
data = [
    {"name": "Nugraha", "birtdate": "1989-09-13"},
    {"name": "John", "birtdate": "1990-01-01"},
    {"name": "Jane", "birtdate": "1992-02-02"},
    {"name": "Doe", "birtdate": "1994-03-03"},
]


print(f"{'No':<5} {'Name:<10'} {'Age':<5}")


for index, person in enumerate(data, start=1):
    birthdate = datetime.strptime(person["birtdate"], "%Y-%m-%d")
    age = (tahun_ini - birthdate).days // 365
    print (f"{index:<5} {person['name']:<10} {age:<5}")