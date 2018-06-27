Title: Veri Gizleme Sanatı STEGANOGRAFİ
Date: 2018-06-27
Tags: 
Category: Blog
Slug: 
Authors: Huriye Özdemir


Güvenlik deyince aklımıza ilk gelen kavramlar hiç kuşkusuz veri gizliliği *(secrecy)* ve mahremiyettir*(privacy)*. Birbirine oldukça benzeyen bu iki kavram aslında bazı noktalarda farklılık gösteriyor.


Biz bir veriyi çeşitli algoritmalarla veya araçlarla şifreleyebilir yani üçüncü kişilerin anlayamayacağı bir biçime dönüştürebiliriz. Fakat bu durumda üçüncü kişiler bu verinin varlığından haberdar olur ve çeşitli yöntemler ile çözümlemeye çalışır. Veriyi bu şekilde    mahrem hale getiren *“Kriptografi”* biliminde verimizin güvenliği, güçlü algoritmalarla etkili bir şekilde karıştırılıp anlaşılamaz hale gelmesine bağlıdır.

Bir diğer yöntem ise bu verinin varlığından bile haberdar olunmadan veriyi çeşitli yollarla gizlemek, çözümlenebilmesi için üçüncü kişilerin eline geçmesini dahi önlemektir. Bu yazımda asıl üzerinde durmak istediğim *Steganografi* bilimi ise bu noktada devreye giriyor.
İngilizce’de “Steganography”, Yunanca’da ise “Steganos (gizli, saklı)” ve “Graphein (yazı)” kelimelerinden oluşur. Tarihi incelediğimizde yüzyıllardan beri veri gizleme ihtiyacı hep var olmuş, özellikle savaşlarda, diplomatik haberleşmelerde ve istihbarat amaçlı olarak çokça kullanılmış, çeşitli yöntemler geliştirilmiştir. Eski Yunan tarihçisi Heredot tarafından yazılmış olan Histories kitabında bulunan ilk Steganografi örneği ise Yunan ve Pers İmparatorluğu arasında geçen savaş esnasında Pers yöneticilerinden Histiaerus’ın, isyan başlatmasını istemek için kölesinin saçlarını kazıtıp gizli mesajını yazması ve saçları uzadığında bu köleyi Aristagoras’a yollaması ve mesajını iletmesi ile olmuştur.

Yine milattan önce kullanılan yöntemlerden biri olan , balmumu tabletlerin içine yazının yazılıp tekrar balmumu ile kapatılması, İkinci Dünya Savaşı’nda görünmez mürekkep kullanımı, mikro noktalama ve boş şifreleme (null cipher) teknikleri, sıradan cümleler kullanılarak gizli harflerin yerlerinden kaynaklanan yöntemler ile şifreli mesajlar iletilmesi, işkence gören bir mahkumun gözlerini açıp kapayarak mors alfabesi yoluyla iletişim kurması, sadece mor ötesi ışıkla görülebilen yazılar yazmayı sağlayan kalemler kullanılması gibi geçmişten verebileceğimiz pek çok ilginç örnek bulunmaktadır.

Peki günümüzün gelişmiş teknolojisini düşünecek olursak veri gizleme teknikleri ne kadar ilerlemiştir? Dijital dünyadaki yeni teknikler ise şu şekildedir:
•	Görüntü veya ses dosyalarındaki en düşük bitlerin içerisine mesajları gizlemek
•	Bir ses dosyasının yankısını değiştirmek
•	Bir dosyanın görünmeyen ya da kullanılmayan alanlarına veriyi yerleştirmek
Steganografi biliminde kullanılan terminolojik bazı kavramlar ise şu şekildedir:
**Taşıyıcı ya da kapak dosyası (cover):**  Gizli bilginin içerisine yazılacağı orijinal dosya.
**Stego-medium:** Bilginin saklanacağı ortam.
**Gömülü (embedded/payload) :** Kapak dosyasında gizlenmiş veri.
**Stego:** Mesaj gömüldükten sonra dosyanın hali.
**Steganaliz:** Dosya içerisine gömülmüş veriyi tespit etme işlemi. 

