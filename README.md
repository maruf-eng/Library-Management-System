# 📚 Kütüphane Uygulaması — README

> Kaynak dosya: :contentReference[oaicite:0]{index=0}

## 🎯 Amaç
✅ Konsol tabanlı basit bir kütüphane otomasyonu  
✅ **Görevli** ve **Öğrenci** rollerine göre menüler  
✅ Kitap ekleme–çıkarma, ödünç alma–teslim etme akışları  
✅ 14 günlük iade süresi ve gecikme cezası hesabı

---

## 🧩 Özellikler (Özet)
📌 **Nesne Yönelimli Tasarım:** `Kitap` (soyut sınıf), `Ekitap`, `BasılıKitap`, `Kütüphane`  
📌 **Rol Bazlı Giriş:** Görevli (şifre: `görevli123`) • Öğrenci (şifresiz)  
📌 **Kitap Yönetimi:** Ekle • Çıkar • Listele  
📌 **Ödünç İşlemleri:** 14 gün kuralı • Gecikme cezası (`ceza_oranı=1.0` TL/gün)  
📌 **Girdi Doğrulama:** Tarih (`YYYY-MM-DD`) • Sayısal alanlar (dosya boyutu/sayfa sayısı)  
📌 **Konsol Uyumlu:** Ek kütüphane gerektirmez

---

## 🔧 Kurulum
🔹 Gereksinimler:  
- Python **3.10** ve üzeri (önerilir)  
- Harici paket yok

🔹 Çalıştırma:
```bash
python kutuphane.py
