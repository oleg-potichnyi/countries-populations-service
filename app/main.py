from app.db.engine import SessionLocal
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import models, crud, schemas


app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/get_data", response_model=schemas.CountryList)
def get_data(
    country_list: schemas.CountryCreate,
    db: Session = Depends(get_db),
):
    return crud.get_country_data(db=db, country_list=country_list)


@app.get("/print_data", response_model=list[schemas.CountryList])
def print_data(db: Session = Depends(get_db)):
    return crud.print_summary_data(db=db)
