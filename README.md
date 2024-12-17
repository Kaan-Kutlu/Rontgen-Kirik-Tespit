# Röntgen Görüntülerinde Kemik Kırığı Tespiti

Bu proje, röntgen görüntülerini analiz ederek kemik kırıklarını veya çatlaklarını otomatik olarak tespit etmeyi amaçlar. Tıbbi tanı süreçlerini desteklemek üzere görüntü işleme teknikleri kullanılmış ve kırık bölgelerin kare içinde gösterilmesi sağlanmıştır.

<img src=Figure_1.png width=50%>
<img src=Figure_2.png width=50%>

## Özellikler
- Histogram eşitlemesi ile kontrast iyileştirme.
- Gauss bulanıklaştırma ile gürültü azaltma.
- Canny algoritması ile kenar tespiti.
- Morfolojik işlemler ve kontur analizi.
- Tespit edilen bölgeleri kare içinde görüntüleme.

## Kullanılan Teknolojiler ve Kütüphaneler
- **Python**: Ana programlama dili.
- **OpenCV**: Görüntü işleme için.
- **NumPy**: Veri manipülasyonu ve hesaplama için.
- **Matplotlib**: Görselleştirme için.

## Gereksinimler
Projeyi çalıştırabilmek için şu kütüphanelerin kurulu olması gerekmektedir:

```bash
pip install opencv-python numpy matplotlib
```

## Nasıl Çalıştırılır?
1. Proje dosyasını bilgisayarınıza klonlayın veya indirin.
   ```bash
   git clone https://github.com/Kaan-Kutlu/Rontgen-Kirik-Tespit.git
   ```
2. Gerekli Python kütüphanelerini yükleyin.
3. Röntgen görüntünü proje dizinine ekleyin ve `broken1.jpg` şeklinde isimlendirin.
4. Ana Python dosyasını çalıştırın:
   ```bash
   python main.py
   ```

## Dosya Yapısı
```
proje-adi/
├── main.py           # Ana Python kodu
├── broken1.jpg       # Test için kullanılan röntgen görüntüsü
├── README.md         # Proje dokümantasyonu
```

## Katkı Sağlama
Katkı sağlamak isterseniz, lütfen bir çekme isteği (pull request) oluşturun veya bir konu (issue) açın.

