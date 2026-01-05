from utils import *

def menu():
    print("\n===== menu =====")
    print("1. konversi nilai ke label")
    print("2. konversi label ke bobot")
    print("3. hitung total sks yang diambil")
    print("4. hitung total nilai")
    print("5. hitung IPS")
    print("6. exit")


def main():
    while True:
        menu()
        pilihan = input("\nPilihan: ")

        # 1. Konversi nilai ke label
        if pilihan == "1":
            nilai = int(input("\nNilai Mahasiswa: "))
            print("Label:", konversi_nilai(nilai))

        # 2. Konversi label ke bobot
        elif pilihan == "2":
            huruf = input("\nLabel Nilai: ")
            bobot = konversi_huruf_ke_angka(huruf)
            print("Bobot:", bobot)

        # 3. Total SKS
        elif pilihan == "3":
            jumlah = int(input("\nJumlah Data: "))
            sks = []
            print("---------- input sks ----------")
            for i in range(jumlah):
                sks.append(int(input(f"SKS {i+1}: ")))
            print("\nTotal SKS:", hitung_total_sks(sks))

        # 4. Total Nilai (SESUAI GAMBAR)
        elif pilihan == "4":
            jumlah = int(input("\nJumlah Data: "))
            sks = []
            nilai = []

            print("---------- input sks ----------")
            for i in range(jumlah):
                sks.append(int(input(f"SKS {i+1}: ")))

            print("\n---------- input Nilai Mahasiswa ----------")
            for i in range(jumlah):
                nilai.append(int(input(f"Nilai {i+1}: ")))

            print("\nTotal Nilai:", hitung_total_nilai(sks, nilai))

        # 5. IPS (SESUAI GAMBAR)
        elif pilihan == "5":
            jumlah = int(input("\nJumlah Data: "))
            sks = []
            nilai = []

            print("---------- input sks ----------")
            for i in range(jumlah):
                sks.append(int(input(f"SKS {i+1}: ")))

            print("\n---------- input Nilai Mahasiswa ----------")
            for i in range(jumlah):
                nilai.append(int(input(f"Nilai {i+1}: ")))

            print("\nIPS:", round(hitung_ips(sks, nilai), 1))

        # 6. Exit
        elif pilihan == "6":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak tersedia!")


if __name__ == "__main__":
    main()