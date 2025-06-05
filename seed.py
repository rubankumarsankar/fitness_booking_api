from sqlmodel import SQLModel, Session
from app.models import Class
from app.database import engine
from datetime import datetime
import pytz

def seed_data():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)

    classes = [
        Class(name="Yoga", instructor="Alice", datetime_ist=now, available_slots=5),
        Class(name="Zumba", instructor="Bob", datetime_ist=now, available_slots=3),
        Class(name="HIIT", instructor="Carol", datetime_ist=now, available_slots=2),
    ]

    with Session(engine) as session:
        for c in classes:
            session.add(c)
        session.commit()

if __name__ == "__main__":
    seed_data()
