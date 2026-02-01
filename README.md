# Playto Community Feed Backend

This project is a Django REST API built as part of the Playto internship task.
It provides a backend system for a community feed with posts, nested comments, and a leaderboard.

---

## 📌 Description

The application allows users to create posts and comments.
Comments support replies (nested comments).
An API endpoint is provided to fetch posts with their nested comments and another endpoint for leaderboard data.

The Django admin panel is used to manage users, posts, and comments.

---

## 🚀 Features

- Django REST Framework based API
- Admin panel for managing data
- Community posts
- Nested comments (replies to comments)
- Leaderboard API endpoint
- Clean and simple backend structure

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default database)

---

## ▶️ How to Run the Project

1. Activate virtual environment  
2. Run database migrations:
   ```bash
   python manage.py migrate


Start the development server:

python manage.py runserver


Open the browser:

Admin Panel: http://127.0.0.1:8000/admin/

Posts API: http://127.0.0.1:8000/api/posts/

📡 API Endpoints

/admin/ → Django admin panel

/api/posts/ → List posts with nested comments

/api/leaderboard/ → Leaderboard data