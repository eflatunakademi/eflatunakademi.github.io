Title: İnternette Gizli Kalın - TOR 
Date: 2018-06-27
Tags: 
Category: Blog
Slug: 
Authors: M. Enes Özen


*Tor(The Onion Router)* Tarayıcısı, internette gezinen kişilerin kimliğini gizleyerek ve internet otoritelerinin web trafiğini izlenmesini engelleyerek özel bilgileri koruyan bir tarayıcıdır. Tor aynı zamanda internet filitrelerini atlatmak için de kullanılabilir.

Tor ilk olarak Amerikan Donanması ile birlikte devlet içi iletişim için geliştirilmiştir. Şuan ise herkesin erişebildiği (gazeteci, aktivist, ordu vs.) sanal tünellerden gizlilik ve güvenlik sağlamaktadır.

Tor Tarayıcı, Mozilla Firefox’un güncel ve gizlilik açısından optimize edilmiş bir versiyonudur. Çevrimiçi anonimlik ve engellenmiş sitelere erişim sağlayan ücretsiz ve açık kaynaklı bir yazılımdır. Diğer tarayıcılardan farklı olarak Tor Tarayıcısı;

-	Kullanıcının IP adresini gizleyerek internette anonim dolaşmayı sağlar,
-	Engellenmiş sitelere erişim sağlar,
-	Normalde varsayılan olarak gelen çevrimiçi izleme özellikleri içermez,
-	Kullanıcı verilerinden para kazanmaz,
-	Dünyanın en ünlü uzmanlarının bazıları tarafından desteklenmekte ve önerilmektedir.

Tor Tarayıcı, ücretsiz ve açık kaynak yazılım üzerinde çalışan, gizlilik ve sansür atlatmayı etkin bir şekilde kullanmak için tasarlanmış Tor ağı üzerinde çalışır. Tor ağı, dünyanın dört bir yanındaki gönüllüler tarafından işletilen binlerce sunucudan oluşmaktadır. Tor tarayıcı her yeni bağlantıda 3 röle seçer ve bunlardan internete bağlanır. Her bağlantı esnasında röleler veriyi gönderdiği ve aldığı yolu tam olarak bilmeyecek şekilde şifrelenir.
Tor tarayıcı kullanıldığında internet bağlantısını farklı bir IP adresinden, genellikle farklı bir ülkeden gelmiş gibi gösterecektir. Bu sayede, erişilen web sitesinden IP adresimizi gizlerken, ağ trafiğimizi izlemeyi denetleyebilecek  üçüncü taraflardan erişilen web sitesini de gizler.

### 1.Tor Nasıl Çalışır?
Aşağıdaki adımlar, Ahmet'in bilgisayarının Merve’nin sunucusu ile iletişim kurmak için Tor Tarayıcı kullandığı zaman Tor ağının nasıl çalıştığını göstermektedir:
**Adım 1:** Ahmet’in Tor Tarayıcısı, Tor dizin sunucusundan(Ayşe) Tor röleleri[1] listesini alır.

![pic](/images/tor/1.jpg)

**Adım 2:** Ahmet'in Tor Tarayıcısı, Tor ağından hedef sunucuya (Merve) rastgele bir yol seçer. Tor ağındaki tüm bağlantılar şifrelenmiştir (yeşil [3]). Bu örnekte, son bağlantı şifrelenmemiştir (kırmızı [2]) çünkü Merve’nin sunucusu http’dir. Ancak Ahmet bir https web sitesini ziyaret ediyorsa son bağlantı da şifrelenmiş olurdu.
 
![pic](/images/tor/2.jpg)
 
**Adım 3:** Eğer daha sonra Ahmet başka bir sunucuyu (Mustafa) ziyaret ederse, Ahmet'in Tor Tarayıcısı farklı rastgele bir yol seçer.

![pic](/images/tor/3.jpg)
 
