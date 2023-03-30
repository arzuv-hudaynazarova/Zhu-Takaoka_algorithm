import re  # re modülünü içe aktarma (düzenli ifadelerle çalışmak için)

# Zhu-Takaoka algoritmasını kullanarak, verilen metin dosyasında bir kelimenin ilk konumunu bulma
def zhu_takaoka(metin, kelime):
    m = len(kelime)
    n = len(metin)
    islem = [m] * 256

    # Zhu-Takaoka algoritması için ön işleme adımı
    for i in range(m - 1):
        islem[ord(kelime[i])] = m - i - 1

    # Zhu-Takaoka algoritması ile kelimeyi metin dosyasında arama
    i = m - 1
    while i < n:
        j = m - 1
        while metin[i] == kelime[j]:
            if j == 0:
                return i  # Kelime bulunduğunda başlangıç pozisyonunu döndür
            i -= 1
            j -= 1
        i += max(islem[ord(metin[i])], m - j)

    return -1  # Kelime bulunamazsa -1 döndür

# 'alice_in_wonderland.txt' dosyasını okuma ve içeriği 'text' değişkenine atama
with open('alice_in_wonderland.txt', 'r') as f:
    text = f.read()

# Aranacak kelimelerin listesini oluşturma
aranan_kelimler = ['upon', 'sigh', 'Dormouse', 'jury-box', 'swim']

# Aranan kelimelerin metin dosyasında kaç kez geçtiğini bulma ve ekrana yazdırma
for kelime in aranan_kelimler:
    sayi = len(re.findall(kelime, text))  # re.findall() kullanarak kelime sayısını bulma
    print(kelime, sayi)

    
    
