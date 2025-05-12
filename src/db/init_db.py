from src.db.database import Base, engine
from src.models.campground_orm import CampgroundORM

def init_db():
    Base.metadata.create_all(bind=engine)
