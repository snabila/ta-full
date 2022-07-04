# Final year project stuffs

## Services

### Frontend

Made with svelte, frontend buat web. Ada di port 3000

### API Gateway

CORS masih error, tapi ada kemungkinan karena pake localhost

### Chatbot

Pakai Rasa Framework, masih belom dimasukkin docker, jadi run sendiri pake:

    rasa run --enable-api --cors="*" --port 5005 --debug

Buat jalanin actions server:

    rasa run actions

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
