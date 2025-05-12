from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from src.db.database import Base

class CampgroundORM(Base):
    __tablename__ = "campgrounds"

    id = Column(String, primary_key=True, index=True)
    type = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    region_name = Column(String)
    administrative_area = Column(String, nullable=True)
    nearest_city_name = Column(String, nullable=True)
    accommodation_type_names = Column(ARRAY(String), default=[])
    bookable = Column(Boolean, default=False)
    camper_types = Column(ARRAY(String), default=[])
    operator = Column(String, nullable=True)
    photo_url = Column(String, nullable=True)
    photo_urls = Column(ARRAY(String), default=[])
    photos_count = Column(Integer, default=0)
    rating = Column(Float, nullable=True)
    reviews_count = Column(Integer, default=0)
    slug = Column(String, nullable=True)
    price_low = Column(Float, nullable=True)
    price_high = Column(Float, nullable=True)
    availability_updated_at = Column(DateTime, nullable=True)
