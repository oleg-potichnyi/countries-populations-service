from app.db.crud import get_country_data
from app.db.engine import SessionLocal


def get_data() -> None:
    try:
        db = SessionLocal()
        get_country_data(db)
    finally:
        db.close()


if __name__ == "__main__":
    get_data()
