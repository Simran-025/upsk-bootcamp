# URL Shortener API

A robust URL shortening service built with FastAPI and SQLAlchemy.

## Features
- Shorten long URLs into unique short codes.
- Redirect users to the original URL via short code.
- Input validation to prevent malicious URL injection.

## Tech Stack
- **Framework:** FastAPI
- **Database:** SQLite (via SQLAlchemy)
- **Migrations:** Alembic

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Simran-025/upsk-bootcamp.git
   cd api
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   alembic upgrade head
   ```

5. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **View API documentation:**
   Visit http://127.0.0.1:8000/docs