**NOT:** Anonimlik ve hız arasında bir ters orantı vardır. Tor, internet trafiğini dünyanın çeşitli yerlerinde bulunan gönüllü sunucular aracılığıyla yaptığı için anonimlik sağlar ancak normal internet bağlantısından neredeyse her zaman yavaş olacaktır.

**Dikkat !:** 2016 yılında Paris de düzenlenen Def Con 24 konferansında Tor Taracının *çıkış düğümleri (exit nodes)* kullanılarak bir zafiyet keşfedilmiştir. Bağlantı için kullanılan Tor röleleri gönüllüler tarafından yönetilir. Bu yüzden bu röleleri kontrol etmek mümkündür. Bu durumu istismar etmek isteyen kişler (hackerlar yada kanun koyucular) bu rölelerin içine kendi rölelerini ağ analiz teknolojileri kullanarak eklerler. Yukarıda da belirttiğim gibi mesaj rölelere şifrelenmiş katmanlar şeklinde gönderilir, rastgele bir şekilde başka röleye bağlantı sağlanır. Son röle yani exit node son katmanın şifresini çözebilir ve elde edilen mesaj açık metindir. Eğer bu son röle kötü niyetli bir düğüm ise bu röleye uğrayan mesaj açık bir şekilde okunabilir. Şöyleki bu mesaj da kişinin gerçek IP adresi ve yeri görünmeyecektir ancak kullanıcı adı, parola, banka bilgisi gibi bilgiler okunabilir.



### 2.Tor Tarayıcısının Yüklenmesi
**Adım 1:** Aşağıdaki adrese gidilir ve *Download Tor Browser* butonuna basılır.

![pic](/images/tor/4.jpg)

**Not:** Eğer yukarıdaki adrese erişim engellendiyse başka bir adresden indirebilmek için *gettor@torproject.org* adresine kullandığımız işletim sistemini (Windows,Osx veya Linux) belirterek bir e-posta göndererek edinebiliriz.
![pic](/images/tor/5.jpg)

**Adım 2:** İndirmek istediğiniz dili ve işletim sistemini belirleyin

![pic](/images/tor/6.jpg)


**Adım 3:** Kurulum dosyasının indirildiği dizine gidilir.

 ![pic](/images/tor/7.jpg)


**Adım 4:** exe dosyasına çift tıklanır ve ardından dil seçimi yapılır.
 
![pic](/images/tor/8.jpg)
 

**Adım 5:** Tor Tarayıcısının yüklenmek istenilen dizin belirlenir. Şekil 6 da yüklenilmek istenilen dizin olarak masaüstü seçilmiş.
 
![pic](/images/tor/9.jpg)
 
Şekil 6: Tor Tarayıcının kurulum yeri

**Adım 6:** Kurulumu tamamlamak için aşağıdaki pencerede bitir(finish) butonuna tıklayın. 

![pic](/images/tor/10.jpg)

### 3.Tor Ağına Bağlamak İçin Gerekli Ayarlar
**Adım 1:** Eğer Tor internete girilen ülkede engellenmemiş ise direk bağlan (connect) butonuna basarak tarayıcı açılabilir. Ancak Türkiye’de tor engellenmiş durumdadır. Bu sebeple ayarlar yapılandırılmalıdır.
 
![pic](/images/tor/11.jpg)
 

**Adım 2:** Yapılandır(Configure) butonuna basıldığında aşağıdaki pencere açılır. Burada Tor internete girilen ülkede engellendiği için köprü bağlantıları kullanılır. Köprü bağlantıları halka açık dizinde listelenmediği için engellenmesi daha zordur. Köprü olarak hazır bulunan obfs4 gibi aracılar seçilip bağlan(connect) butonuna basılır.
 
 ![pic](/images/tor/12.jpg)

**Adım 3:** Kısa bir süre sonra Tor Tarayıcı açılacaktır

![pic](/images/tor/13.jpg)

### 4.Özel Köprüler İle Tor Ağında Bağlanma

