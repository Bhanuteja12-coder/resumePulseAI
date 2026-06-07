# ResumePulse AI

A Django backend prototype for a resume and job matching platform.

This repository currently contains a Django REST Framework backend skeleton with placeholder apps for accounts, resumes, and jobs. The `frontend/` directory is present but empty and does not yet contain a web application.

## Current status

- Django backend scaffold built
- `accounts`, `resumes`, and `jobs` app skeletons present
- Admin interface available at `/admin/`
- No frontend app has been implemented yet
- No custom REST API routes are configured beyond Django admin at this time

## Tech stack

- Python 3
- Django 6.0.6
- Django REST Framework
- PostgreSQL
- JWT authentication support via `djangorestframework-simplejwt`
- CORS support via `django-cors-headers`

## Repository structure

- `backend/`
  - `config/` — Django settings and project configuration
  - `accounts/` — authentication app scaffold
  - `resumes/` — resume processing app scaffold
  - `jobs/` — job description management app scaffold
  - `manage.py` — Django management utility
  - `requirements.txt` — Python dependencies
- `frontend/` — currently empty placeholder
- `README.md` — this file

## Setup

1. Open a terminal and navigate to the repository root.
2. Change directory to the backend folder:
   ```bash
   cd backend
   ```
3. Create a virtual environment:
   ```bash
   python -m venv ven
   ```
4. Activate the virtual environment:
   - Windows:
     ```bash
     ven\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source ven/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Create a `.env` file in `backend/` with the following values:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True

   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
7. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
8. Create a Django superuser:
   ```bash
   python manage.py createsuperuser
   ```
9. Start the development server:
   ```bash
   python manage.py runserver
   ```
10. Open the admin interface at:
    ```text
    http://127.0.0.1:8000/admin/
    ```

## Notes

- `config/settings.py` currently loads `.env` for database configuration but the `SECRET_KEY` is hardcoded in settings.
- The repository currently has no frontend implementation in `frontend/`.
- The backend apps are scaffolded but do not yet expose custom API endpoints.

## Dependencies

The project uses the following backend dependencies from `backend/requirements.txt`:

- asgiref==3.11.1
- Django==6.0.6
- django-cors-headers==4.9.0
- djangorestframework==3.17.1
- djangorestframework_simplejwt==5.5.1
- psycopg2-binary==2.9.12
- PyJWT==2.13.0
- python-dotenv==1.2.2
- sqlparse==0.5.5
- tzdata==2026.2
