from pydantic import BaseModel


class SchoolBase(BaseModel):
    fullname: str
    city: str
    state: str
    country: str
