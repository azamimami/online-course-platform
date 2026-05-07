
# ===================== ONLINE KURS PLATFORMU =====================

kurs_id_counter = 1
ogrenci_id_counter = 1
egitmen_id_counter = 1


# ================= SAFE INPUT =================
def safe_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Hatalı giriş! Sadece sayı gir.")


# ================= EGITMEN =================
class Egitmen:
    def __init__(self, ad, soyad, uzmanlik):
        global egitmen_id_counter

        self.egitmen_id = egitmen_id_counter
        egitmen_id_counter += 1

        self.ad = ad
        self.soyad = soyad
        self.uzmanlik = uzmanlik

    def __str__(self):
        return f"[{self.egitmen_id}] {self.ad} {self.soyad} | {self.uzmanlik}"


# ================= OGRENCI =================
class Ogrenci:
    def __init__(self, ad, soyad, email):
        global ogrenci_id_counter

        self.ogrenci_id = ogrenci_id_counter
        ogrenci_id_counter += 1

        self.ad = ad
        self.soyad = soyad
        self.email = email

    def __str__(self):
        return f"[{self.ogrenci_id}] {self.ad} {self.soyad} | {self.email}"


# ================= KURS =================
class Kurs:
    def __init__(self, kurs_adi, egitmen, kontenjan):
        global kurs_id_counter

        self.kurs_id = kurs_id_counter
        kurs_id_counter += 1

        self.kurs_adi = kurs_adi
        self.egitmen = egitmen
        self.kontenjan = kontenjan
        self.ogrenciler = []

    def ogrenci_kaydet(self, ogrenci):
        if len(self.ogrenciler) >= self.kontenjan:
            return "Kontenjan dolu"

        if ogrenci in self.ogrenciler:
            return "Öğrenci zaten kayıtlı"

        self.ogrenciler.append(ogrenci)
        return "Öğrenci kaydedildi"

    def __str__(self):
        ogr = ", ".join([o.ad for o in self.ogrenciler]) if self.ogrenciler else "Yok"

        return (
            f"[{self.kurs_id}] {self.kurs_adi} | "
            f"Eğitmen: {self.egitmen.ad} {self.egitmen.soyad} | "
            f"Kayıtlı: {len(self.ogrenciler)} | "
            f"Öğrenciler: {ogr}"
        )


# ================= SISTEM =================
class Sistem:
    def __init__(self):
        self.kurslar = []
        self.ogrenciler = []
        self.egitmenler = []

    # EKLE
    def kurs_ekle(self, k):
        self.kurslar.append(k)

    def ogrenci_ekle(self, o):
        self.ogrenciler.append(o)

    def egitmen_ekle(self, e):
        self.egitmenler.append(e)

    # BUL
    def kurs_bul(self, id):
        return next((k for k in self.kurslar if k.kurs_id == id), None)

    def ogrenci_bul(self, id):
        return next((o for o in self.ogrenciler if o.ogrenci_id == id), None)

    def egitmen_bul(self, id):
        return next((e for e in self.egitmenler if e.egitmen_id == id), None)

    # SIL (FIXED)
    def egitmen_sil(self, eid):
        for e in self.egitmenler:
            if e.egitmen_id == eid:
                self.egitmenler.remove(e)
                return True
        return False

    def ogrenci_sil(self, oid):
        for o in self.ogrenciler:
            if o.ogrenci_id == oid:
                self.ogrenciler.remove(o)
                return True
        return False

    def kurs_sil(self, kid):
        for k in self.kurslar:
            if k.kurs_id == kid:
                self.kurslar.remove(k)
                return True
        return False


# ================= MENU =================
def menu():
    s = Sistem()

    while True:
        print("\n===== ONLINE KURS PLATFORMU =====")
        print("1- Eğitmen Ekle")
        print("2- Eğitmen Listele")
        print("3- Öğrenci Ekle")
        print("4- Öğrenci Listele")
        print("5- Kurs Ekle")
        print("6- Kurs Listele")
        print("7- Kursa Öğrenci Kaydet")
        print("8- Öğrenci Kurslarını Göster")
        print("9- Eğitmen Sil")
        print("10- Öğrenci Sil")
        print("11- Kurs Sil")
        print("0- Çıkış")

        secim = input("Seçim: ")

        # 1
        if secim == "1":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            uzm = input("Uzmanlık: ")
            s.egitmen_ekle(Egitmen(ad, soyad, uzm))

        # 2
        elif secim == "2":
            if not s.egitmenler:
                print("Yok")
            else:
                for e in s.egitmenler:
                    print(e)

        # 3
        elif secim == "3":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            email = input("Email: ")
            s.ogrenci_ekle(Ogrenci(ad, soyad, email))

        # 4
        elif secim == "4":
            if not s.ogrenciler:
                print("Yok")
            else:
                for o in s.ogrenciler:
                    print(o)

        # 5
        elif secim == "5":
            if not s.egitmenler:
                print("Önce eğitmen ekle")
                continue

            for e in s.egitmenler:
                print(e)

            eid = safe_int("Eğitmen ID: ")
            eg = s.egitmen_bul(eid)

            if not eg:
                print("Geçersiz ID")
                continue

            ad = input("Kurs adı: ")
            kont = safe_int("Kontenjan: ")

            s.kurs_ekle(Kurs(ad, eg, kont))

        # 6
        elif secim == "6":
            if not s.kurslar:
                print("Yok")
            else:
                for k in s.kurslar:
                    print(k)

        # 7
        elif secim == "7":
            for o in s.ogrenciler:
                print(o)

            oid = safe_int("Öğrenci ID: ")
            ogr = s.ogrenci_bul(oid)

            if not ogr:
                print("Hata")
                continue

            for k in s.kurslar:
                print(k)

            kid = safe_int("Kurs ID: ")
            kurs = s.kurs_bul(kid)

            if not kurs:
                print("Hata")
                continue

            print(kurs.ogrenci_kaydet(ogr))

        # 8
        elif secim == "8":
            for o in s.ogrenciler:
                print(o)

            oid = safe_int("Öğrenci ID: ")
            ogr = s.ogrenci_bul(oid)

            if not ogr:
                print("Hata")
                continue

            found = False
            for k in s.kurslar:
                if ogr in k.ogrenciler:
                    print(k.kurs_adi)
                    found = True

            if not found:
                print("Kurs yok")

        # 9 SIL EGITMEN
        elif secim == "9":
            for e in s.egitmenler:
                print(e)

            eid = safe_int("Silinecek Eğitmen ID: ")
            if s.egitmen_sil(eid):
                print("Silindi")
            else:
                print("Bulunamadı")

        # 10 SIL OGRENCI
        elif secim == "10":
            for o in s.ogrenciler:
                print(o)

            oid = safe_int("Silinecek Öğrenci ID: ")
            if s.ogrenci_sil(oid):
                print("Silindi")
            else:
                print("Bulunamadı")

        # 11 SIL KURS
        elif secim == "11":
            for k in s.kurslar:
                print(k)

            kid = safe_int("Silinecek Kurs ID: ")
            if s.kurs_sil(kid):
                print("Silindi")
            else:
                print("Bulunamadı")

        elif secim == "0":
            break

        else:
            print("Hatalı seçim")


menu()