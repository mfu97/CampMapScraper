import schedule
import time
from src.main import main

def run_job():
    print("Scraper başlıyor...")
    main()

schedule.every().day.at("03:00").do(run_job)

print("Zamanlayıcı başlatıldı. Ctrl+C ile durdurabilirsin.")
while True:
    schedule.run_pending()
    time.sleep(1)