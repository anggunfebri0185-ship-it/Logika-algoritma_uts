# Fungsi untuk mengubah input menjadi list nilai
def parse_nilai(data):
    return list(map(int, data.split(",")))

# Fungsi untuk menentukan kelulusan
def tentukan_kelulusan(nilai, kkm=75):
    rata_rata = sum(nilai) / len(nilai)
    if rata_rata >= kkm:
        return rata_rata, "LULUS"
    else:
        return rata_rata, "TIDAK LULUS"