# STEGANOGRAFİ METOTLARI
**Metin Steganografi**
Bu teknik oldukça basit görünmesine rağmen metin içerisine gizlenmiş veriyi bulmak oldukça zor. Öncelikle metin içerisinde cümle yapıları oluşturulur ve belirlenmiş kurallara göre harfler eklenir, boşluklar doldurulur. Metin içerisinde ifade tarzında herhangi bir hata olmaz fakat bazı kelimelerde morfolojik hatalar görülebilir. Örnek olarak, Alman bir casusun İkinci Dünya Savaşı’nda kullandığı şifreli metni inceleyelim:

*“Apparently neutral’s protest is thorougly discounted and ignored. Isman hard hit. Blockade issue affects Pretext for embargo on by products, ejecting suets and vegetable oils.”*

Her kelimenin ikinci harfini birleştirerek mesajını iletmiş:

*“Pershing sails from NY June .”*

Metin Staganografi’nin satır/kelime kaydırma (Line/Word shifting), açık alan (Open Spaces), karakter kodlama (encoding), semantik metotlar, kelimeler içinde özel karakter kullanımı, ilkleme (akrostiş) gibi kullanılabilecek daha birçok yöntemi vardır.


**Görüntü Steganografi**
En sık kullanılan yöntemlerden biri olan Görüntü Steganografi ile resmin pikselleri içerisine mesajlarımızı gizleyebiliyoruz. En az öneme sahip bite ekleme, yani *“LSB (Least Significant Bit) in BMP”* tekniğinde veri saklamak için ideal olan, herhangi bir sıkıştırma yapmadan resmin özelliklerini tutan 24 bitlik resim dosyası BMP (Bitmap) içerisine veriyi gizleyebiliriz. Her pikselin 24 bit olduğunu düşünürsek 2 bitlik oynamalar fark edilebilir bir değişiklik yapmayacaktır. Her pikselin renk değeri ise kırmızı yeşil ve mavi renklerini içeren 3 byte’lık alanda tutulur.


24 bitlik resmin 3 pikselinin şu şekilde olduğunu düşünürsek:
(00101101	 00011101	 11011100)
(10100110	 11000101	 00001100)
(11010010  	 10101100  	 01100011)


Her 8 bitin LSB’sini işaretlediğimizde 200 sayısının binary karşılığı olan 11001000 sayısı karşımıza çıkıyor.


(0010110**1**	 0001110**1**	 1101110**0**)
(1010011**0**	 1100010**1**	 0000110**0**)
(1101001**0**  	 1010110**0**  	 01100011)


Bunun gibi LSB’ler kullanılarak harflerin binary karşılıkları ile veriler bitler içerisine kolaylıkla gizlenebilir.


Bu işlemi gerçekleştirmek için sık kullanılan Steghide aracını Linux işletim sistemimize kurarak verilerimizi nasıl gizleyeceğimizi uygulamalı olarak görelim.
1.	Öncelikle “apt-get install steghide” komutu ile aracımızın kurulumunu yapıyoruz.

![pic](/images/stega/1.PNG)

2.	Kurulduktan sonra *“Steghide”* yazarak verimizi gizlemek için ne gibi parametreler kullanabileceğimizi görebiliriz. 

![pic](/images/stega/2.PNG)

3.	Ben *“Steghide embed -cf ogemi.jpg -ef parolalarım.txt”* komutu kullanarak verilerin gizleneceği dosyayı belirtmek için -cf, hangi dosyayı gizleyeceğimizi belirtmek için ise -ef parametresini kullandım. *“Embedding Options”* kısmını inceleyerek eklemek istediğiniz parametreler varsa ekleyebilirsiniz. Veri gömülürken de üçüncü kişilere karşı tedbir amaçlı bir “passphrase” oluşturmamız isteniyor.

![pic](/images/stega/3.PNG)

4.	Text dosyamızın içeriğini o gemiye istifledikten sonra gemimizin yükünü inceleyebiliriz. Yani *“steghide info ogemi.jpg”* komutu ile içerik hakkında bilgi alalım.

![pic](/images/stega/4.PNG)

5.	Son olarak gemimizin yükünü hafifletmek ve parolalarımızı çekmek istersek de *“steghide extract -sf ogemi.jpg”* komutunu kullanıyoruz.  Dosyayı çıkartmak için ise en başta oluşturduğumuz şifreyi giriyoruz.

