# Mengubah input menjadi list angka
def parse_angka(data):
    return list(map(int, data.split(",")))

# Menghitung total dari list angka
def hitung_total(data):
    return sum(data)