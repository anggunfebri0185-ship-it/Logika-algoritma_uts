def konversi_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "A-"
    elif nilai >= 75:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "B-"
    elif nilai >= 60:
        return "C+"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"


def konversi_huruf_ke_angka(huruf):
    huruf = huruf.lower()
    if huruf == "a":
        return 4
    elif huruf == "a-":
        return 3.75
    elif huruf == "b+":
        return 3.5
    elif huruf == "b":
        return 3
    elif huruf == "b-":
        return 2.75
    elif huruf == "c+":
        return 2.5
    elif huruf == "c":
        return 2
    elif huruf == "d":
        return 1
    else:
        return 0


def hitung_total_sks(sks):
    return sum(sks)


def hitung_total_nilai(sks, nilai_angka):
    total = 0
    for i in range(len(sks)):
        huruf = konversi_nilai(nilai_angka[i])
        bobot = konversi_huruf_ke_angka(huruf)
        total += sks[i] * bobot
    return total


def hitung_ips(sks, nilai_angka):
    total_sks = sum(sks)
    if total_sks == 0:
        return 0
    total_nilai = hitung_total_nilai(sks, nilai_angka)
    return total_nilai / total_sks