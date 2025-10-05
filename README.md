# Alx_CapstoneProject
🧠 Habit Tracker API – Capstone Project

A backend API for a Habit Tracking Application that helps users build and maintain habits through reminders, streak tracking, and calendar integration. This project is part of my Capstone Project for the ALX Backend course.

🚀 Project Overview

The Habit Tracker App is designed to help users create, manage, and track their daily habits effectively.
Key features include:

✅ Create and manage personal habits.

⏰ Set reminders for habits at specific times.

🔥 Track daily streaks and progress.

📅 Calendar integration to align habits with daily plans.

📊 View progress analytics and habit history.

This backend is built with Django REST Framework and follows a clean, modular architecture for scalability and maintainability.

🗄️ Database Design (ERD)

Below is the Entity Relationship Diagram (ERD) representing the database structure:


(Replace the link with the actual ERD image URL from your Google Doc or diagram tool)

📡 API Endpoints

Here’s an overview of the core API endpoints the backend exposes:

Endpoint	Method	Description	Auth Required
/api/users/register/	POST	Register a new user	❌
/api/users/login/	POST	Authenticate user & get token	❌
/api/habits/	GET	List all habits for the authenticated user	✅
/api/habits/	POST	Create a new habit	✅
/api/habits/<id>/	GET	Retrieve details of a specific habit	✅
/api/habits/<id>/	PUT	Update a habit	✅
/api/habits/<id>/	DELETE	Delete a habit	✅
/api/reminders/	POST	Create a reminder for a habit	✅
/api/streaks/	GET	View current streaks and progress	✅
/api/calendar/sync/	POST	Sync habits with external calendar	✅
🛠️ Tech Stack

Backend: Django, Django REST Framework

Database: PostgreSQL (or MySQL)

Authentication: JWT (JSON Web Tokens)

Calendar Sync: Google Calendar API (optional extension)

Other Tools: Celery & Redis (for background reminders)

🧪 Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/habit-tracker-api.git
cd habit-tracker-api


Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt


Set up your .env file:

SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/habit_db


Apply migrations and run the server:

python manage.py migrate
python manage.py runserver


Access the API at:
👉 http://127.0.0.1:8000/api/

🧰 Project Structure
habit-tracker-api/
├── habits/              # Habit app (models, views, serializers)
├── users/               # User authentication & profiles
├── reminders/           # Reminder and notification logic
├── streaks/             # Streak tracking logic
├── calendar/            # Calendar integration (optional)
├── manage.py
└── README.md

📈 Next Steps

 Implement automated email/notification reminders.

 Add analytics dashboard for user habit insights.

 Deploy to a cloud platform (Render/Heroku).

 Add test coverage for all endpoints.

📚 Progress Report (Part 3)

✅ Project initialized and GitHub repo set up.

✅ ERD and API endpoints designed.

✅ Core models and basic endpoints implementation started.

Next week goals: Implement reminder scheduling, streak logic, and integrate calendar API.

📌 Challenges & Solutions
Challenge	Solution
Designing a scalable database schema	Created a normalized ERD with clear relationships
Reminder scheduling logic	Plan to use Celery with Redis for background tasks
Authentication handling	Implemented JWT-based auth for secure access
📂 Repository

🔗 GitHub: https://github.com/yourusername/habit-tracker-api

👤 Author

Ian Ndambuki
📧 Email: indumia2@gmail.com

💼 LinkedIn
 | 🐙 GitHub
