# 9. Sınıf Matematik - Mantık ve Niceleyiciler Oyunları

Bu proje, 9. sınıf matematik müfredatındaki mantık ve niceleyiciler konusunu eğlenceli ve interaktif oyunlarla öğretmek için tasarlanmıştır. Flask web framework'ü kullanılarak geliştirilmiş ve Railway platformunda deploy edilmeye hazırdır.

## 🚀 Deployment (Railway)

Bu proje Railway platformunda kolayca deploy edilebilir:

1. Railway hesabınıza giriş yapın
2. "New Project" → "Deploy from GitHub repo" seçin
3. Bu repository'yi seçin
4. Railway otomatik olarak `app.py`'yi algılayacak ve deploy edecektir

### Gerekli Dosyalar:
- `app.py` - Flask uygulaması
- `requirements.txt` - Python bağımlılıkları
- `Procfile` - Deployment komutu
- `railway.json` - Railway konfigürasyonu

## 🎮 Oyunlar

### 1. 🎯 Niceleyici Doğruluk Oyunu (game1.html)
- **Konu**: Evrensel (∀) ve Varoluşsal (∃) niceleyiciler
- **Amaç**: Verilen önermelerin doğruluk değerlerini belirleme
- **Özellikler**:
  - 8 farklı soru
  - 🧩 **Bulmaca Modu**: Rastgele bulmacalar
  - 📅 **Günlük Bulmaca**: Her gün yeni meydan okuma
  - 🏆 **Lider Tablosu**: Kullanıcı puanları
  - ⏱️ **Zamanlı Bulmacalar**: Süre sınırlı oyun modu
  - Doğruluk tabloları ve açıklamalar
  - Puan sistemi ve ilerleme takibi
  - Detaylı geri bildirim

### 2. 🧩 Mantık Bağlaçları Bulmacası (game2.html)
- **Konu**: Mantık bağlaçları (∧, ∨, →, ↔)
- **Amaç**: Doğru mantık bağlacını seçerek önermeleri tamamlama
- **Özellikler**:
  - Interaktif doğruluk tabloları
  - 🧩 **Bulmaca Modu**: Çeşitli zorluk seviyeleri
  - 📅 **Günlük Bulmaca**: Günlük meydan okumalar
  - 🏆 **Lider Tablosu**: Sıralama sistemi
  - Gerçek hayat örnekleri
  - Görsel geri bildirim
  - Bağlaç açıklamaları

### 3. 🏗️ Önerme Kurma Yarışması (game3.html)
- **Konu**: Niceleyiciler ve mantık bağlaçlarını birleştirme
- **Amaç**: Verilen koşullara uygun mantıksal önermeleri oluşturma
- **Özellikler**:
  - Sürükle-bırak arayüzü
  - 🧩 **Bulmaca Modu**: Karmaşık önerme kurma
  - 📅 **Günlük Bulmaca**: Günlük özel görevler
  - 🏆 **Lider Tablosu**: İlerleme takibi
  - 5 farklı zorluk seviyesi
  - İpucu sistemi
  - Adım adım öğrenme

### 4. ⚡ Mantık Devresi Simülatörü (game4.html)
- **Konu**: Mantık kapıları ve görselleştirme
- **Amaç**: Mantıksal işlemleri devre şemaları ile anlama
- **Özellikler**:
  - Interaktif mantık kapıları (AND, OR, NOT, XOR, NAND, NOR)
  - 🧩 **Bulmaca Modu**: Devre tasarım meydan okumaları
  - 🏆 **Lider Tablosu**: En iyi devre tasarımcıları
  - Gerçek zamanlı doğruluk tablosu
  - Görsel devre çizimi
  - Otomatik test modu
  - Meydan okuma görevleri

## 🚀 Kullanım