![pic](/images/stega/5.PNG)

6.	Son olarak resmimize baktığımızda öncesi ve sonrası arasında fark edilebilir bir değişim olmadığını görüyoruz. Yani gemimiz hala kalbin derinliklerine gömülmüş bir şekilde bekliyor. 

![pic](/images/stega/önce.PNG) ![pic](/images/sonra/5.PNG)


**Ses Steganografi**

Ses steganografi ise bir ses dosyasında verileri gizlemeye veya güvenli ve sağlam bir şekilde işaretlemek için kullanılır. Gizli bir bilgi, ses sinyalleri kullanılarak gömülmek suretiyle gizlenmiş olur. Bu yöntem, savaş alanı iletişimi ve bankacılık işlemleri gibi bazı uygulamalarda ciddi ve hayati bir öneme sahiptir. Bu gömme işlemi de tıpkı görüntü steganografide olduğu gibi binary değerleri değiştirerek yapılır. Fakat görüntüden farklı olarak ses dosyası için kullanılan sinyal işleme metotları daha karmaşıktır.

Ses sinyallerini dijital ve analog olmak üzere ayırırsak dijital sesler ayrık, analog sesler ise süreklidir. Ayrık sinyaller, belirli oranlarda sürekli analog sinyalleri işlenerek üretilir. Örneğin, CD için dijital ses  işleme oranı 44 kHz'dir. Aşağıdaki şekilde dijital ses sinyali dalgası oluşturmak için işlenmiş sürekli bir analog ses sinyali dalgasını göstermektedir.

![pic](/images/stega/sinyal.PNG) ![pic](/images/stega/sinyal2.PNG)
 
**Ses Steganografi Metotları**

Matematik ve sinyal işleme alanındaki gelişmelerle birlikte ses dosyalarına veri gömmek için bir çok metot geliştirilmiştir. Bu yüzden en sık kullanılanlar üzerinde durmak istiyorum.

**LSB (Least Significant Bit) Kodlama Metodu**
Görüntü steganografide de belirtmiş olduğum gibi en sık kullanılan ve en kolay yöntemlerden biri olan LSB kodlama ses dosyaları için de şüphesiz aynı öneme sahip. Ses dosyaları için nasıl olduğunu yine bir örnekle inceleyecek olursak aşağıdaki tabloda “Hi” kelimesinin binary karşılığının LSB ile kodlandığını görüyoruz.
Bu yöntem ile ses düzeyindeki değişiklikler kulağımızla algılayamayacağımız seviyededir. İnsan kulağının duyamayacağı 20.000 Hz. üzerindeki frekanslar ayarlanarak mesajlar gizlenir.

**Eşlik biti (Parity) Kodlama Metodu**
Parity kodlamasında ise ses sinyali ayrı örnek alanlarına ayrılır ve her mesaj bir eşlik biti içindeki alanda gizlenir. Bu nedenle, bu metot bitleri gizlemek için daha geniş bir seçenek yelpazesi sunar ve sinyaldeki değişimi daha gözlemlenemez hale getirir.

![pic](/images/stega/sinyal3.PNG)

Bu tekniklerden farklı olarak faz kaymaları kullanılarak veri gizlemeye yarayan *Faz Kodlama (Phase Coding)* tekniği, ses sinyalinin frekans spektrumu boyunca gizli verileri mümkün olduğunca maksimum seviyede dağıtmaya çalışan *Yayılı Spektrum (Spread Spectrum)* tekniği ve gizli verinin ayrık bir sinyale eko eklenerek bir ses ortamına sokulmasını sağlayan Eko Gizleme tekniği gibi yöntemler de mevcuttur fakat ayrıntıya girmeden bu işlemi hangi araçlarla nasıl yapabileceğimizden bahsedeceğim.


Teknik bilgiden biraz pratik bilgiye geçiş yapalım. Eğer Mr. Robot dizisini izliyorsanız 1. Sezon 8. bölümde Elliot’un *DeepSound* aracını kullanarak verileri ses dosyaları içerisine nasıl sakladığını da görmüş olmalısınız.
 
