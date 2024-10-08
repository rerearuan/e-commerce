# TUGAS INDIVIDU PBP
**Nama**: Regina Meilani Aruan  
**NPM**: 2306275632

## Daftar Isi
1. [Tugas 1](#tugas-1)
2. [Tugas 2](#tugas-2)
3. [Tugas 3](#tugas-3)
4. [Tugas 4](#tugas-4)
5. [Tugas 5](#tugas-5)
6. [Tugas 6](#tugas-6)

## TUGAS 2

### 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?

Pertama-tama, saya membuat direktori bernama e-commerce, kemudian menginstal semua dependencies yang diperlukan, termasuk Django. Selanjutnya, saya menjalankan perintah django-admin startproject main untuk memulai proyek Django baru dengan nama main.

Kedua, untuk menambahkan aplikasi dengan nama main ke dalam proyek e-commerce, saya menggunakan perintah python manage.py startapp main. Perintah ini membuat sebuah folder main dengan struktur dasar aplikasi Django yang diperlukan. 

Ketiga, agar aplikasi main dapat diakses, saya membuat file urls.py di dalam direktori main dan menambahkan routing yang diperlukan. Ini memastikan bahwa URL yang dikunjungi pengguna diarahkan ke tampilan yang sesuai dalam aplikasi main.

Keempat, di dalam main/models.py, saya mendefinisikan model Product dengan atribut yang relevan untuk aplikasi mainnya BambooShop. Model Product memiliki atribut sebagai berikut:
- name (nama produk) dengan tipe data CharField yang dapat menyimpan hingga 255 karakter
- price (harga produk) dengan tipe data DecimalField yang dapat menyimpan angka desimal dengan hingga 10 digit dan 2 angka di belakang koma
- description (deskripsi produk) dengan tipe data TextField untuk deskripsi produk yang lebih panjang.
- stock (jumlah stok) dengan tipe data IntegerField, default 0.
- category (kategori produk) dengan tipe data CharField yang memiliki panjang maksimum 100 karakter.
- rating (penilaian produk) dengan tipe data FloatField, default 0.
- date_added (tanggal ditambahkan) dengan tipe data DateTimeField yang otomatis mengisi tanggal dan waktu saat produk ditambahkan.
- review (ulasan produk) dengan tipe data TextField, yang dapat kosong atau null.
Setelah mendefinisikan model, saya menjalankan migrasi untuk memperbarui database dengan struktur tabel baru.

Kelima, di file views.py, saya membuat fungsi show_main yang menangani request dan mengembalikan template HTML bernama main.html. Fungsi ini menyertakan data produk dalam konteks yang akan ditampilkan pada template. Contoh data produk mencakup atribut seperti nama, harga, deskripsi, stok, kategori, penilaian, tanggal ditambahkan, dan ulasan.

Keenam, di main/urls.py, saya menambahkan routing untuk memetakan fungsi show_main yang telah dibuat di views.py. Ini menentukan URL yang diakses pengguna dan menghubungkannya dengan tampilan yang sesuai.

Ketiga, untuk membuat aplikasi BambooShop dapat diakses secara online, saya mengakses halaman PWS, mendaftar jika belum memiliki akun, lalu membuat proyek baru. Di file settings.py proyek Django, saya menambahkan URL deployment PWS ke dalam ALLOWED_HOSTS. Kemudian, saya mengisi credentials yang diberikan untuk menyelesaikan proses deployment dan memastikan aplikasi BambooShop dapat diakses oleh teman-teman melalui Internet.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Client Request ->  URL Routing (urls.py) -> View Function (views.py) -> Model (models.py) -> Database -> HTML Template -> Client Response

Pada bagan alur request dan response di aplikasi Django, urls.py berfungsi sebagai pengatur rute, menentukan bagaimana URL yang diminta oleh client dipetakan ke fungsi view yang tepat di views.py. Fungsi view tersebut memproses request dan, jika diperlukan, berinteraksi dengan models.py untuk mengambil atau memanipulasi data dari database. Setelah data diproses, fungsi view mengirimkan data tersebut ke berkas HTML Template untuk dirender menjadi format yang dapat ditampilkan di browser. HTML Template ini kemudian dipergunakan untuk menyusun respons akhir yang dikirim kembali ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah alat penting dalam pengembangan perangkat lunak karena ia mengelola versi kode dengan efisien. Dengan Git, pengembang dapat melacak perubahan kode secara rinci, yang membantu mereka memahami bagaimana dan kapan kode berubah seiring waktu. Git memudahkan kolaborasi dengan memungkinkan beberapa pengembang bekerja pada proyek yang sama secara bersamaan melalui sistem branching dan merging. Ini juga memungkinkan rollback atau pengembalian ke versi sebelumnya jika terjadi kesalahan, serta menyediakan sistem yang transparan untuk mengelola dan mengintegrasikan perubahan dari berbagai kontributor.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dijadikan pilihan untuk pembelajaran awal karena kemudahan penggunaannya dan struktur yang jelas. Framework ini mengintegrasikan berbagai fitur penting secara default, seperti otentikasi dan manajemen basis data, yang memungkinkan pemula fokus pada logika aplikasi daripada harus membangun dari nol. Dokumentasinya yang lengkap dan komunitas yang aktif mempermudah proses belajar, sementara struktur arsitektur Model-View-Template (MVT) membantu pemula memahami bagaimana aplikasi web bekerja secara sistematis.

### 5. Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM atau Object-Relational Mapping karena menghubungkan objek Python dengan tabel-tabel di database. ORM memungkinkan pengembang untuk berinteraksi dengan data menggunakan sintaks Python yang familiar, daripada menulis query SQL yang rumit. Ini membuat pengelolaan data lebih intuitif dan terintegrasi langsung dengan kode aplikasi, memungkinkan pengembang untuk menangani data sebagai objek dan mengelola hubungan antar data dengan cara yang lebih alami dan mudah dipahami.



## TUGAS 3

### 1.  Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

*Data delivery* sangat penting dalam pengimplementasian platform karena dapat memungkinkan pertukaran data antar bagian sistem yang berbeda, misal dari satu stack ke stack lainnya. XML dan JSON adalah dua format data yang umum digunakan untuk mentransfer informasi antara aplikasi web atau layanan web. Dalam sebuah aplikasi, *front-end* sering kali membutuhkan data dari *back-end* (server) untuk menampilkan informasi dan memproses permintaan user.  Dengan adanya implementasi *data delivery*, seperti menggunakan format XML atau JSON, komunikasi ini menjadi lebih mudah dan teratur.


### 2.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON lebih populer dibandingkan dengan XML karena secara struktur lebih sederhana dan mudah digunakan, terutama untuk aplikasi modern. JSON dirancang untuk pertukaran data dengan format yang lebih ringkas, sehingga lebih cepat diproses dan dikirim. Hal ini membuat komunikasi antar sistem menjadi lebih efisien, terutama untuk API dan aplikasi seluler yang membutuhkan kecepatan.

Struktur JSON terdiri dari pasangan *key-value*, yang mirip dengan objek dalam pemrograman. Setiap *key* berfungsi sebagai nama atau kunci, sedangkan *value* adalah nilai yang terkait dengan kunci tersebut. Format ini memungkinkan data disimpan dan diakses dengan lebih mudah.

Berbeda dengan XML yang lebih rumit dan sering digunakan untuk menyimpan data kompleks, JSON lebih fokus pada pertukaran data yang cepat dan ringan. Selain itu, JSON lebih mudah dibaca oleh manusia dan langsung dapat digunakan di JavaScript tanpa memerlukan alat tambahan, yang membuatnya lebih praktis untuk aplikasi web masa kini. Jadi, jika tujuan utamanya adalah performa dan kecepatan, JSON umumnya menjadi pilihan yang lebih tepat.


### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada Form Django digunakan untuk memvalidasi data input yang diterima dari user. Fungsinya adalah memastikan bahwa data yang dimasukkan sudah sesuai dengan aturan validasi yang ditentukan dalam form tersebut. Jika data valid, method ini akan mengembalikan *True*, sehingga form dapat diproses untuk menyimpan data ke database. Namun, jika data tidak valid, `is_valid()` akan mengembalikan *False* dan Django akan menampilkan pesan kesalahan kepada user.

Proses validasi ini terjadi saat data difilter dan dibersihkan. Ada tiga metode pembersihan (*cleaning*) yang berjalan selama validasi, biasanya dijalankan ketika `is_valid()` dipanggil. Proses ini memastikan data memenuhi semua aturan yang ditetapkan. Jika diperlukan penyesuaian pengolahan, perubahan dapat dilakukan pada berbagai metode tersebut, tergantung pada tujuan validasi yang ingin dicapai. (Django Documentation)


### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token diperlukan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Setiap kali halaman dengan form muncul, Django secara otomatis menghasilkan token acak (random string) yang disisipkan ke dalam form. Ketika form tersebut dikirim, token ini ikut terkirim ke server, dan di server, token tersebut akan diperiksa untuk memastikan bahwa permintaan itu benar-benar berasal dari pengguna yang sah, bukan dari penyerang.

Jika kita tidak menambahkan CSRF token, aplikasi kita akan menjadi rentan terhadap serangan CSRF. Dengan CSRF token, permintaan ini bisa dicegah karena server akan mendeteksi bahwa token yang dikirim tidak valid atau tidak ada, sehingga permintaan akan ditolak. (Django Documentation)


### 5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama-tama, saya membuat form input di dalam file `views.py`. Di sini, saya memastikan form tersebut terhubung ke model yang menggunakan UUID. Saya mengimpor form dari `forms.py` dan membuat fungsi `create_product_entry` di `views.py`. Fungsi ini menangani permintaan POST untuk menyimpan data produk yang baru dimasukkan.

Langkah berikutnya adalah membuat file `create_product_entry.html` di dalam folder main/templates. Saya menggunakan template dasar dari `base.html` (skeleton) yang sudah dibuat sebelumnya. Dengan ini, form input dapat terstruktur dengan baik. Di halaman ini, saya menggunakan block content untuk mengisi form produk bambooshop.

Saya memastikan bahwa UUID digunakan di dalam model produk untuk setiap entri baru yang ditambahkan. UUID berguna untuk memberikan ID unik pada setiap produk, memastikan tidak ada bentrok ID saat data produk bertambah.

Setelah form selesai, saya menambahkan 4 fungsi views baru untuk melihat data yang sudah dimasukkan. View pertama dan kedua berfungsi untuk menampilkan data dalam format XML dan JSON. View ketiga dan keempat memungkinkan melihat data spesifik berdasarkan ID dalam format XML dan JSON.

Langkah berikutnya adalah menambahkan routing di file urls.py. Saya membuat URL yang terhubung ke setiap view yang sudah dibuat sebelumnya, sehingga masing-masing format dan view (baik yang menampilkan semua data atau berdasarkan ID) bisa diakses melalui URL yang berbeda.

Setelah semua routing dan view sudah siap, saya menggunakan Postman untuk menguji setiap URL yang menampilkan data dalam format XML dan JSON.  Tak lupa, saya melakukan add-commit-push ke GitHub E-commerce saya. Untuk deploy PWS. saya sedikit terhambat karena masih ada error atau failed terus menerus. Saya telah menyertakan bukti screenshot hasil dari Postman sebagai dokumentasi bukti pengujian.


<img src="xmlimage.png">
<img src="jsonimage.png">
<img src="xmlidimage.png">
<img src="jsonidimage.png">


## TUGAS 4

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?

`HttpResponseRedirect()` dan `redirect()` di Django memiliki kesamaan pada fungsinya, yaitu keduanya digunakan untuk mengarahkan pengguna ke URL yang berbeda setelah permintaan dikirimkan ke server. Perbedaan utamanya adalah `HttpResponseRedirect()` hanya menerima URL lengkap sebagai argumen, sedangkan `redirect()` lebih fleksibel.  Dengan menggunakan `redirect()`, kita bisa langsung memasukkan URL, nama pola, dan objek mode. Sehingga, Django secara otomatis akan mengelola proses pengalihan halaman tersebut. Sedangkan dengan `HttpResponseRedirect()`, kita harus memberikan URL penuh sebagai parameter, jadi kita perlu menuliskan URL lengkap atau membangunnya secara manual. Berdasarkan dokumentasi resmi Django, `redirect()` lebih sering digunakan karena kemudahannya dalam menangani berbagai skenario pengalihan halaman secara efisien.


### 2. elaskan cara kerja penghubungan model Product dengan User!

Model `Product` dan `User` di Django dapat dihubungkan menggunakan `ForeignKey`. Dengan cara ini, kita dapat memastikan bahwa setiap `product` yang ditambahkan ke sistem terkait dengan `user` yang spesifik. Misalnya, dalam model `Product`, kita bisa menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)`. Jika `user` tersebut dihapus, maka `product` yang terkait dengan `user` tersebut juga bisa dihapus. Ini adalah cara yang efektif untuk mengelola hubungan antar objek dalam database.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

*Authentication* dan *authorization* adalah dua konsep yang berbeda, tetapi saling berkaitan. *Authentication* (otentikasi) adalah proses verifikasi identitas pengguna, biasanya melalui nama user dan kata sandi, untuk memastikan bahwa kita adalah pemilik akun yang sah. Setelah berhasil diotentikasi, *authorization* (otorisasi) menentukan hak akses user terhadap fitur atau bagian tertentu dalam aplikasi berdasarkan izin yang mereka miliki. Saat pengguna login, Django menggunakan model `User` untuk otentikasi, sedangkan otorisasi dilakukan dengan sistem `permissions` sehingga pengaturan akses ke fitur tertentu hanya untuk user yang berhak.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat user yang telah login dengan menggunakan sesi berbasis cookie. Ketika kita berhasil login, Django akan membuat cookie khusus di browser pengguna yang berisi ID sesi yang unik. ID ini digunakan untuk melacak sesi pengguna selama menggunakan web tanpa perlu meminta login kembali di setiap halaman. Selain untuk melacak login, cookie juga sering digunakan untuk menyimpan data sesi sementara lainnya.  Untuk memastikan keamanan cookie, kita bisa menggunakan Secure dan HttpOnly flags agar lebih aman dari serangan seperti Cross-Site Scripting (XSS) yang bisa mengeksploitasi data cookie.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama-tama, saya membuat halaman `register.html` dan `login.html` di dalam folder `templates` di `main app`. Di sini, saya memastikan form registrasi dan login terhubung dengan model `User` bawaan Django. Di `views.py`, saya mengimpor `UserCreationForm` untuk form registrasi dan menambahkan fungsi `register` yang akan menangani permintaan POST dan menampilkan pesan sukses saat pengguna berhasil membuat akun baru. Saya juga menambahkan form login dengan mengimpor `authenticate` dan `login`, kemudian membuat fungsi `login_user` yang menangani proses login dan merender `login.html`.

Setelah itu, saya memastikan pengguna bisa logout dengan membuat fungsi `logout_user` yang mengimpor `logout` dan menambahkan button di halaman utama untuk memanggil fungsi ini. Saya juga menambahkan decorator `@login_required` pada fungsi `show_main` di `views.py`, sehingga pengguna hanya bisa mengakses halaman utama setelah login. Semua fungsi ini kemudian saya sambungkan dengan `urls.py` untuk membuat routing yang sesuai.

Untuk membuat dummy data, saya mulai dengan membuat dua akun pengguna baru secara manual di aplikasi. Setelah itu, saya menambahkan tiga data produk dummy untuk setiap akun di database lokal. Saya membuat file `dummy_data.py` secara terpisah, di mana saya menuliskan skrip untuk membuat objek `Product` yang terkait dengan masing-masing pengguna. Di sini, saya mengimpor model `Product` dan `User`, lalu menggunakan `User.objects.get()` untuk mengambil masing-masing akun pengguna, kemudian membuat tiga entri produk untuk setiap akun dengan model `Product` yang sudah dihubungkan melalui `ForeignKey`.

Langkah terakhir, saya memodifikasi fungsi `create_product_entry` di `views.py` untuk memastikan setiap produk baru yang dimasukkan terhubung langsung dengan pengguna yang sedang login, sehingga data yang dimasukkan selalu terkait dengan pengguna aktif. Setelah semua langkah selesai, saya melakukan migrasi dan testing untuk memastikan fitur login, logout, registrasi, serta penghubungan produk dengan pengguna berjalan lancar.


## Tugas 5

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Ketika ada beberapa CSS selector yang diterapkan pada elemen HTML yang sama, maka prioritas pengambilan akan ditentukan oleh spesifitasnya dan urutan dalam file CSS (jika tingkat spesifitas sama). Berikut urutannya:
Inline Styles, dimana CSS yang ditulis langsung di dalam atribut HTML.  Inline Stylie ini akan mengoveride internal dan external style. (misalnya  `<div style="color: red;">`)
ID Selector, yaitu selector yang menggunakan ID (misalnya `#header`), memiliki prioritas lebih tinggi daripada class.
Class Selector, Attribute Selector, dan Pseudo-class merupakn selector yang menggunakan class (misalnya `.menu`), atribut (misalnya `[type="text"]`), atau pseudo-class (misalnya `:hover`).
Element Selector dan Pseudo-element, yaitu selector yang menggunakan nama elemen HTML (misalnya `div, p`) dan pseudo-element (misalnya `::before`, `::after`).
Universal Selector, yaitu selector yang menggunakan `*`, yang berarti memilih semua elemen.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design merupakan konsep krusial dalam pengembangan aplikasi web karena memungkinkan situs untuk menyesuaikan tampilan sesuai dengan berbagai ukuran layar, mulai dari desktop hingga smartphone. Dengan desain yang responsif, pengalaman pengguna menjadi lebih baik, aksesibilitas situs meningkat, dan peringkat SEO juga dapat diperbaiki. Contoh aplikasi yang telah menerapkan responsive design adalah X (Twitter), yang secara otomatis mengatur tampilannya berdasarkan perangkat yang digunakan, serta Facebook, yang antarmukanya beradaptasi dengan baik di berbagai perangkat. Sebaliknya, beberapa situs web lama yang hanya dirancang untuk desktop, seperti beberapa portal berita dan yang kita gunakan sebagai mahasiswa UI, yaitu SiakNG.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin, border, dan padding adalah elemen penting dalam CSS yang memengaruhi tata letak elemen. Margin adalah ruang di luar elemen yang menciptakan jarak antara elemen tersebut dengan elemen lainnya di sekitarnya. Sebagai contoh, kita dapat mengatur margin dengan `margin: 20px;`, yang memberikan jarak 20px di semua sisi. Border adalah garis yang mengelilingi elemen dan dapat memiliki berbagai gaya, seperti solid, dashed, atau dotted. Contohnya, kita bisa mengatur border dengan `border: 1px solid black;`, yang menghasilkan border hitam dengan ketebalan 1px. Sedangkan padding adalah ruang di dalam elemen, antara konten dan border. Kita bisa mengatur padding dengan `padding: 10px;`, yang memberikan ruang 10px di semua sisi konten.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox adalah model layout satu dimensi yang memudahkan pengaturan dan perataan elemen dalam satu baris atau kolom. Ini sangat membantu dalam menciptakan layout responsif, seperti menata tombol, card, atau navigasi, di mana elemen dapat tumbuh atau menyusut secara otomatis sesuai kebutuhan. Sementara itu, Grid Layout adalah model layout dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom. Grid sangat cocok untuk desain yang lebih kompleks, seperti layout majalah atau dashboard. Dengan memanfaatkan Flexbox dan Grid Layout, kita dapat menciptakan desain yang lebih fleksibel dan responsif.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Pertama-tama, saya menambahkan fungsi untuk mengedit dan menghapus produk di file views.py. Untuk fungsi edit_product, saya mengimplementasikan logika yang mengambil data produk berdasarkan ID-nya, lalu menampilkan form yang berisi informasi produk untuk diedit. Begitu juga dengan delete_product, saya menambahkan fungsi untuk menghapus produk dari database. Setelah selesai, saya menambahkan path untuk kedua fungsi ini di urls.py agar dapat diakses dari browser.

Selanjutnya, saya tidak perlu membuat desain card baru, karena saya sudah mendesain tampilan produk di styles.css sebelumnya. Desain ini sudah diterapkan baik untuk produk yang sudah ada maupun produk baru di halaman main. Saya memastikan bahwa tampilan produk yang ada sudah sesuai dengan ketentuan tugas sebelumnya dan memeriksa bahwa desain yang diterapkan tetap konsisten dan menarik.

Untuk setiap new produk yang ditambahkan admin, saya menambahkan dua button: satu untuk mengedit dan satu lagi untuk menghapus produk. Button-button ini saya letakkan di bawah informasi produk pada card. Saya memastikan bahwa tombol-tombol ini berfungsi dengan baik dengan menghubungkannya ke fungsi edit_item dan delete_item yang telah dibuat sebelumnya.

Terakhir, saya memastikan bahwa tampilan aplikasi responsif, khususnya pada ukuran mobile dan desktop. Saya memanfaatkan fitur grid dan flexbox dari Bootstrap5 agar elemen-elemen dalam halaman bisa menyesuaikan ukuran layar dengan baik. Navbar saya juga menggunakan Bootstrap's navbar component yang secara otomatis berubah menjadi tombol hamburger saat ditampilkan di perangkat mobile.


## TUGAS 6

# 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

JavaScript sangat bermanfaat dalam pengembangan aplikasi web karena memungkinkan halaman web menjadi interaktif dan responsif. Dengan JavaScript, kita bisa memperbarui konten halaman tanpa perlu me-reload seluruh halaman, membuat pengalaman pengguna lebih mulus. Misalnya, ketika menggunakan AJAX, JavaScript memungkinkan aplikasi web mengambil atau mengirim data ke server di latar belakang tanpa mengganggu aktivitas pengguna di halaman.


# 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

Fungsi `await` digunakan ketika kita memanggil `fetch()` dalam JavaScript untuk menangani proses asinkron. `await` memastikan bahwa kode akan menunggu hingga permintaan ke server selesai dan respons diterima sebelum melanjutkan ke baris berikutnya. Jika kita tidak menggunakan `await`, kode akan terus berjalan tanpa menunggu respons. Hal ini dapat menyebabkan hasil yang tidak lengkap   karena data belum diterima saat kode dilanjutkan.

# 3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST?

Penggunaan decorator `csrf_exempt` pada view yang menangani AJAX POST bertujuan untuk menonaktifkan proteksi CSRF (Cross-Site Request Forgery). Django secara default melindungi aplikasi dari serangan CSRF, tetapi untuk request AJAX tertentu. Jadi, kita perlu menonaktifkan proteksi ini agar request bisa diterima tanpa menimbulkan error. Selain itu,  penting untuk memastikan bahwa request tetap aman dengan mekanisme proteksi lainnya.

# 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data input pengguna di backend sangat penting meskipun ada validasi di frontend. Jika hanya mengandalkan frontend, user yang berniat jahat bisa mem-bypass validasi tersebut dengan mudah menggunakan alat tertentu. Jadi, backend juga harus membersihkan dan memvalidasi data untuk memastikan keamanan dan integritas aplikasi, mencegah serangan seperti XSS (Cross-Site Scripting).

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Pertama-tama, saya mengimplementasikan AJAX GET untuk mengambil data produk yang hanya milik pengguna yang sedang login. Di sini, saya membuat fungsi `getProductEntries()` yang mengambil data produk dari server dalam format JSON. Setelah itu, saya menggunakan fungsi `refreshProductEntries()` untuk menampilkan data produk secara dinamis tanpa harus melakukan reload halaman. Jadi, ketika ada perubahan, produk-produk yang muncul di halaman hanya milik pengguna yang sedang login.

Untuk AJAX POST, saya membuat tombol yang membuka modal berisi form untuk menambah produk baru. Saat tombol ditekan, modal terbuka dan ketika form di-submit, data produk dikirim ke server menggunakan fetch (tanpa reload). Di sinilah fungsi `addProductEntry()` berperan. Fungsi ini mengirim data secara asinkron ke path `/create-ajax/`, yang terhubung ke fungsi view `add_product_entry_ajax`. Fungsi view ini akan menerima data dari form dan menyimpannya ke dalam database.

Sebelum data produk dikirim ke server, di fungsi `addProductEntry()`, saya melakukan validasi menggunakan DOMPurify untuk membersihkan input dari potensi XSS. Jadi, misalnya jika ada input yang berbahaya di nama produk, deskripsi, kategori, atau review, produk tersebut tidak akan ditambahkan, dan saya menampilkan pesan alert yang mengatakan "Produk mengandung input yang berbahaya dan tidak akan ditambahkan.PAHAM!" Jika semua input aman, data akan dikirim ke server.

Selain validasi XSS di frontend menggunakan DOMPurify pada fungsi `addProductEntry()`, saya juga melakukan pembersihan input di backend dengan menggunakan `strip_tags`. Ini diterapkan baik saat menambahkan maupun mengedit produk.

Setelah produk berhasil ditambahkan, modal secara otomatis ditutup, form di-reset, dan produk baru langsung ditampilkan di halaman tanpa reload, berkat pemanggilan fungsi `refreshProductEntries()`. Jika ada masalah dalam proses penambahan produk, saya menampilkan pesan error yang sesuai, seperti "Gagal menambahkan produk."

Dengan langkah ini, saya memastikan bahwa penambahan produk di BambooShop berjalan lancar, aman dari potensi serangan XSS, dan produk baru bisa langsung terlihat tanpa perlu melakukan reload halaman.
