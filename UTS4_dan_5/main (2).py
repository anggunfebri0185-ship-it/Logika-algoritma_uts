from utils import *

while True:
    print("\n1. Prisma Segi Tujuh")
    print("2. Prisma Segi Delapan")
    print("3. Limas Segi Empat")
    print("4. Limas Segi Lima")
    print("5. Kerucut Terpancung")
    print("6. Tabung Berongga")
    print("7. Bola Berongga")
    print("8. Prisma Segitiga Sama Sisi")
    print("9. Prisma Layang-Layang")
    print("10. Prisma Belah Ketupat")
    print("11. Keluar")

    pilih = int(input("\nPilih bangun ruang: "))

    if pilih == 1:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi: "))
        print("Volume:", prisma_segitujuh(la, t))

    elif pilih == 2:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi: "))
        print("Volume:", prisma_segidellapan(la, t))

    elif pilih == 3:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi limas: "))
        print("Volume:", limas_segempat(la, t))

    elif pilih == 4:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi limas: "))
        print("Volume:", limas_segilima(la, t))

    elif pilih == 5:
        r1 = float(input("Jari-jari atas: "))
        r2 = float(input("Jari-jari bawah: "))
        t = float(input("Tinggi: "))
        print("Volume:", kerucut_terpancung(r1, r2, t))

    elif pilih == 6:
        rl = float(input("Jari-jari luar: "))
        rd = float(input("Jari-jari dalam: "))
        t = float(input("Tinggi: "))
        print("Volume:", tabung_berongga(rl, rd, t))

    elif pilih == 7:
        rl = float(input("Jari-jari luar: "))
        rd = float(input("Jari-jari dalam: "))
        print("Volume:", bola_berongga(rl, rd))

    elif pilih == 8:
        la = float(input("Luas alas segitiga: "))
        t = float(input("Tinggi prisma: "))
        print("Volume:", prisma_segitiga_samasisi(la, t))

    elif pilih == 9:
        la = float(input("Luas alas layang-layang: "))
        t = float(input("Tinggi prisma: "))
        print("Volume:", prisma_layang_layang(la, t))

    elif pilih == 10:
        la = float(input("Luas alas belah ketupat: "))
        t = float(input("Tinggi prisma: "))
        print("Volume:", prisma_belah_ketupat(la, t))

    elif pilih == 11:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")