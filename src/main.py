from src.db.database import SessionLocal
from src.db.init_db import init_db
from src.services.scraper_service import ScraperService
from src.repositories.campground_repository import CampgroundRepository

URL = "https://thedyrt.com/api/v6/locations/search-results?filter%5Bsearch%5D%5Bdrive_time%5D=any&filter%5Bsearch%5D%5Bair_quality%5D=any&filter%5Bsearch%5D%5Bstart_date%5D=2025-05-13&filter%5Bsearch%5D%5Bend_date%5D=2025-05-20&filter%5Bsearch%5D%5Bavailable%5D=1&filter%5Bsearch%5D%5Belectric_amperage%5D=any&filter%5Bsearch%5D%5Bmax_vehicle_length%5D=any&filter%5Bsearch%5D%5Bprice%5D=any&filter%5Bsearch%5D%5Brating%5D=any&filter%5Bsearch%5D%5Bbbox%5D=-123.068%2C-9.559%2C-70.07%2C69.092&sort=recommended&page%5Bnumber%5D=1&page%5Bsize%5D=500"

def main():
    print("DB başlatılıyor...")
    init_db()

    print("Veri çekiliyor...")
    raw = ScraperService.fetch_raw_data(URL)
    
    campgrounds = ScraperService.parse_data(raw)

    session = SessionLocal()
    repo = CampgroundRepository(session)

    print("Veritabanına yazılıyor...")

    added_count = 0

    for cg in campgrounds:
        result = repo.save(cg)
        if result:
            added_count += 1

    print(f"✅ {added_count} yeni kayıt eklendi.")

if __name__ == "__main__":
    main()
