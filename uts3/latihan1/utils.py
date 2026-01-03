# Fungsi untuk mengubah input menjadi list nilai
def parse_nilai(data):
    return list(map(int, data.split(",")))

# Fungsi untuk mencari nilai terbesar
def cari_terbesar(nilai):
    return max(nilai)

# Fungsi untuk mencari nilai terkecil
def cari_terkecil(nilai):
    return min(nilai)
