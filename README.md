```markdown
# ResumePulse AI

An AI-powered Resume Analyzer that compares resumes with job descriptions, generates match scores, extracts missing skills, and provides AI-driven improvement suggestions using Gemini.

This repository contains a full-stack implementation featuring a Django REST Framework backend and a modern React (Vite) frontend.

---

## Current status

- **Django Backend:** Complete with REST API endpoints, JWT authentication, PostgreSQL database integration, and local file parsing (PDF/DOCX).
- **NLP & AI Engine:** Implemented keyword extraction and match scoring via TF-IDF cosine similarity, alongside dynamic, context-aware suggestions powered by the Google Gemini API.
- **React Frontend:** Built an interactive, responsive user interface using Tailwind CSS, React Router, Axios, and visual analytics dashboards backed by Recharts.
- **Testing:** Comprehensive test suite execution across backend endpoints (authentication, uploads, and CRUD operations) alongside integrated frontend verification.

---

## Tech stack

### Frontend
- React 18 (Vite)
- TypeScript
- Tailwind CSS
- React Router DOM
- Recharts (for data visualization)
- Axios

### Backend
- Python 3
- Django 6.0.6
- Django REST Framework
- PostgreSQL
- `scikit-learn` (for TF-IDF and Cosine Similarity)
- `djangorestframework-simplejwt` (JWT Auth)
- `django-cors-headers` (CORS handling)
- `PyMuPDF` (fitz) & `python-docx` (for file parsing)
- `google-generativeai` (Gemini API Integration)

---

## Repository structure

```text
ResumePulseAI/
│
├── backend/
│   ├── config/          — Django settings and project configuration
│   ├── accounts/        — Authentication app
│   ├── jobs/            — Job description management app
│   ├── resumes/         — Resume processing app
│   ├── reports/         — AI analysis reports app
│   ├── manage.py        — Django management utility
│   └── requirements.txt — Python dependencies
│
└── frontend/
    ├── src/
    │   ├── components/  — Reusable UI elements (Charts, Layouts)
    │   ├── pages/       — Dashboard, Report view, History, Auth pages
    │   ├── services/    — API connection layer (Axios)
    │   └── App.tsx      — Core application routing
    ├── package.json
    └── vite.config.ts

```
## Backend API endpoints
### 🔐 Auth
 * POST /api/auth/register/ — register a new user
 * POST /api/auth/login/ — obtain JWT access and refresh tokens
 * POST /api/auth/refresh/ — refresh an access token
 * POST /api/auth/verify/ — verify a JWT token
 * GET /api/auth/me/ — retrieve authenticated user profile
### 📄 Resumes & Management
 * POST /api/resumes/upload/ — upload a resume file (authenticated users only)
 * GET /api/resumes/ — list uploaded resumes for the authenticated user
 * GET /api/resumes/<id>/ — retrieve a single uploaded resume
### 📌 Jobs
 * GET /api/jobs/ — list job descriptions
 * POST /api/jobs/ — create a job description
 * GET /api/jobs/<id>/ — retrieve a job description
 * PATCH /api/jobs/<id>/ — update a job description
 * DELETE /api/jobs/<id>/ — delete a job description
### 📊 Reports & Analysis
 * POST /api/resumes/analyze/ — trigger hybrid NLP & Gemini analysis
 * GET /api/reports/ — list analysis reports for the authenticated user (with pagination)
 * GET /api/reports/<id>/ — retrieve a single analysis report
 * DELETE /api/resumes/reports/<id>/delete/ — delete a generated analysis report
### File constraints
 * Accepts .pdf and .docx files only
 * Requires a valid JWT access token for all resume, job, and report routes
## Setup & Installation
### 1. Backend Setup
 1. Open a terminal and navigate to the backend folder:
```bash
cd backend

```
 2. Create and activate a virtual environment:
```bash
python -m venv venv

```
 * **Windows:** venv\Scripts\activate
 * **Linux/macOS:** source venv/bin/activate
 3. Install the required dependencies:
```bash
pip install -r requirements.txt

```
 4. Create a .env file in the backend/ directory with the following variables:
```env
SECRET_KEY=your_django_secret_key
DEBUG=True

# Database settings
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Third-Party API Keys
GOOGLE_API_KEY=your_gemini_api_key

```
 5. Apply database migrations and create an admin user:
```bash
python manage.py migrate
python manage.py createsuperuser

```
 6. Start the backend development server:
```bash
python manage.py runserver

```
### 2. Frontend Setup
 1. Open a new terminal window and navigate to the frontend folder:
```bash
cd frontend

```
 2. Install the frontend dependencies:
```bash
npm install

```
 3. Create a .env file in the frontend/ directory:
```env
VITE_API_BASE_URL=http://localhost:8000/api

```
 4. Start the Vite development application:
```bash
npm run dev

```
## Testing
### Backend tests
To run the built-in Django API test configurations (including authentication flows, document parsing, and analysis routes):
```bash
python manage.py test

```
### Frontend verification
Tested utilizing targeted integration routines tracking Axios response management, route shielding for private dashboards, and seamless fallback state handling during Gemini free-tier quota limitations.
## Future Improvements
 * 🚀 Deploy frontend to Vercel/Netlify and backend to AWS/Render.
 * 📊 Build historical progress tracking to map keyword improvements over time.
 * 👥 Implement multi-user collaboration roles and shareable report configurations.
## 👨‍💻 Author
Built with 💻 by **Bhanu Teja**
```

```
