# Fungsi untuk mengubah angka menjadi format Rupiah
def format_rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")