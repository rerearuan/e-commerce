TUGAS INDIVIDU PBP


TUGAS 2
Jawaban dari pertanyaan tugas 2:
1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?

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

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Client Request ->  URL Routing (urls.py) -> View Function (views.py) -> Model (models.py) -> Database -> HTML Template -> Client Response

Pada bagan alur request dan response di aplikasi Django, urls.py berfungsi sebagai pengatur rute, menentukan bagaimana URL yang diminta oleh client dipetakan ke fungsi view yang tepat di views.py. Fungsi view tersebut memproses request dan, jika diperlukan, berinteraksi dengan models.py untuk mengambil atau memanipulasi data dari database. Setelah data diproses, fungsi view mengirimkan data tersebut ke berkas HTML Template untuk dirender menjadi format yang dapat ditampilkan di browser. HTML Template ini kemudian dipergunakan untuk menyusun respons akhir yang dikirim kembali ke client.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah alat penting dalam pengembangan perangkat lunak karena ia mengelola versi kode dengan efisien. Dengan Git, pengembang dapat melacak perubahan kode secara rinci, yang membantu mereka memahami bagaimana dan kapan kode berubah seiring waktu. Git memudahkan kolaborasi dengan memungkinkan beberapa pengembang bekerja pada proyek yang sama secara bersamaan melalui sistem branching dan merging. Ini juga memungkinkan rollback atau pengembalian ke versi sebelumnya jika terjadi kesalahan, serta menyediakan sistem yang transparan untuk mengelola dan mengintegrasikan perubahan dari berbagai kontributor.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dijadikan pilihan untuk pembelajaran awal karena kemudahan penggunaannya dan struktur yang jelas. Framework ini mengintegrasikan berbagai fitur penting secara default, seperti otentikasi dan manajemen basis data, yang memungkinkan pemula fokus pada logika aplikasi daripada harus membangun dari nol. Dokumentasinya yang lengkap dan komunitas yang aktif mempermudah proses belajar, sementara struktur arsitektur Model-View-Template (MVT) membantu pemula memahami bagaimana aplikasi web bekerja secara sistematis.

5. Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM atau Object-Relational Mapping karena menghubungkan objek Python dengan tabel-tabel di database. ORM memungkinkan pengembang untuk berinteraksi dengan data menggunakan sintaks Python yang familiar, daripada menulis query SQL yang rumit. Ini membuat pengelolaan data lebih intuitif dan terintegrasi langsung dengan kode aplikasi, memungkinkan pengembang untuk menangani data sebagai objek dan mengelola hubungan antar data dengan cara yang lebih alami dan mudah dipahami.

