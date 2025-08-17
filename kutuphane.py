from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class Kitap(ABC):
    def __init__(self, baslik, yazar, barkod, tur, tema):
        self.baslik = baslik
        self.yazar = yazar
        self.barkod = barkod.strip()
        self.tur = tur
        self.tema = tema
        self.ödünç_alındı_mı = False

    @abstractmethod
    def göster(self):
        pass


class Ekitap(Kitap):
    def __init__(self, baslik, yazar, barkod, tur, tema, dosya_boyutu):
        super().__init__(baslik, yazar, barkod, tur, tema)
        try:
            self.dosya_boyutu = float(dosya_boyutu)
        except ValueError:
            print("Hatalı dosya boyutu. Lütfen sayısal bir değer girin.")
            self.dosya_boyutu = 0

    def göster(self):
        if self.ödünç_alındı_mı:
            durum = "Ödünçte"
        else:
            durum = "Müsait"
        return f"Başlık: {self.baslik}, Yazar: {self.yazar}, Barkod: {self.barkod}, Tür: {self.tur}, Tema: {self.tema}, Dosya Boyutu: {self.dosya_boyutu} MB, Durum: {durum}"


class BasılıKitap(Kitap):
    def __init__(self, baslik, yazar, barkod, tur, tema, sayfa_sayısı):
        super().__init__(baslik, yazar, barkod, tur, tema)
        try:
            self.sayfa_sayısı = int(sayfa_sayısı)
        except ValueError:
            print("Hatalı sayfa sayısı. Lütfen tam sayı girin.")
            self.sayfa_sayısı = 0

    def göster(self):
        if self.ödünç_alındı_mı:
            durum = "Ödünçte"
        else:
            durum = "Müsait"
        return f"Başlık: {self.baslik}, Yazar: {self.yazar}, Barkod: {self.barkod}, Tür: {self.tur}, Tema: {self.tema}, Sayfa Sayısı: {self.sayfa_sayısı} sayfa, Durum: {durum}"


class Kütüphane:
    def __init__(self):
        self.kitaplar = []
        self.ceza_oranı = 1.0

    def kitap_ödünç_al(self, barkod):
        for kitap in self.kitaplar:
            if kitap.barkod == barkod:
                if kitap.ödünç_alındı_mı:
                    print(f"{kitap.baslik} zaten ödünç alınmış.")
                else:
                    alinan_tarih = self.tarih_girisi("Kitabın alındığı tarihi girin (YYYY-MM-DD): ")
                    kitap.ödünç_alındı_mı = True
                    kitap.alinan_tarih = alinan_tarih
                    print(f"{kitap.baslik} ödünç alındı. Alındığı tarih: {kitap.alinan_tarih.strftime('%Y-%m-%d')}")
                return
        print("Böyle bir kitap bulunamadı.")

    def kitap_teslim_et(self, barkod):
        for kitap in self.kitaplar:
            if kitap.barkod == barkod:
                if not kitap.ödünç_alındı_mı:
                    print(f"{kitap.baslik} zaten kütüphanede.")
                else:
                    teslim_edilen_tarih = self.tarih_girisi("Kitabın teslim edildiği tarihi girin (YYYY-MM-DD): ")
                    kitap.ödünç_alındı_mı = False
                    gecikme = teslim_edilen_tarih - kitap.alinan_tarih
                    gecikme_gün = max(0, (gecikme - timedelta(days=14)).days)
                    ceza = gecikme_gün * self.ceza_oranı
                    print(f"{kitap.baslik} teslim edildi. Gecikme: {gecikme_gün} gün. Ceza: {ceza:.2f} TL.")
                return
        print("Böyle bir kitap bulunamadı.")

    def kitap_göster(self):
        if not self.kitaplar:
            print("Kütüphanede kitap yok")
            return
        for kitap in self.kitaplar:
            print(kitap.göster())

    def tarih_girisi(self, prompt):
        while True:
            try:
                tarih_str = input(prompt)
                return datetime.strptime(tarih_str, "%Y-%m-%d")
            except ValueError:
                print("Hatalı tarih formatı. Lütfen YYYY-MM-DD formatında girin.")

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitap_cıkar(self, barkod):
        barkod = barkod.strip()
        for kitap in self.kitaplar:
            if kitap.barkod == barkod:
                self.kitaplar.remove(kitap)
                print(f"{kitap.baslik} çıkarıldı.")
                return
        print("Böyle kitap bulunamadı.")


def görevli_girişi():
    şifre = input("Görevli şifresini girin: ")
    if şifre == "görevli123":
        return True
    else:
        print("Yanlış şifre.")
        return False


def öğrenci_girişi():
    return True


