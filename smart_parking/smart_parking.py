import random

def buat_data_parkir(jumlah_slot):
    slots = []
    for i in range(jumlah_slot):
        status = random.randint(0, 1)
        slots.append(status)
    return slots


def hitung_ringkasan(slots):
    total_slot = len(slots)
    slot_terisi = sum(slots)
    slot_kosong = total_slot - slot_terisi
    return total_slot, slot_terisi, slot_kosong


def tentukan_kondisi(slot_kosong):
    if slot_kosong == 0:
        return "PENUH"
    elif slot_kosong <= 3:
        return "HAMPIR PENUH"
    else:
        return "MASIH TERSEDIA"


def tampilkan_status_slot(slots):
    for i in range(len(slots)):
        if slots[i] == 1:
            print("Slot", i + 1, ": TERISI")
        else:
            print("Slot", i + 1, ": KOSONG")


def tampilkan_dashboard(slots):
    total_slot, slot_terisi, slot_kosong = hitung_ringkasan(slots)
    kondisi = tentukan_kondisi(slot_kosong)

    print("===================================")
    print("SMART PARKING SYSTEM")
    print("===================================")
    print("Total slot      :", total_slot)
    print("Slot terisi     :", slot_terisi)
    print("Slot kosong     :", slot_kosong)
    print("Kondisi parkir  :", kondisi)
    print("===================================")

    tampilkan_status_slot(slots)


def main():
    jumlah_slot = 10

    while True:
        print("\n1. Jalankan simulasi")
        print("2. Keluar")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            data_parkir = buat_data_parkir(jumlah_slot)
            tampilkan_dashboard(data_parkir)

        elif pilihan == "2":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


main()