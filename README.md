# Alx_CapstoneProject
A backend API for a Habit Tracking Application that helps users build and maintain habits through reminders, streak tracking, and calendar integration.
This project is part of my Capstone Project for the ALX Backend course.

📌 Table of Contents

🚀 Project Overview

🗄️ Database Design (ERD)

📡 API Endpoints

🛠️ Tech Stack

🧪 Installation & Setup

📂 Project Structure

📈 Next Steps

📚 Progress Report (Part 3)

⚠️ Challenges & Solutions

📂 Repository

👤 Author

🚀 Project Overview

The Habit Tracker App helps users form and maintain daily habits through an intuitive, data-driven backend.

✨ Key Features

✅ Create, update, and delete personal habits

⏰ Set custom reminders for each habit

🔥 Track streaks and habit completion history

📅 Sync with calendar to align habits with daily plans

📊 View progress analytics over time

🗄️ Database Design (ERD)

Here’s the high-level Entity Relationship Diagram (ERD) for the project:

(Replace the link with the actual ERD image from your Google Doc or diagram tool)

📡 API Endpoints

Below is a summary of the main API endpoints:

Endpoint	Method	Description	Auth Required
/api/users/register/	POST	Register a new user	❌
/api/users/login/	POST	Authenticate user & get token	❌
/api/habits/	GET	List all habits for the logged-in user	✅
/api/habits/	POST	Create a new habit	✅
/api/habits/<id>/	GET	Retrieve a specific habit	✅
/api/habits/<id>/	PUT	Update a habit	✅
/api/habits/<id>/	DELETE	Delete a habit	✅
/api/reminders/	POST	Create a reminder for a habit	✅
/api/streaks/	GET	View current streaks and progress	✅
/api/calendar/sync/	POST	Sync habits with an external calendar	✅
🛠️ Tech Stack

Backend: Django, Django REST Framework

Database: PostgreSQL / MySQL

Auth: JWT (JSON Web Tokens)

Calendar Sync: Google Calendar API (optional)

Background Jobs: Celery + Redis (for reminders)

🧪 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/habit-tracker-api.git
cd habit-tracker-api

2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/habit_db

4️⃣ Run Migrations & Start the Server
python manage.py migrate
python manage.py runserver


API is now live at:
👉 http://127.0.0.1:8000/api/

📂 Project Structure
habit-tracker-api/
├── habits/               # Habit models, serializers, views
├── users/                # User auth and profile management
├── reminders/            # Reminder scheduling logic
├── streaks/              # Streak tracking and history
├── calendar/             # Calendar sync integration
├── manage.py
└── README.md

📈 Next Steps

 Implement automated email/notification reminders

 Add progress analytics dashboard

 Deploy the backend to Render or Heroku

 Write unit and integration tests for all endpoints

📚 Progress Report (Part 3)

✅ Repository initialized and pushed to GitHub
✅ ERD and API endpoints designed and documented
✅ Core models and initial endpoints implemented

🎯 Next Week’s Focus:

Implement reminder scheduling

Build streak logic

Integrate Google Calendar API

⚠️ Challenges & Solutions
Challenge	Solution
Designing a scalable schema	Created a normalized ERD with clear relationships
Implementing reminder scheduling	Plan to use Celery with Redis for async tasks
Authentication & security	Integrated JWT-based authentication
📂 Repository

🔗 GitHub Repo: https://github.com/yourusername/habit-tracker-api

👤 Author

Ian Ndambuki
📧 Email: indumia2@gmail.com

🐙 GitHub: yourusername

💡 Final Note

This project is part of the ALX Backend Capstone Project, focusing on building real-world backend applications from scratch. It’s designed to be extendable and production-ready.