def görevli_menu():
    print("\n1) Kitap ekle\n2) Kitap çıkar\n3) Kitapları göster\n4) Çıkış")
    islem = input("Yapmak istediğiniz işlemi seçin: ")
    return islem


def öğrenci_menu():
    print("\n1) Ödünç al\n2) Teslim et\n3) Kitapları göster\n4) Çıkış")
    islem = input("Yapmak istediğiniz işlemi seçin: ")
    return islem


def görevli_ve_öğrenci_girişi():
    while True:
        print("\n1) Görevli Girişi\n2) Öğrenci Girişi\n3) Çıkış")
        giriş = input("Giriş yapmak istediğiniz tipi seçin: ")
        if giriş == "1":
            if görevli_girişi():
                return "görevli"
        elif giriş == "2":
            return "öğrenci"
        elif giriş == "3":
            return None
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")


kütüphanem = Kütüphane()

while True:
    kullanıcı_tipi = görevli_ve_öğrenci_girişi()

    if kullanıcı_tipi is None:
        print("Çıkılıyor...")
        break

    while kullanıcı_tipi == "görevli":
        islem = görevli_menu()

        if islem == "4":
            break

        elif islem == "1":
            baslik = input("Kitap başlığı: ")
            yazar = input("Kitap yazarı: ")
            barkod = input("Kitap barkodu: ")

            print("\nKitap Türleri:")
            print("1) Anı\n2) Roman\n3) Hikaye\n4) Gezi\n5) Şiir\n6) Biyografi\n7) Dini\n8) Bilgi")
            tur_secim = input("Kitap türünü seçin (1-8): ")
            turler = {
                "1": "Anı",
                "2": "Roman",
                "3": "Hikaye",
                "4": "Gezi",
                "5": "Şiir",
                "6": "Biyografi",
                "7": "Dini",
                "8": "Bilgi"
            }
            tur = turler.get(tur_secim)
            while tur is None:
                print("Geçersiz tür seçimi.")
                tur_secim = input("Kitap türünü seçin (1-8): ")
                tur = turler.get(tur_secim)

            print("\nKitap Temaları:")
            print("1) Dram\n2) Gizem\n3) Polisiye\n4) Romantik\n5) Fantastik\n6) Macera")
            tema_secim = input("Kitap temasını seçin (1-6): ")
            temalar = {
                "1": "Dram",
                "2": "Gizem",
                "3": "Polisiye",
                "4": "Romantik",
                "5": "Fantastik",
                "6": "Macera"
            }
            tema = temalar.get(tema_secim)
            while tema is None:
                print("Geçersiz tema seçimi.")
                tema_secim = input("Kitap temasını seçin (1-6): ")
                tema = temalar.get(tema_secim)

            dosya_boyutu = input("E-Kitap dosya boyutu (MB, basılı kitapsa boş geçin): ")
            if dosya_boyutu.strip():
                kitap = Ekitap(baslik, yazar, barkod, tur, tema, dosya_boyutu)
            else:
                sayfa_sayısı = input("Basılı kitap sayfa sayısı: ")
                kitap = BasılıKitap(baslik, yazar, barkod, tur, tema, sayfa_sayısı)
            kütüphanem.kitap_ekle(kitap)
            print(f"{kitap.baslik} kütüphaneye eklendi.")

        elif islem == "2":
            if not kütüphanem.kitaplar:
                print("Kütüphanede kitap yok, kitap çıkaramazsınız.")
            else:
                barkod = input("Çıkarmak istediğiniz kitabın barkodu: ")
                kütüphanem.kitap_cıkar(barkod)

        elif islem == "3":
            kütüphanem.kitap_göster()

        else:
            print("Geçersiz işlem. Lütfen 1 ile 4 arasında bir seçenek girin.")

    while kullanıcı_tipi == "öğrenci":
        islem = öğrenci_menu()

        if islem == "4":
            break

        elif islem == "1":
            if not kütüphanem.kitaplar:
                print("Kütüphanede kitap yok, ödünç alma işlemi yapılamaz.")
            else:
                barkod = input("Ödünç almak istediğiniz kitabın barkodu: ")
                kütüphanem.kitap_ödünç_al(barkod)

        elif islem == "2":
            if not kütüphanem.kitaplar:
                print("Kütüphanede kitap yok, teslim etme işlemi yapılamaz.")
            else:
                barkod = input("Teslim etmek istediğiniz kitabın barkodu: ")
                kütüphanem.kitap_teslim_et(barkod)

        elif islem == "3":
            kütüphanem.kitap_göster()

        else:
            print("Geçersiz işlem. Lütfen 1 ile 4 arasında bir seçenek girin.")
