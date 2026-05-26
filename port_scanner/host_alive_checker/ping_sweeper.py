import os
import platform
import threading
import sys


aktif_cihazlar = []


def ping_at(ip):
    isletim_sistemi = platform.system()

    if isletim_sistemi == "Windows":
        parametre = "-n 1"
        komut = "ping " + parametre + " " + ip + " > nul"
    else:
        parametre = "-c 1"
        komut = "ping " + parametre + " " + ip + " > /dev/null 2>&1"

    cevap = os.system(komut)

    if cevap == 0:
        print("[+] " + ip + " aktif")
        aktif_cihazlar.append(ip)


print("=== Basit Python Ping Sweeper ===")
ip_blok = input("IP blogunu girin (orn: 192.168.1.): ")
baslangic = input("Baslangic numarasi (orn: 1): ")
bitis = input("Bitis numarasi (orn: 50): ")

baslangic = int(baslangic)
bitis = int(bitis)

print("")
print("Tarama basliyor: " + ip_blok + str(baslangic) + " - " + ip_blok + str(bitis))
print("")

thread_listesi = []

for i in range(baslangic, bitis + 1):
    hedef_ip = ip_blok + str(i)
    t = threading.Thread(target=ping_at, args=(hedef_ip,))
    t.start()
    thread_listesi.append(t)

for t in thread_listesi:
    t.join()

print("")
print("Tarama tamamlandi.")
print("Toplam aktif cihaz sayisi: " + str(len(aktif_cihazlar)))