DeepSound aracında *“Open carrier files”* seçeneği ile ses dosyasını seçip, *“Add secret files”* seçeneği ile de saklamak istediğimiz dosyayı ekliyoruz. Ses kalitesini istediğimiz gibi ayarlayıp *“Encode secret files”* dediğimizde veriyi gömmeden önce istediğimiz formatı seçip şifre belirledikten sonra da işlem tamamlanmış oluyor. Veriyi sakladığımız ses dosyasını tekrar programda açtıktan sonra *“Extract secret files”* dediğimizde ise gizli veriye ulaşmış oluyoruz.

Steghide ve DeepSound dışında elbette onlarca araç geliştirilmiş durumda. *QuickStego, StegFS, StegoShare, Outguess, Stegbreak, Zsteg, OpenStego, Matroschka, AudioStegano, BitCrypt, MP3Stego, Xiao, Crypture, SteganographX Plus, rSteg, SSuite, Picsel, Camouflage, Hide’N’Send* bunlardan sadece bazıları. Bu saydığım araçların içerisinde hem görüntü hem de ses dosyaları için geliştirilmiş olanları da bulunuyor.


Steganografi metin, ses, resim ya da video dosyalarına telif hakkı sağlamak amacıyla *damgalama (watermarking)* işlemlerinde de kullanılır. Dijital damgalama görünür ve görünmez olmak üzere ikiye ayrılır. Görünen damgalama, herhangi bir resmin köşesinde bulunan logo olabilir. Görünmeyen damgalamada ise kişiye özel veriler ona sahiplik oluşturması açısından dosyaya gömülür.


Son olarak *Steganaliz* ise bir taşıyıcı dosya içerisinde, saklanmış bir bilgi olup olmadığını bulmayı, eğer var ise bu bilgiyi elde etmeyi amaçlayan ve steganografik sistemlere karşı yapılan analiz ve araştırmalara denir. *Pasif (tarama)* ve *aktif (bozma/yok etme)* olarak ikiye ayrılır. Steganalistler çeşitli steganografik saldırılara karşı incelemeler yaparlar. Bu saldırı tipleri ve amaçları kısaca şu şekildedir.


**File only:** 	Saldırganın dosyaya erişimi vardır ve içeride gizlenmiş bir mesaj olup olmadığını belirlemeye çalışır.
**File an Original copy:**	Saldırgan şifrelenmiş mesajın bir kopyasına ve orijinalinin bir kopyasına sahip olabilir.
**Reformat Attack:**	Dosyanın biçimi değiştirilir.
**Compression Attack:**	 Sıkıştırma algoritmaları ile gereksiz bilgiler bir dosyadan kaldırılmaya çalışılır.
**Visual Attack:**	Bir insanın görsel anormallikleri aramasına izin verecek şekilde nesnenin bir kısmını saran stego-only-ataktır.
**Structural Attack:**	 Saldırgan, bitlerin istatistiksel profilini inceler bir mesajın varlığını tespit edebilir.
**Statistical Attack:**	Potansiyel bir kapak dosyasının frekans dağılımının, kapak dosyasının teorik olarak beklenen dağılımı ile karşılaştırılmasıdır.

Geçmişten günümüze Steganografi sanatının tarihsel sürecini incelediğimizde ne kadar mesafe katettiğini açıkça görebiliyor, gelecekte de hızla ilerleyip yepyeni tekniklerle karşımıza çıkabileceğini de tahmin edebiliyoruz. İnsanlar için gizlilik ve mahremiyetin oldukça önemli olduğunu düşünürsek Steganografi ve Kriptografi bilimleri birbirlerini tamamlayarak hayatımızda önemli ve vazgeçilmez bir yer kaplıyor.

HURİYE ÖZDEMİR - [Arka Kapı Dergisi 2. Sayı](https://www.arkakapidergi.com/)

**Kaynakça:**

[http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.401.5678&rep=rep1&type=pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.401.5678&rep=rep1&type=pdf)
[http://resources.infosecinstitute.com/steganography-and-tools-to-perform-steganography/#gref](http://resources.infosecinstitute.com/steganography-and-tools-to-perform-steganography/#gref)
https://www.slideshare.net/UttamJain/steganography-14902856 
http://steganography-info.blogspot.com.tr/2008/04/steganography-and-attacks.html 


