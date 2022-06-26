# Just some thesis stuffs

## Changelog

**Jun 3, 2022**

- Git init
- New monitoring form page (front end only)

**Jun 5, 2022**

- Frontend kurang lebih udah semua, kurang chart aja
- Mulai search service

**Jun 7, 2022**

- Search service API udah
- Problem : nggak ada web yang konsisten struktur htmlnya, jadinya kadang nggak ngasih hasil

**Jun 10, 2022**

- Konsep search service ganti : awalnya di scrape dari sumber web terus hasilnya disimpan di database, scrapernya nggak usah dibikinin API, ke hasil database nya aja
- Program scrapernya udah

**Jun 11, 2022**

- Database & API disease info udah

## Services

### Frontend

Made with svelte, frontend buat web. Ada di port 3000

### API Gateway (belom buat)

Rencananya pakai KrakenD

### NLP (belom buat)

Dapet input dari halaman chat, buat tau perintah dari isi chatnya apa

### Questionare

Aka monitoring form. Made with FastAPI. Ada di port 8000. Alur kerjanya:

- Dokter : bisa buat form monitoring dan liat hasil di halaman admin
- Pasien : bisa subscribe ke form buat dapet notif dan isi form lewat halaman chat

### Expert System

Made with FastAPI, cuma bisa ditambah dari kodingan. Ada di port 8001

### Disease Info

Made with FastAPI di port 8002.

**(v1)** Input query dari chat yang udah ngelewatin service NLP, lewat google search cari dari url whitelist

**(v2)** Ada database isinya hasil scrape dari web, NLP nanti yang ngefilter user mau dapat informasi apa

Sources:

- Mayoclinic : Overview, symptoms, when to see doctor, causes, risk factors, complication, prevention
