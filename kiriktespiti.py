import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('broken6.jpg', cv2.IMREAD_GRAYSCALE)

# Histogram eşitlemesi yaparak kontrastı artır
equalized_image = cv2.equalizeHist(image)

# Görüntüyü Gauss bulanıklaştırma ile yumuşat (gürültü azaltma)
blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)

# Kenar tespiti için Canny algoritmasını kullan
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

# Morfolojik işlemler (görüntüyü genişletme ve erozyon)
kernel = np.ones((5,5), np.uint8)
morph_image = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Hough dönüşümü ile doğrusal kırıkları tespit et
lines = cv2.HoughLinesP(morph_image, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

# Görüntüyü renkli hale getir (kare çizim için)
result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Tespit edilen doğrusal çizgileri ve kırıkları çizin
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Yeşil çizgiler

# Konturları bul
contours, _ = cv2.findContours(morph_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kırık kemiği tespit etmek için en büyük konturu seç
if contours:
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Kırık bölgede kare çiz

# Sonuçları görselleştirme
plt.figure(figsize=(12, 6))

# Orijinal Görüntü ve Eşitleme sonrası
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Röntgen Görüntüsü')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Eşitlemesi Uygulanmış Görüntü')
plt.axis('off')

# Kenar tespiti ve morfolojik işlem sonucu
plt.subplot(2, 2, 3)
plt.imshow(morph_image, cmap='gray')
plt.title('Morfolojik İşlem ve Kenar Tespiti')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(result_image)
plt.title('Kırık Kemik Tespiti ve Çizgi Çizimi')
plt.axis('off')

plt.tight_layout()
plt.show()
