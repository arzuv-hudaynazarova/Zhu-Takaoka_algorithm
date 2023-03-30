
# Zhu-Takaoka algoritması kullanarak, verilen metin dosyasında bir kelimenin ilk konumunu bulan fonksiyonu oluşturdum
def zhu_takaoka_arama(metin, kelime):
    kelime_uzunluk = len(kelime)
    metin_uzunluk = len(metin)
    islem = [kelime_uzunluk] * 256

    # Zhu-Takaoka algoritması için ön işleme adımı oluşturdum
    for i in range(kelime_uzunluk - 1):
        islem[ord(kelime[i])] = kelime_uzunluk - i - 1

    # Zhu-Takaoka algoritması ile kelimeyi  metin dosyasında aradım
    i = kelime_uzunluk - 1
    while i < metin_uzunluk:
        j = kelime_uzunluk - 1
        while metin[i] == kelime[j]:
            if j == 0:
                return i  # Kelime bulunduğunda başlangıç pozisyonunu döndüren kodu yazdım
            i -= 1
            j -= 1
        i += max(islem[ord(metin[i])], kelime_uzunluk - j)

    return -1  # Kelime bulunamazsa -1 döndüren kod parçası

# Zhu-Takaoka algoritması kullanarak belirtilen kelimenin metin dosyasında kaç kez geçtiğini hesaplayan fonksiyonu gösterdim 
def kelime_sayisi(metin, kelime):
    index = 0
    sayac = 0
    while index != -1:
        index = zhu_takaoka_arama(metin, kelime)
        if index != -1:
            sayac += 1
            metin = metin[index + 1:]
    return sayac

# 'alice_in_wonderland.txt' dosyasını okuma ve içeriğini 'text' değişkenine atadım
with open('alice_in_wonderland.txt', 'r') as f:
    text = f.read()

# Aranacak kelimelerin listesini oluşturdum
aranan_kelimeler = ['upon', 'sigh', 'Dormouse', 'jury-box', 'swim']

# Aranan kelimelerin metin dosyasında kaç kez geçtiğini bulan ve ekrana yazdıran kodu oluşturdum
print("Aşağıdaki kelimelerin 'Alice in Wonderland' metnin dosyasındaki kaç kez geçtiğini göstermektedir: \n")
for kelime in aranan_kelimeler:
    sayi = kelime_sayisi(text, kelime)
    print(f"{kelime}: {sayi} kez geçiyor.")

print("\nNot: Bu sonuçlar  Zhu-Takaoka algoritması kullanılarak elde edilmiştir.")


