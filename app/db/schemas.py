from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str
    population: int


class CountryCreate(CountryBase):
    pass


class CountryList(CountryBase):
    id: int

    class Config:
        orm_mode = True
