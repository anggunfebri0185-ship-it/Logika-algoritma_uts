def parse_harga(data):
    return list(map(int, data.split(",")))

def hitung_total(harga):
    return sum(harga)

def hitung_pajak(total):
    if total >50:
        return total * 0.1 
    else:
        return 0

def format_rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")