from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassOut(BaseModel):
    id: int
    name: str
    instructor: str
    datetime_ist: datetime
    available_slots: int

    class Config:
        orm_mode = True

class BookingIn(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BookingIn):
    id: int

    class Config:
        orm_mode = True
