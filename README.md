# Data Science SQL Project 5

### Proje Kurulumu
Projeyi öncelikle forklayın ve clone edin.
Proje sayımız ilerledikçe proje yönetimimizi kolaylaştırmak adına projelerimizi belli klasör kalıplarında saklamak işimizi kolaylaştırmak adına iyi bir alışkanlıktır.
Örnek bir Lokasyon: Code2Work/DataScience/data-project-2.

### Proje Kurulumu Komutlar
Aşağıdaki komutları sıtrayla çalıştırınız.
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt => Install all dependencies
* python watch.py => Python run all tests

## Bonus
* Eğer daha detaylı bir şekilde testlerin içerisine bakmak isterseniz
* pytest .\tests\test_question.py -s -v 

### Projeye Başlamadan Önce
* Belirtilen sql querylerini yazabilmek için scripts klasörü altındaki bulunan init_db.py dosyası içerisindeki tüm queryleri 
sırasıyla kendi local veritabanınızda çalıştırınız. 
* Veritabanınızın hazır olduğundan emin olmak için tüm tablolara birer SELECT sorgusu atıp sonuçların doğru olduğundan emin olunuz.
* Çalışırken sadece data klasörü altında bulunan questions.py dosyasında çalışacağız. Bunun klasör dışındaki kodları değiştirmeyiniz !
* connect_db fonksiyonu içerisinde veritabanına bağlanma bilgileri var. Projenizi kendi localinizde test ederken burada bilgileri kendi local veritabanı bilgilerinizle değiştirerek test ediniz. Ancak kodunuzu <b>pushlarken bu veritabanı bilgilerini ilk bulduğunuz şekilde bırakınız.</b> Çünkü kodlarınız Cloud bir ortamda bu bilgilerle bir veritabanına bağlancaklardır.

# Questions
1. NULL emailleri 'unknown@example.com' ile değiştir
2. İçerisinde '@' işareti geçmeyen emailleri bul.
3. customer tablosundan önce kullanıcının ismini daha sonra isminin ilk 3 harfini short_name ismiyle getir.
4. customer tablosundan önce kullanıcının ismini daha sonra emailinin @ şlaretinin sağ tarafında kalan kısmını(domain) bilgisini getiriniz.
5. Tüm müşterilerin isim ile emaili birleştirerek full_info ismiyle dönen sorguyu yazınız.
6. orders tablosundan tüm tutarları INTEGER'a çevirip order_id ile birlikte total_amount_int ismiyle dönen sorguyu yazınız.
7. müşterilerin ismini ve emaillerindeki @ işaretinin kaçıncı indkste olduğunun bilgisini at_position ismiyle dönen sorguyu yazınız.
8. ürünler tablosundan ürünün ismini ve kategorisini product_category ismiyle dönecek sorguyu yazınız. Eğer kategori NULL ise NULL terimini 'Unknown' ile değiştiriniz.
9. orders tablosu üzerinden customer_id, total_amount ve toplam harcamaya göre sıralamasını(RANK) rank_by_spend ismiyle dönen sorguyu yazınız.
10. Siparişlere göre çalışan toplamı (Running Total - SUM OVER) değerini bulan sorguyu yazınız.
11. Elektronik ve beyaz eşya ürünlerini tek listede getiren sorguyu yazınız
12. Tüm siparişler ve eksik siparişleri birleştiren sorguyu yazınız.