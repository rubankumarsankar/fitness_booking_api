from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Class(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    instructor: str
    datetime_ist: datetime
    available_slots: int


class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    class_id: int
    client_name: str
    client_email: str