Tor ağına bağlanmak için daha az kişiler tarafından kullanılan ve bu sebeple engellenmesi daha düşük olan özel köprüler ile bağlantı yapılabilir. Tor sayfasına erişilemiyorsa “bridges@torproject.org” adresine “get bridges” yazip e-mail göndererek özel köprüler elde edilebilir.

Ancak Tor sayfasına erişilebiliniyorsa şu adımlar uygulanarak özel köprüler elde edilebilinir;

**Adım 1:** Aşağıdaki adrese gidilir ve sadece köprüleri bana ver(just give me bridges) butonuna tıklanır.
 
![pic](/images/tor/14.jpg)

**Adım 2:**  Güvenlik kodu doldurulur ve girişe basılır.
 
 ![pic](/images/tor/15.jpg)

![pic](/images/tor/16.jpg)

**Adım 3:** Aldığımız köprüler aşağıdaki bölüme kopyalanır ve bağlan (connect) butonuna tıklanır.

![pic](/images/tor/17.jpg)

### 5.Tor’u Güvenli ve Anonim Bir Şekilde Kullanmak İçin Yapılması Gerekenler
Tor Tarayıcı sadece Tor Tarayıcısı penceresinde yapılan işlemler için anonimlik sağlar. Uygulamanın çalışıyor olması diğer programların da Tor Ağını kullanıyor anlamına gelmemektedir.

**Tor Tarayıcının çalışıp çalışmadığını kontrol etme**
Tor tarayıcının düzgün bir şekilde kurulup çalıştığından emin olmak için Tor Ağ Ayarlarını Test Et(Test Tor Network Settings) linkine tıklanabilir.

![pic](/images/tor/18.jpg)

Eğer aşağıdaki gibi bir sayfayla karşılaşırsak Tor tarayıcının düzgün çalıştığını söyleyebiliriz.

![pic](/images/tor/19.jpg)

Tor Projesinin kendi control sistemi haricinde https://www.iplocation.net/ ve https://www.ip2location.com/ adreslerinden bağlantı bilgilerini öğrenebiliriz.

**Yeni Kimlik Oluşturma**

İstediğimiz zaman yeni kimlik oluşturabiliriz. Bu sayede Tor yeni bağlantı düğümleri oluşturacak ve erişilecek web sitelerine farklı bir IP adresinden ulaşıyor gibi görülecektir. Bunu yapmak için aşağıdaki adımlar uygulanabilir.

**Adım 1:** Tor Tarayıcısı menüsünü açmak için   butonuna tıklanır.

![pic](/images/tor/20.jpg)

**Adım 2:** Açılan menüden Yeni Kimlik (New Identity) seçilir. Tor Tarayıcı tarama geçmişini temizleyecek ve yeniden başlayacaktır. Tarayıcı yeniden başladığında farklı bir IP adresinden bağlandığını görebilirsiniz.

**NoScript Eklentisinin Etkinleştirilmesi**
Tor Tarayıcısı NoScript eklentisi ile birlikte gelir ancak devre dışı bırakılmıştır. NoScript, zararlı web sitelerinden ve gerçek kimliğimizi Tor Tarayıcısındaki kodlar aracılığıyla ifşa edilmesine karşı ek koruma sağlar. Bu nedenle NoScript eklentisinin aktif edilmesinde fayda vardır.
Aşağıdaki adımlar izlenerek NoScript aktif edilebilir.

**Adım 1:** Tor Tarayıcının sol üstünde yer alan   simgesine tıklanır.

![pic](/images/tor/21.jpg)


**Adım 2:** Global Olarak Komutları Engelle( Forbid Scripts Globally) seçilir.

Bu ayar yapıldığında pek çok siteyi bozuk görebilirsiniz. Eğer web sitesi doğru yüklemeyi başaramaz ise şekil 1’de gösterilen tuşa tıklayarak ve geçici olarak bu sayfaya izin ver(Temporarily allow all this page) seçilerek web sitesi NoScript beyaz listesine eklenebilir.

**HTTPS Everywhere Eklentisini Etkinleştirmek**

