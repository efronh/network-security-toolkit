# Ağ Güvenliği Araç Seti

IT ve SOC operasyonları için geliştirilmiş temel Python ağ güvenliği araçları.

## Araçlar

### 1. Host Alive Checker
Ağdaki cihazların aktif olup olmadığını otomatik olarak kontrol eder.

**Neden gerekli:** Her cihazı tek tek manuel kontrol etmek hem yavaş hem de 
atlama riskine yol açar. Bu araç, threading kullanarak tüm IP aralığını 
aynı anda tarar — hızlı ve eksiksiz.

**Kullanım:**
```bash
python host_alive_checker.py
```

### 2. Port Tarayıcı
Hedef cihazdaki kritik portları tarar ve banner bilgisi almaya çalışır.

**Taranan portlar:**
| Port | Servis | Risk |
|------|--------|------|
| 21 | FTP | Şifresiz dosya transferi |
| 22 | SSH | Brute force hedefi |
| 23 | Telnet | Şifreleme yok — yüksek risk |
| 25 | SMTP | Mail relay kötüye kullanımı |
| 80 | HTTP | Şifresiz web trafiği |
| 443 | HTTPS | Şifreli web trafiği |
| 445 | SMB | WannaCry / ransomware hedefi |
| 3389 | RDP | Brute force hedefi |

**Neden gerekli:** Yanlışlıkla açık bırakılan veya kullanıcının izinsiz açtığı 
bir port log üretmeyebilir — ya da o log incelenene kadar saldırı gerçekleşmiş 
olabilir. Bu araç, açık portları saldırgandan önce tespit eder.

**Kullanım:**
```bash
python port_scanner.py
```

## Motivasyon

Ağ güvenliği temellerini pekiştirmek ve IT ekiplerinin altyapıyı nasıl 
izlediğini anlamak için geliştirildi — aktif cihaz tespiti ve güvenlik 
olayına dönüşmeden önce açık servislerin belirlenmesi.
