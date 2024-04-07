import requests
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.models import DBCountry
from bs4 import BeautifulSoup


def get_country_data(db: Session) -> None:
    url = (
        "https://en.wikipedia.org/w/index.php?"
        "title=List_of_countries_by_population_(United_Nations)"
        "&oldid=1215058959"
    )
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    for row in soup.find("table", class_="wikitable").find_all("tr")[2:]:
        columns = row.find_all("td")
        name = columns[1].text.strip()
        population_2023 = int(columns[3].text.strip().replace(",", ""))
        continental_region = columns[5].text.strip()

        country = DBCountry(
            name=name,
            population_2023=population_2023,
            continental_region=continental_region,
        )
        db.add(country)
    db.commit()


def print_summary_data(db: Session) -> None:
    regions = db.query(DBCountry.continental_region).distinct().all()
    for region in regions:
        total_population = (
            db.query(func.sum(DBCountry.population_2023))
            .filter_by(continental_region=region)
            .scalar()
        )
        largest_country = (
            db.query(DBCountry)
            .filter_by(continental_region=region)
            .order_by(DBCountry.population_2023.desc())
            .first()
        )
        smallest_country = (
            db.query(DBCountry)
            .filter_by(continental_region=region)
            .order_by(DBCountry.population_2023.asc())
            .first()
        )
        print(f"Region: {region}")
        print(f"Total Population: {total_population}")
        print(
            f"Largest Country: {largest_country.name}, "
            f"Population: {largest_country.population}"
        )
        print(
            f"Smallest Country: {smallest_country.name}, "
            f"Population: {smallest_country.population}"
        )