### Yerel Geliştirme:
1. Python 3.7+ yüklü olduğundan emin olun
2. Gerekli paketleri yükleyin: `pip install -r requirements.txt`
3. Flask uygulamasını çalıştırın: `python app.py`
4. Tarayıcınızda `http://localhost:5000` adresine gidin

### Statik Kullanım:
1. `templates/index.html` dosyasını bir web tarayıcısında açın
2. Ana sayfadan istediğiniz oyunu seçin
3. Her oyunun kendi talimatları ve kontrolleri vardır

## 🆕 Yeni Özellikler

### Backend API Özellikleri:
- **Kullanıcı İlerleme Takibi**: Her oyundaki ilerleme kaydedilir
- **Bulmaca Sistemi**: Dinamik bulmaca oluşturma ve yönetimi
- **Günlük Bulmacalar**: Her gün yeni meydan okumalar
- **Lider Tablosu**: Kullanıcı sıralaması ve puanlama sistemi
- **RESTful API**: Tüm oyun verileri API üzerinden yönetilir

### Frontend Geliştirmeleri:
- **Çoklu Oyun Modları**: Normal, Bulmaca ve Günlük mod seçenekleri
- **Gerçek Zamanlı Puanlama**: Anlık puan güncellemeleri
- **İlerleme Kaydetme**: Kullanıcı verilerinin otomatik kaydedilmesi
- **Responsive Tasarım**: Tüm cihazlarda mükemmel görünüm

## 📚 Öğrenme Hedefleri

### Niceleyiciler
- **∀ (Evrensel)**: "Her", "tüm" anlamında
- **∃ (Varoluşsal)**: "Var olan", "en az bir" anlamında
- **∃! (Tekil varoluşsal)**: "Tam olarak bir" anlamında

### Mantık Bağlaçları
- **∧ (Ve)**: Her iki önerme de doğru olmalı
- **∨ (Veya)**: En az bir önerme doğru olmalı
- **→ (İse)**: Koşullu önerme
- **↔ (Ancak ve ancak)**: İki yönlü koşul
- **¬ (Değil)**: Olumsuzlama

## 🎯 Eğitim Faydaları

1. **Görsel Öğrenme**: Mantıksal kavramları görselleştirme
2. **Interaktif Deneyim**: Aktif katılım ve deneyimleme
3. **Anında Geri Bildirim**: Hataları hemen düzeltme
4. **Kademeli Öğrenme**: Basit'ten karmaşığa doğru ilerleme
5. **Pratik Uygulama**: Teorik bilgiyi pratiğe dökme

## 🛠️ Teknik Özellikler

- **HTML5**: Modern web standartları
- **CSS3**: Responsive tasarım ve animasyonlar
- **JavaScript**: Interaktif oyun mekaniği
- **Canvas API**: Devre çizimi için
- **Responsive Design**: Mobil uyumlu

## 📱 Uyumluluk

- ✅ Chrome, Firefox, Safari, Edge
- ✅ Masaüstü ve mobil cihazlar
- ✅ Tablet uyumlu
- ✅ Çevrimdışı çalışma

## 🎨 Tasarım Özellikleri

- Modern ve temiz arayüz
- Renk kodlu geri bildirimler
- Animasyonlu geçişler
- Kullanıcı dostu kontroller
- Erişilebilir tasarım

## 📈 Değerlendirme Sistemi

Her oyun kendi puan sistemine sahiptir:
- Doğru cevaplar için puan kazanma
- Yanlış cevaplar için açıklama
- İlerleme takibi
- Başarı yüzdesi hesaplama

## 🔧 Geliştirme Notları

Proje tamamen vanilla JavaScript ile geliştirilmiştir, herhangi bir external kütüphane gerektirmez. Tüm oyunlar tek sayfa uygulamaları (SPA) olarak tasarlanmıştır.

---

**Geliştirici**: AI Assistant  
**Tarih**: 2024  
**Sürüm**: 1.0  
**Lisans**: Eğitim amaçlı kullanım
