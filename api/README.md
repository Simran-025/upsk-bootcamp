# Upsk Bootcamp - Team Collaboration API

This project is a FastAPI-based application designed to manage teams and users, allowing for efficient team collaboration and management.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete for both Users and Teams.
- **Association**: Easily link users to teams and manage team membership.
- **SQLite Integration**: Uses SQLAlchemy for lightweight, efficient database management.

## Installation

1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
Start the server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

Access the interactive API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints
- **Users**: `/users/` (POST, PUT, DELETE)
- **Teams**: `/teams/` (POST, PUT, DELETE, GET users)
