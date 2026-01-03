import math

def prisma_segitujuh(luas_alas, tinggi):
    return luas_alas * tinggi

def prisma_segidellapan(luas_alas, tinggi):
    return luas_alas * tinggi

def limas_segempat(luas_alas, tinggi):
    return (1/3) * luas_alas * tinggi

def limas_segilima(luas_alas, tinggi):
    return (1/3) * luas_alas * tinggi

def kerucut_terpancung(r1, r2, t):
    return (1/3) * math.pi * t * (r1**2 + r1*r2 + r2**2)

def tabung_berongga(r_luar, r_dalam, t):
    return math.pi * t * (r_luar**2 - r_dalam**2)

def bola_berongga(r_luar, r_dalam):
    return (4/3) * math.pi * (r_luar**3 - r_dalam**3)

def prisma_segitiga_samasisi(luas_alas, tinggi):
    return luas_alas * tinggi

def prisma_layang_layang(luas_alas, tinggi):
    return luas_alas * tinggi

def prisma_belah_ketupat(luas_alas, tinggi):
    return luas_alas * tinggi