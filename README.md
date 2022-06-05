# Tugas Akhir

## Changelog

**Jun 3, 2022**

- git init
- new monitoring form page (front end only)

**Jun 5, 2022**

- Frontend kurang lebih udah semua, kurang chart aja
- Mulai search service

## Services

### Frontend

Made with svelte, frontend buat web. Ada di port 3000

### API Gateway (belom buat)

Rencananya pakai KrakenD, jangankan buat, baca materialnya aja belom :)

### NLP (belom buat)

Dapet input dari halaman chat, buat tau perintah dari isi chatnya apa

### Questionare

aka monitoring form. Made with FastAPI. Ada di port 8000. Alur kerjanya:

- Dokter : bisa buat form monitoring dan liat hasil di halaman admin
- Pasien : bisa subscribe ke form buat dapet notif dan isi form lewat halaman chat

### Expert System

Made with FastAPI, cuma bisa ditambah dari kodingan _(last update Jun 3, 2021)_. Ada di port 8001

### Search Scraper (belom di convert ke API)

Made with FastAPI di port 8002. Input query dari chat yang udah ngelewatin service NLP
