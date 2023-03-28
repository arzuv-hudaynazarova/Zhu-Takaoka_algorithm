# Zhu-Takaoka_algorithm
#Zhu-Takaoka algoritması

Bu kod, öncelikle 'alice_in_wonderland.txt' dosyasını okur. Daha sonra, 'upon', 'sigh', 'Dormouse', 'jury-box' ve 'swim' kelimeleri için birer arama yaparak kaç kez tekrar ettiklerini hesaplar ve ekrana yazdırır. re.findall fonksiyonu kullanarak, verilen kelimenin dosyada kaç kez tekrar ettiğini buluruz.


Zhu-Takaoka algoritması, bir metin içinde verilen bir deseni hızlı bir şekilde arayan bir arama algoritmasıdır. Bu algoritma, Boyer-Moore algoritmasına benzer bir şekilde, önceden hesaplanmış bir karakter atlama tablosu kullanarak arama işlemini hızlandırır.

Algoritma, önce aranan desenin son karakteriyle eşleşen karakterlerin konumunu arar. Eğer eşleşme olursa, desenin geri kalanını sondan başlayarak kontrol eder ve metin içinde tam bir eşleşme bulursa, desenin başlangıç konumunu döndürür.

Eğer bir eşleşme yoksa, son karaktere göre karakter atlama tablosunu kullanarak deseni metinde bir sonraki pozisyona atlama yapar. Bu sayede, birçok karşılaştırma işlemi yapmadan arama işlemini hızlandırır.

Zhu-Takaoka algoritması, özellikle kısa desenlerin aranması için çok hızlıdır ve Boyer-Moore algoritması ile karşılaştırıldığında daha az bellek kullanır. Ancak, uzun desenler için Boyer-Moore algoritması daha verimlidir.
