from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select, Session
from app.models import Class, Booking
from app.database import get_session
from typing import List

app = FastAPI()

@app.get("/classes", response_model=List[Class])
def get_classes(session: Session = Depends(get_session)):
    return session.exec(select(Class)).all()

@app.post("/book")
def book_class(booking: Booking, session: Session = Depends(get_session)):
    class_obj = session.get(Class, booking.class_id)

    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    if class_obj.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    class_obj.available_slots -= 1
    session.add(booking)
    session.commit()
    return {"message": "Booking successful", "booking_id": booking.id}

@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: str, session: Session = Depends(get_session)):
    bookings = session.exec(select(Booking).where(Booking.client_email == email)).all()
    return bookings
