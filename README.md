# ResumePulse AI

A Django backend prototype for a resume and job matching platform.

This repository currently contains a Django REST Framework backend scaffold with working authentication and resume upload endpoints. The `frontend/` directory is present but empty and does not yet contain a web application.

## Current status

- Django backend scaffold built
- `accounts` and `resumes` apps implemented with REST endpoints
- Resume uploads now extract raw text from PDF and DOCX files and store it in the database
- `resumes` exposes authenticated GET endpoints for list/detail retrieval of uploaded resumes
- `jobs` app now exposes CRUD API endpoints
- Admin interface available at `/admin/`
- Auth, resume, and job APIs tested successfully
- No frontend app has been implemented yet

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
  - `accounts/` — authentication app
  - `jobs/` — job description management app scaffold
  - `manage.py` — Django management utility
  - `requirements.txt` — Python dependencies
- `frontend/` — currently empty placeholder
- `resumes/` — resume upload app package used by the backend
- `README.md` — this file

## Backend API endpoints

- `POST /api/auth/register/` — register a new user
- `POST /api/auth/login/` — obtain JWT access and refresh tokens
- `POST /api/auth/refresh/` — refresh an access token
- `POST /api/auth/verify/` — verify a JWT token
- `GET /api/auth/me/` — retrieve authenticated user profile
- `POST /api/resumes/upload/` — upload a resume file (authenticated users only)
- `GET /api/resumes/` — list uploaded resumes for the authenticated user
- `GET /api/resumes/<id>/` — retrieve a single uploaded resume
- `GET /api/reports/` — list analysis reports for the authenticated user, with pagination
- `GET /api/reports/<id>/` — retrieve a single analysis report
- `GET /api/jobs/` — list job descriptions
- `POST /api/jobs/` — create a job description
- `GET /api/jobs/<id>/` — retrieve a job description
- `PATCH /api/jobs/<id>/` — update a job description
- `DELETE /api/jobs/<id>/` — delete a job description

### Resume upload constraints

- Accepts `.pdf` and `.docx` files only
- Requires a valid JWT access token for resume routes

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

## Testing

The backend currently includes API tests for authentication, resume upload, resume retrieval, and job CRUD. Run:

```bash
python manage.py test
```

At the time of this update, the backend test suite ran successfully with 11 passing tests.

## Notes

- `config/settings.py` currently loads `.env` for database configuration but the `SECRET_KEY` is hardcoded in settings.
- `jobs` app is present but does not expose API routes yet.
- `frontend/` remains a placeholder with no implementation.

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
- PyMuPDF==1.25.0
- python-docx==0.8.12
- sqlparse==0.5.5
- tzdata==2026.2
