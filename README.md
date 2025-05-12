# 🏕️ The Dyrt Campground Scraper

Bu proje, [The Dyrt](https://thedyrt.com/) haritası üzerinden kamp alanlarını otomatik olarak toplayarak PostgreSQL veritabanına kaydeder. Python ile yazılmıştır ve Docker üzerinden kolayca çalıştırılabilir. 

## 🚀 Özellikler

- The Dyrt API üzerinden kamp verilerini toplar
- Pydantic ile veri doğrulama yapar
- SQLAlchemy ile PostgreSQL’e kayıt işlemi yapar
- Aynı kayıtları tekrar eklemeyi engeller
- Cron benzeri zamanlayıcı ile düzenli veri güncellemesi yapılabilir
- Docker ile çalıştırılabilir yapı


## ⚙️ Kurulum

### 1. Depoyu Klonla
git clone https://github.com/kullaniciadi/case_study.git
cd case_study

### 2. Ortam Değişkenlerini Tanımla
Proje kök dizinine .env dosyası oluştur ve aşağıdaki satırları ekle:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=campgrounds
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

### 3. Docker ile Başlat
Projeyi build edip başlatmak için:
docker compose up --build

Scraper konteyneri başlatıldığında main.py dosyasını çalıştırarak verileri çeker ve veritabanına kaydeder.

⏱️ Cron-like Scheduler
Otomatik veri güncellemesi yapmak istersen, şu komutu kullanabilirsin:
python -m src.jobs.scheduler
Bu yapı, APScheduler ile düzenli olarak veri çekilmesini sağlar.

🧪 Lokal Test
Projenin ana scriptini yerelde çalıştırmak için:
python -m src.main

📌 Gelecek Geliştirmeler
Gelişmiş loglama
Multithreading ya da async yapı kullanarak scraper’ın performansını artırma
Enlem/boylam verisinden adres çıkarımı
