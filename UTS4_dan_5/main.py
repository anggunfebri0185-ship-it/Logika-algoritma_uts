from utils import *

while True:
    print("\n1. Segitiga Sama Sisi")
    print("2. Segitiga Sama Kaki")
    print("3. Segitiga Sembarang")
    print("4. Trapesium Sama Kaki")
    print("5. Trapesium Sama Sisi")
    print("6. Layang-Layang")
    print("7. Belah Ketupat")
    print("8. Setengah Lingkaran")
    print("9. Persegi Panjang")
    print("10. Jajar Genjang")
    print("11. Keluar")

    pilih = int(input("\nPilih bangun datar: "))

    if pilih == 1:
        s = float(input("Masukkan sisi: "))
        print("Keliling:", segitiga_sama_sisi_keliling(s))

    elif pilih == 2:
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas:", segitiga_sama_kaki_luas(a, t))

    elif pilih == 3:
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        c = float(input("Sisi c: "))
        print("Keliling:", segitiga_sembarang_keliling(a, b, c))

    elif pilih == 4:
        a = float(input("Sisi sejajar a: "))
        b = float(input("Sisi sejajar b: "))
        c = float(input("Sisi miring: "))
        print("Keliling:", trapesium_sama_kaki_keliling(a, b, c))

    elif pilih == 5:
        a = float(input("Sisi sejajar: "))
        t = float(input("Tinggi: "))
        print("Luas:", trapesium_sama_sisi_luas(a, t))

    elif pilih == 6:
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        print("Keliling:", layang_layang_keliling(a, b))

    elif pilih == 7:
        s = float(input("Masukkan sisi: "))
        print("Keliling:", belah_ketupat_keliling(s))

    elif pilih == 8:
        r = float(input("Masukkan jari-jari: "))
        print("Luas:", setengah_lingkaran_luas(r))

    elif pilih == 9:
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        print("Diagonal:", diagonal_persegi_panjang(p, l))

    elif pilih == 10:
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        print("Keliling:", jajargenjang_keliling(a, b))

    elif pilih == 11:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")