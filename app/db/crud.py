from fastapi import requests
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db import models
from app.db.engine import SessionLocal
from app.db.models import DBCountry


def get_country_data(db: Session):
    url = (
        "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    session = SessionLocal()
    country = DBCountry(name="Country Name", population=population)
    session.add(country)
    session.commit()
    session.close()
    return db.query(models.DBCountry).all()


def print_summary_data(db: Session | Session) -> None:
    session = SessionLocal()
    for region in regions:
        total_population = session.query(func.sum(DBCountry.population)).filter_by(region=region).scalar()
        largest_country = (
            session.query(DBCountry).filter_by(region=region).order_by(DBCountry.population.desc()).first()
        )
        smallest_country = (
            session.query(DBCountry).filter_by(region=region).order_by(DBCountry.population.asc()).first()
        )
        print(f"Region: {region}")
        print(f"Total Population: {total_population}")
        print(f"Largest Country: {largest_country.name}, Population: {largest_country.population}")
        print(f"Smallest Country: {smallest_country.name}, Population: {smallest_country.population}")
        session.close()


print_summary_data()
