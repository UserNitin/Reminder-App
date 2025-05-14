# 🕑 Django Reminder App

A simple Django web application that lets users create and store reminders with a custom message, date, time, and delivery method (SMS or Email). It provides both a user-friendly web interface and a REST API endpoint to save reminders to the database.

## 🚀 Features
- Create reminders with message, date, time, and delivery method
- UI built using Django templates
- REST API endpoint to store reminders (no delivery logic included)

## 📦 Usage
1. Clone the repo:  
   `git clone https://github.com/UserNitin/Reminder-App.git && cd Reminder-App`

2. Create a virtual environment and activate it:  
   `python -m venv venv && venv\Scripts\activate` (Windows)

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Run migrations:  
   `python manage.py migrate`

5. Start the server:  
   `python manage.py runserver`  
   Access the app at `http://127.0.0.1:8000/`

## 🧪 API Endpoint
- **POST** `/reminders/api/create/`  
  JSON Body:
  ```json
  {
    "message": "Take medicine",
    "date": "2025-05-15",
    "time": "10:00",
    "delivery_method": "email"
  }
