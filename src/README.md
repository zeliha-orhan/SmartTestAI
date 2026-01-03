# Frontend Web Interface

AI kod analiz araçlarını (Snyk Code vs DeepSource) karşılaştırmak için basit ve temiz web arayüzü.

## Dosyalar

- `index.html` - Tablo ve görsel öğeler içeren ana karşılaştırma sayfası
- `styles.css` - Responsive tasarıma sahip temiz, minimal stil dosyası

## Kullanım

### Sayfayı Açma

**Seçenek 1: Yerel Sunucu (Önerilen)**
```bash
# src klasörüne gidin
cd src

# Python 3 kullanarak HTTP sunucusu başlatın
python -m http.server 8000

# Ardından tarayıcınızda şu adrese gidin:
# http://localhost:8000
```

**Seçenek 2: Doğrudan Dosya Açma**
- `index.html` dosyasına çift tıklayarak varsayılan tarayıcınızda açın
- Veya sağ tıklayıp "Birlikte aç" → tercih ettiğiniz tarayıcıyı seçin
- Not: Bu yöntemde bazı özellikler çalışmayabilir (CORS kısıtlamaları nedeniyle)

## Özellikler

- **Karşılaştırma Tablosu**: Snyk Code ve DeepSource'un yan yana karşılaştırması
- **Görsel Öğeler**: 
  - Progress bar'lar sayısal metrikler için (Kod Kapsamı, Precision, Recall, F1 Score, vb.)
  - Sorun sayıları breakdown gösterimi (Critical, High, Medium, Low)
  - Metrik değerleri ve görsel gösterimler
- **Özet Kartları**: Her aracın durumu ve özelliklerinin hızlı özeti
- **Metrik Açıklamaları**: Precision, Recall, F1 Score ve False Positive Rate hakkında bilgilendirici açıklamalar
- **Responsive Tasarım**: Masaüstü, tablet ve mobil cihazlarda çalışır

## Karşılaştırma Kriterleri

1. **Toplam Sorun Sayısı** - Tespit edilen kod sorunları (Critical, High, Medium, Low breakdown ile)
2. **Tarama Süresi** - Kod analizinin tamamlanma süresi (saniye)
3. **Kod Kapsamı** - Analiz edilen kod yüzdesi
4. **Precision (Kesinlik)** - Doğru pozitif / (Doğru pozitif + Yanlış pozitif)
5. **Recall (Duyarlılık)** - Doğru pozitif / (Doğru pozitif + Yanlış negatif)
6. **F1 Score** - Precision ve Recall'un harmonik ortalaması
7. **Yanlış Pozitif Oranı** - Yanlış pozitif / (Yanlış pozitif + Doğru negatif)
8. **Bellek Kullanımı** - Tarama sırasında kullanılan bellek (MB)

## Veri

Karşılaştırma verileri HTML dosyasına doğrudan gömülmüş statik/mock verilerdir. Şu anda gerçek zamanlı veri entegrasyonu yoktur. Backend veya API çağrısı gerekmez.

## Gelecek Geliştirmeler

- Gerçek zamanlı veri entegrasyonu (JSON dosyalarından veri okuma)
- Backend API'den canlı veri çekme
- Dinamik grafikler ve görselleştirmeler
- Tarihsel veri karşılaştırması

## Notlar

- Site şu anda statik verilerle çalışmaktadır
- Gerçek tarama sonuçları için backend API'ye entegrasyon yapılabilir
- Tüm metrikler `results/` klasöründeki JSON dosyalarından alınabilir
