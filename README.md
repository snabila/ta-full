## Final year project stuffs

### Desc

Repo ini isinya program tugas akhir kuliah. Isinya sistem telekonsultasi medis dengan chatbot. Konsultasi medis itu biasanya dilakukan dengan tujuan: [(source)](https://www.docdoc.com/id/info/procedure/general-consultation)

1. Mengambil tindakan pencegahan bagi pasien yang memiliki faktor resiko
2. Mendapatkan diagnosa atas gejala
3. Pemeriksaan rutin
4. Menilai kembali resiko pasien terhadap beberapa kondisi medis

Program yang dibuat ini diharapkan bisa membantu mencapai 3 tujuan pertama tersebut dengan:

1. Fitur pencarian informasi penyakit ([service disease info](#disease-info)) dimana salah satu kolom tabel nya ada informasi untuk pencegahan/prevention
2. Bisa menampung model sistem pakar ([service expert system](#expert-system))
3. Bantu dokter melakukan monitoring sederhana ([service monitoring](#monitoring))

Framework, tools, library yang digunain diantaranya:

1. [Rasa](https://rasa.com/). Framework chatbot Python.
2. [ExpressJS](https://expressjs.com/). Web framework Javascript.
3. [FastAPI](https://fastapi.tiangolo.com/). Web framework Python buat service yang butuh buat pakai library Python, tapi akhirnya kebablasan pake ini terus karena docs nya yang dibuat otomatis.
4. [KrakenD](https://www.krakend.io/). API gateway biar endpoint yang di expose si krakend nya aja
5. [Docker Compose](https://docs.docker.com/compose/). Buat manage container, aku pribadi cuma biar ngerunnya langsung sekalian aja. Definitely ada fungsi lainnya yang penting tapi belum kupelajarin.
6. [SvelteKit](https://kit.svelte.dev/). Frontend web framework, waktu itu dipakai karena saya nggak sanggup speedrun belajar React.
7. [Tailwind](https://tailwindcss.com/). Framework CSS.

### To Do List

- [ ] Cari cara cancel/skip form Rasa dari custom action atau validasi slot
- [ ] Error handling
  - [ ] Pilih isi form tapi belum terdaftar di kode tsb
  - [ ] Pilih isi form tapi belum terdaftar di manapun
  - [x] Pilih hapus form tapi belum terdaftar di kode tsb
  - [ ] Pilih hapus form tapi belum terdaftar di manapun

## Services

Buat run semuanya bisa

    docker-compose up

tamahin flag `-d` kalau nggak mau lihat log.

### Frontend

Proses autentikasi masih banyak yang di proses di frontendnya, which I think can be moved to gateway, tapi nggak sempet kemaren. Struktur website nya kurang lebih gini

    ├──Homepage (chatbot)          - All roles
    └──Admin                       - Dokter
        ├──Dashboard
        ├──Monitoring
        │   ├──Index
        │   ├──Individual
        │   └──New & Edit
        ├──Pasien
        │   ├──Index
        |   └──Individual
        └──Respon

Halaman respon cuma buat liat indeks respon terbaru aja, buat detail responnya sendiri diliat di halaman masing-masing pasien.

### API Gateway

CORS masih error, tapi ada kemungkinan karena pakai localhost

Catatan untuk penggunaan KrakenD:

- Nggak bisa gabungin lebih dari satu _non-safe methods_, sebenernya aku juga belom research lagi yang lain bisa atau nggak
- Designer GUI nya agak membingungkan pertama kali liatnya, perlu sholat tobat dulu biar diarahin ke settings yang diinginkan wkwk

Alternatif lainnya ada [Tyk](https://tyk.io/) dan [Kong](https://konghq.com/), komunitas mereka lebih besar, jadi lebih banyak resource buat belajarnya. Bisa diubah aja gateway nya kalau mau.

### Chatbot

Masih belom dimasukkin docker, jadi run sendiri pake:

    rasa run --enable-api --cors="*" --port 5005 --debug

Buat jalanin actions server:

    rasa run actions

Alur percakapannya masih kaku banget and prone to errors kalau keluar dari alur. Forms yang udah dibuat sebenernya perlu diperbaikin lagi tapi kemarin nggak sempet.

Error handling nya masih jelek, terutama di fungsi monitoring:

1. Kalau user pilih isi tapi belum terdaftar ke manapun >> dia bakal ngulang 'belum terdaftar' dua kali, stuck di `monit_form_2` dan `monit_isi_form`
2. Kalau user pilih isi tapi belum terdaftar di kode tsb >> stuck di nunggu input `monit_isi_loop`, harus ada input lagi dulu baru dia nanya `utter_bantu_lagi`
3. Kalau user pilih hapus tapi belum terdaftar ke manapun >> stuck di nunggu input `monit_form_2`

### Monitoring

Alur kerjanya:

- Dokter : bisa buat form monitoring dan liat hasil di halaman admin
- Pasien : bisa subscribe ke form dan isi form lewat halaman chat

Kemarin mau nambahin fitur notifikasi tapi nggak sempet.

### Expert System

Buat load model sistem pakar, buat modelnya di aplikasi sendiri nggak usah dimasukin ke server. Kemarin pertanyaannya masih hardcode di utter Rasa-nya. Bagusnya kedepannya disimpen di database sendiri aja, jadi Rasa ambil pertanyaannya dari database (liat custom action monitoring).

### Disease Info

**(v1)** Input query dari chat yang udah ngelewatin service NLP, lewat google search cari dari url whitelist. \
**(v2)** Ada database isinya hasil scrape dari web, chatbot nanti yang tanya user mau dapat informasi apa.

Sumber:

- Mayoclinic (`diseaseinfo.db`) : Overview, symptoms, when to see doctor, causes, risk factors, complication, prevention.

Kemarin lihat hasilnya sekilas dan ada yang ke skip, ini juga masih terjemahan mesin jadi masih banyak yang rada ngaco terjemahannya.

Some suggestions kalau mau nerjemahin situs Bahasa Inggris:

- Pakai database yang gampang buat di export ke csv kayak SQL
- Masukin csv nya ke Google Sheets, mereka ada rumus buat manggil Google Translate
- Kalau udah selesai import lagi ke database
