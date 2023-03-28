def Zhu_Takaoka_algoritmasi(metin, desen):
    def hucre_olustur(desen):
        hucre = {}
        for i in range(len(desen) - 1):
            hucre[desen[i]] = len(desen) - i - 1
        return hucre

    def pozisyon_belirleme(bos_harf, eklem, kosul):
        for i in range(1, len(kosul) + 1)[::-1]:
            etiket = True
            for terim_index in range(len(eklem)):
                desen_index = i - len(eklem) - 1 + terim_index
                if desen_index < 0 or eklem[terim_index] == kosul[desen_index]:
                    pass
                else:
                    etiket = False
            desen_index = i - len(eklem) - 1
            if etiket and (desen_index <= 0 or kosul[desen_index - 1] != bos_harf):
                return len(kosul) - desen_index
        return len(kosul)

    def hucre_olustur_1(desen):
        hucre = {}
        text = ""
        for i in range(len(desen)):
            text = desen[i] + text
            text_eklem = text[1:]
            hucre[i] = pozisyon_belirleme(desen[len(text) - 1], text_eklem, desen)
        return hucre

    def ara(arama_metni, aranan_desen):
        hucre_olusturmaa = hucre_olustur_1(aranan_desen)
        hucre = hucre_olustur(aranan_desen)
        i = 0
        sayac = 0
        while i < len(arama_metni) - len(aranan_desen) + 1:
            j = len(aranan_desen)
            while j > 0 and aranan_desen[j - 1] == arama_metni[i + j - 1]:
                j -= 1
            if j > 0:
                cozum = hucre.get(arama_metni[i + j - 1], len(aranan_desen))
                degistirme = hucre_olusturmaa[len(aranan_desen) - j]
                if cozum > degistirme:
                    i += cozum
                else:
                    i += degistirme
            else:
                sayac += 1
                i += len(aranan_desen)
        return sayac

    return ara(metin, desen)

with open("alice_in_wonderland.txt", "r", encoding="utf-8") as dosya:
    alice_metni = dosya.read()

aranan_kelimeler = ["upon",  "sigh", "Dormouse", "jury-box", "swim"]

for kelime in aranan_kelimeler:
    sayac = Zhu_Takaoka_algoritmasi(alice_metni, kelime)
    print(f"{kelime}: {sayac} ")
