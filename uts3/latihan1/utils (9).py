# Mengubah input menjadi list nilai
def parse_nilai(data):
    return list(map(int, data.split(",")))

# Menghitung rata-rata nilai
def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)