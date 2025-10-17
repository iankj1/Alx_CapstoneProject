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

| Endpoint                    | Method     | Description                                   | Auth Required |
| --------------------------- | ---------- | --------------------------------------------- | ------------- |
| `/api/users/register/`      | **POST**   | Register a new user                           | ❌             |
| `/api/users/login/`         | **POST**   | Authenticate user and return a JWT token      | ❌             |
| `/api/users/profile/`       | **GET**    | Retrieve the logged-in user’s profile         | ✅             |
| `/api/users/profile/`       | **PUT**    | Update the logged-in user’s profile           | ✅             |
| `/api/tasks/`               | **GET**    | Get all tasks for the logged-in user          | ✅             |
| `/api/tasks/`               | **POST**   | Create a new task                             | ✅             |
| `/api/tasks/<id>/`          | **GET**    | Retrieve details of a specific task by ID     | ✅             |
| `/api/tasks/<id>/`          | **PUT**    | Update an existing task                       | ✅             |
| `/api/tasks/<id>/`          | **DELETE** | Delete a task by ID                           | ✅             |
| `/api/tasks/<id>/complete/` | **PATCH**  | Mark a task as completed                      | ✅             |
| `/api/tasks/streaks/`       | **GET**    | View current streak and task completion stats | ✅             |
| `/api/reminders/`           | **POST**   | Create a reminder for a task                  | ✅             |
| `/api/reminders/`           | **GET**    | Get all reminders for the logged-in user      | ✅             |
| `/api/calendar/sync/`       | **POST**   | Sync tasks with external calendar (optional)  | ✅             |


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

# To-Do List Backend — ALX Capstone

Backend API for a To-Do List application with reminders and streak tracking.

## Features
- User registration/login (JWT)
- Task CRUD, filtering, search, ordering
- Set reminders (Celery + Redis)
- Streak tracking on task completion
- Swagger API docs
- Docker / Docker Compose for reproducible environment
- Tests for auth and tasks

## Quickstart (local, SQLite)
1. Create venv:
   $ python -m venv venv
   $ source venv/bin/activate
2. Install:
   $ pip install -r requirements.txt
3. Copy `.env.example` -> `.env` and set values
4. Migrate and create superuser:
   $ python manage.py makemigrations
   $ python manage.py migrate
   $ python manage.py createsuperuser
5. Run server:
   $ python manage.py runserver
6. Open:
   - Swagger: http://127.0.0.1:8000/swagger/
   - API root: http://127.0.0.1:8000/

## Docker (Postgres + Redis)
1. Copy `.env.example` -> `.env` and set `DATABASE_URL=postgres://postgres:postgres@db:5432/todo_db`
2. Build & run:
   $ docker compose up --build
3. Migrate:
   $ docker compose exec web python manage.py migrate
4. Create superuser:
   $ docker compose exec web python manage.py createsuperuser

## API Endpoints (summary)
- POST /api/users/register/
- POST /api/users/login/
- POST /api/users/token/refresh/
- GET/PUT /api/users/me/
- GET/POST /api/tasks/
- GET/PUT/PATCH/DELETE /api/tasks/{id}/
- PATCH /api/tasks/{id}/complete/
- GET /api/tasks/streak/
- Swagger: /swagger/

## Tests
Run:
$ python manage.py test
(or with Docker: docker compose exec web python manage.py test)

## Notes
- Reminder delivery uses Celery; configure SMTP or push service for real notifications.
- Calendar sync endpoints are left as scaffold for OAuth integration.



This project is part of the ALX Backend Capstone Project, focusing on building real-world backend applications from scratch. It’s designed to be extendable and production-ready.
