import socket
import threading
import sys
from datetime import datetime

portlar = [21, 22, 23, 25, 80, 443, 445, 3389]
acik_portlar = []

def port_tara(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        sonuc = s.connect_ex((ip, port))
        if sonuc == 0:
            banner = ""
            try:
                s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                veri = s.recv(1024)
                banner = veri.decode(errors="ignore").strip()
                banner = banner.replace("\n", " ").replace("\r", " ")
                if len(banner) > 100:
                    banner = banner[:100] + "..."
            except:
                banner = "Banner alinamadi"
            print("[+] Port " + str(port) + " ACIK  -->  " + banner)
            acik_portlar.append(port)
        s.close()
    except:
        pass

print("------ Basit Port Tarayici ------")
hedef = input("Hedef IP adresini girin: ")

try:
    hedef_ip = socket.gethostbyname(hedef)
except:
    print("Hedef cozumlenemedi, program kapaniyor.")
    sys.exit()

print("Tarama baslatildi: " + hedef_ip)
print("Baslangic zamani: " + str(datetime.now()))
print("---------------------------------")

thread_listesi = []

for p in portlar:
    t = threading.Thread(target=port_tara, args=(hedef_ip, p))
    t.start()
    thread_listesi.append(t)

for t in thread_listesi:
    t.join()

print("---------------------------------")
print("Tarama bitti: " + str(datetime.now()))
print("Toplam acik port sayisi: " + str(len(acik_portlar)))
if len(acik_portlar) > 0:
    print("Acik portlar: " + str(acik_portlar))
else:
    print("Hicbir port acik bulunamadi.")
