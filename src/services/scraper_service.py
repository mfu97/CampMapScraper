import requests
from src.models.campground import Campground

class ScraperService:
    @staticmethod
    def fetch_raw_data(url: str) -> list[dict]:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("data", [])

    @staticmethod
    def parse_data(raw_data: list[dict]) -> list[Campground]:
        campgrounds = []

        for i, item in enumerate(raw_data):
            try:
                # 'attributes' içindeki veriyi dışarı çıkartıyoruz (flatten)
                attributes = item.get("attributes", {})
                flat_item = {
                    **item,           # id, type, links
                    **attributes      # name, latitude, longitude vs.
                }
                # Pydantic model ile doğrula
                campground = Campground(**flat_item)
                campgrounds.append(campground)
            except Exception as e:
                print(f"[{i}] Doğrulama hatası: {e}")

        return campgrounds