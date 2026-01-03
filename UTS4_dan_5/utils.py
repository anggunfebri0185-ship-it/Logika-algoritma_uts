import math

def segitiga_sama_sisi_keliling(s):
    return 3 * s

def segitiga_sama_kaki_luas(alas, tinggi):
    return 0.5 * alas * tinggi

def segitiga_sembarang_keliling(a, b, c):
    return a + b + c

def trapesium_sama_kaki_keliling(a, b, c):
    return a + b + 2 * c

def trapesium_sama_sisi_luas(a, t):
    return 0.5 * a * t

def layang_layang_keliling(a, b):
    return 2 * (a + b)

def belah_ketupat_keliling(s):
    return 4 * s

def setengah_lingkaran_luas(r):
    return 0.5 * math.pi * r * r

def diagonal_persegi_panjang(p, l):
    return math.sqrt(p*p + l*l)

def jajargenjang_keliling(a, b):
    return 2 * (a + b)