from app.db.crud import print_summary_data
from app.db.engine import SessionLocal


def print_data() -> None:
    try:
        db = SessionLocal()
        print_summary_data(db)
    finally:
        db.close()


if __name__ == "__main__":
    print_data()
