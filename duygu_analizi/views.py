from django.shortcuts import render
import random

# Anasayfa görüntüleme fonksiyonu
def anasayfa(request):
    return render(request, 'duygu_analizi/anasayfa.html')

# Örnek bir duygu analizi fonksiyonu; kendi analiz fonksiyonunuzu buraya entegre edebilirsiniz
def duygu_analizi_fonksiyonu(metin):
    # Burada metnin analiz edilip "pozitif", "negatif" veya "nötr" olarak sınıflandırıldığını varsayıyoruz
    if any(word in metin.lower() for word in ["mutlu", "harika", "iyi", "güzel"]):
        return "pozitif"
    elif any(word in metin.lower() for word in ["üzgün", "kötü", "berbat", "sinirli"]):
        return "negatif"
    else:
        return "notr"

# Analiz fonksiyonu
def analiz(request):
    sonuc = ""
    if request.method == "POST":
        metin = request.POST.get("metin")
        
        # Duygu analiz fonksiyonunu çalıştırarak duygu durumu elde ediyoruz
        duygu_durumu = duygu_analizi_fonksiyonu(metin)

        # Her bir duygu durumu için rastgele mesajlar
        pozitif_mesajlar = [
            "Harika bir enerji hissediyorum!",
            "Bugün çok pozitif bir ruh halindesiniz!",
            "Mutlu günler diliyorum!",
            "İçinizdeki mutluluk dışarıya yansıyor!",
        ]
        negatif_mesajlar = [
            "Üzgün olduğunuzu hissediyorum, umarım daha iyi hissedersiniz.",
            "Bugün zor bir gün olabilir, kendinize zaman ayırın.",
            "Her şey yoluna girecek, güçlü kalın!",
            "Olumsuzluklar geçicidir, unutmayın.",
        ]
        notr_mesajlar = [
            "Her şey normal görünüyor.",
            "Duygu durumunuz dengeli görünüyor.",
            "Nötr bir ruh halindesiniz.",
            "Ruh haliniz oldukça sabit.",
        ]

        # Duygu durumuna göre rastgele bir mesaj seçiyoruz
        if duygu_durumu == "pozitif":
            sonuc = random.choice(pozitif_mesajlar)
        elif duygu_durumu == "negatif":
            sonuc = random.choice(negatif_mesajlar)
        else:
            sonuc = random.choice(notr_mesajlar)
    
    return render(request, 'duygu_analizi/anasayfa.html', {'sonuc': sonuc})
