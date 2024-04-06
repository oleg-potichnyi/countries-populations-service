from app.db.engine import Base
from sqlalchemy import Column, Integer, String, BigInteger


class DBCountry(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    population_2023 = Column(BigInteger)
    continental_region = Column(String(255))
