# 🏋️‍♂️ Fitness Studio Booking API

A simple Booking API built using **FastAPI** and **SQLModel** for a fictional fitness studio that offers classes like Yoga, Zumba, and HIIT.

## 📌 Features

- List available fitness classes
- Book a class (validates available slots)
- Get bookings by client email
- Timezone-aware (IST)
- SQLite database using SQLModel

## 🗂️ Project Structure
```bash 
fitness_booking/
├── app/
│ ├── main.py # FastAPI routes
│ ├── models.py # SQLModel models
│ ├── database.py # DB engine and session
│ 
├── requirements.txt
├── seed.py # Seed script for test data
├── .gitignore
├── README.md

```


## 🚀 Setup Instructions

### 1. Clone the repo / download zip

```bash
git clone https://github.com/rubankumarsankar/fitness_booking_api.git
cd fitness-booking-api
```


###2. Create virtual environment & install dependencies
```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

###3. Seed the database
# Run this from the root folder

```bash

python seed.py

```
###4. Start the API server

```bash

uvicorn app.main:app --reload

```

##🧪 Sample API Usage
###🔍 View Classes

```bash

curl http://127.0.0.1:8000/classes

```


### Book a Class
```bash

curl -X POST http://127.0.0.1:8000/book \
  -H "Content-Type: application/json" \
  -d '{"class_id": 1, "client_name": "John", "client_email": "john@example.com"}'

```

###📥 View Bookings by Email

```bash

curl "http://127.0.0.1:8000/bookings?email=john@example.com"

```

###🧠 Bonus Notes
```bash
All class times are stored in IST (Asia/Kolkata) timezone.

The seed script creates Yoga, Zumba, and HIIT sample classes.

Data is persisted in a local fitness.db SQLite file.
```