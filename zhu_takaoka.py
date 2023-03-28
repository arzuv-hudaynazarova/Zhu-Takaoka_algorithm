import re

def zhu_takaoka(text, desen):
    m = len(desen)
    n = len(text)
    islem = [m] * 256

    for i in range(m - 1):
        islem[ord(desen[i])] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == desen[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(islem[ord(text[i])], m - j)

    return -1

with open('alice_in_wonderland.txt', 'r') as f:
    text = f.read()

aranan_kelimler = ['upon', 'sigh', 'Dormouse', 'jury-box', 'swim']

for kelime in aranan_kelimler:
    sayi = len(re.findall(kelime, text))
    print(kelime, sayi)
