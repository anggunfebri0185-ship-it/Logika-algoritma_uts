# Fungsi untuk membulatkan angka ke 2 desimal
# dan mengubah titik menjadi koma
def konversi_angka(angka):
    hasil = round(angka, 3)
    return str(hasil).replace(".", ",")