HTTPS Everywhere eklentisi Tor Tarayıcı ile birlikte gelmektedir. Bu eklenti yardımıyla internette gezinirken girilen sitelerin HTTP yerine HTTPS protokolünü otomatik olarak devreye sokarak güvenli bir şekilde dolaşmamızı sağlar. Bu sayede günümüzde sıkça rastlanılan Phishing(Oltalama) saldırılarına karşı bir nebze daha koruma sağlar.

Aşağıdaki adımlar izlenerek HTTPS Everywhere eklentisi aktif edilebilir.

**Adım 1:** Tor Tarayıcın sağ üst köşesinde bulunan   simgesine tıklanır.
 
 ![pic](/images/tor/22.jpg)
 
**Adım 2:** HTTPS Everywhere’ e izin ver(Enable HTTPS Everywhere) ve tüm şifrelenmemiş istekleri engelle(Block all unencrypted requests) kutucukları işaretlenir. Eğer HTTP kullanan bir siteye tekrar erişmek istersek tüm şifrelenmemiş istekleri engelle(Block all unencrypted requests) kutucuğundaki seçenek kaldırılmalıdır.

### Deep Web – Dark Web
Tor denildiği zaman akla ilk gelen kavramlardan biri Deep Web(Derin İnternet). İnternette arama yapıldığında ilk olarak karşımıza çıkan bir buz dağı resmidir.

![pic](/images/tor/23.jpg)

 Burada suyun üzerinde kalan yani bizim dışardan baktığımızda gördüğümüz kısım normal tarayıcılar ile eriştiğimiz içerikleri temsil etmektedir. Geri kalan suyun altındaki büyük bölüm ise Deep Web’i yani derin interneti temsil etmektedir. Buradaki sitelere ve bilgilere erişmek için Tor Tarayıcı kullanmak gerekmektedir. Çünkü bu içeriklerin güvenli olmaması ve suç teşkil etmesi sebebiyle günlük hayatta kullandığımız arama motorları tarafından listelenmemektedir. Genellikle buradaki siteler .onion/.clos uzantılıdır. http://[rastgele rakamlar ve sayılar].onion/.clos şeklinde karışık, herhangi bir anlam ifade etmeyen alan adlarından oluşmaktadır. Resimde de görüldüğü gibi Deep Web katmanlı bir yapıya sahiptir bu yüzden daha derine inilmek isteniyorsa özel cihazlara ihtiyaç duyulmaktadır.
 

Sonuç olarak; 
İnternetin tehlikelerle dolu bir ortam olduğu bu günlerde gizliliği ve güvenliği mümkün olduğunca sağlamaya çalışan Tor Tarayıcısı, aynı zamanda internet sansürüne karşı bir atlatma yöntemi sunar. Ancak “Kontrolsüz güç güç değildir” ilkesinden yola çıkarak eğer kullanıcı Tor Tarayıcının gücünü, Tor’un özellik ve kabiliyetlerini bilmeden kullanırsa hem Tor’u etkin bir şekilde kullanmamış olur hem de ciddi güvenlik problemleriyle karşılaşabilir.

MEHMET ENES ÖZEN - [Arka Kapı Dergisi 2. Sayı](https://www.arkakapidergi.com/)




Kaynak:
[https://www.torproject.org/about/overview.html.en](https://www.torproject.org/about/overview.html.en)
[http://www.cs.tufts.edu/comp/116/archive/fall2016/npatel.pdf](http://www.cs.tufts.edu/comp/116/archive/fall2016/npatel.pdf)
[https://boingboing.net/2016/07/01/researchers-find-over-100-spyi.html](https://boingboing.net/2016/07/01/researchers-find-over-100-spyi.html)
[https://en.wikipedia.org/wiki/Tor_(anonymity_network)](https://en.wikipedia.org/wiki/Tor_(anonymity_network))
[https://securityinabox.org/en/guide/torbrowser/windows/](https://securityinabox.org/en/guide/torbrowser/windows/)






