from sqlalchemy.orm import Session
from src.models.campground import Campground
from src.models.campground_orm import CampgroundORM

class CampgroundRepository:
    def __init__(self, session):
        self.session = session

    def save(self, campground: Campground):
        existing = self.session.query(CampgroundORM).filter_by(id=campground.id).first()

        if existing:
            print(f"Kayıt zaten var, atlanıyor: {campground.id}")
            return False

        orm_obj = CampgroundORM(
            id=campground.id,
            name=campground.name,
            latitude=campground.latitude,
            longitude=campground.longitude,
            region_name=campground.region_name,
            administrative_area=campground.administrative_area,
            nearest_city_name=campground.nearest_city_name,
            accommodation_type_names=campground.accommodation_type_names,
            bookable=campground.bookable,
            camper_types=campground.camper_types,
            operator=campground.operator,
            photo_url=str(campground.photo_url) if campground.photo_url else None,
            photo_urls=[str(url) for url in campground.photo_urls],
            photos_count=campground.photos_count,
            rating=campground.rating,
            reviews_count=campground.reviews_count,
            slug=campground.slug,
            price_low=campground.price_low,
            price_high=campground.price_high,
            availability_updated_at=campground.availability_updated_at,
        )

        self.session.add(orm_obj)
        self.session.commit()
        print(f"✅ Yeni kayıt eklendi: {campground.id}")
        return True