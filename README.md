

```md
# ResumePulse AI 🚀

An AI-driven career intelligence platform that analyzes resumes, predicts job compatibility, identifies skill gaps, and generates personalized improvement strategies.

ResumePulse AI helps candidates understand how well their resume matches a job description and provides actionable AI-powered recommendations to improve their chances.

---

## ✨ Features

### Resume Intelligence
- Upload PDF/DOCX resumes
- Extract resume text automatically
- Parse skills and experience information
- Analyze resume quality

### Job Match Analysis
- Compare resume with job description
- Generate compatibility score
- Analyze:
  - Skills match
  - Experience match
  - Keyword match

### AI Career Assistant
- Gemini API powered suggestions
- Personalized resume improvement tips
- Skill gap recommendations
- Role-specific guidance

### User Dashboard
- Secure authentication
- Resume history
- Previous analysis reports
- Track improvement over time

---

# 🛠 Tech Stack

## Frontend
- React.js
- Axios
- React Router
- Tailwind CSS

## Backend
- Python
- Django
- Django REST Framework

## Database
- PostgreSQL

## Authentication
- JWT Authentication

## AI / NLP
- Google Gemini API
- TF-IDF
- Cosine Similarity

## Resume Processing
- PyMuPDF (PDF extraction)
- python-docx (DOCX extraction)

---

# 📂 Project Structure

```

ResumePulseAI/

│
├── backend/
│
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │
│   ├── accounts/
│   │   └── Authentication system
│   │
│   ├── resumes/
│   │   └── Resume upload & parsing
│   │
│   ├── jobs/
│   │   └── Job description management
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── React application
│
└── README.md

````

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone <repository-url>

cd ResumePulseAI
````

---

# Backend Setup

Go to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv ven
```

Activate:

### Windows

```bash
ven\Scripts\activate
```

### Linux/Mac

```bash
source ven/bin/activate
```

---

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` inside backend folder:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=resumepulse_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

GEMINI_API_KEY=your_api_key
```

---

# Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE resumepulse_db;
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

---

# Run Backend

```bash
python manage.py runserver
```

Backend runs:

```
http://127.0.0.1:8000/
```

---

# Frontend Setup

Go to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Run:

```bash
npm run dev
```

Frontend runs:

```
http://localhost:5173/
```

---

# 🔐 API Features

## Authentication

Register user

```
POST /api/auth/register/
```

Login

```
POST /api/auth/login/
```

Refresh token

```
POST /api/auth/token/refresh/
```

---

## Resume API

Upload resume:

```
POST /api/resumes/upload/
```

Get resumes:

```
GET /api/resumes/
```

---

## Job Description API

Create job:

```
POST /api/jobs/
```

Get jobs:

```
GET /api/jobs/
```

---

# 📊 Matching Algorithm

ResumePulse AI uses:

## TF-IDF

Converts resume and job description text into numerical vectors.

## Cosine Similarity

Calculates similarity between resume and job description.

Output:

```
Overall Match Score: 85%

Skills Match: 90%
Experience Match: 80%
Keyword Match: 85%
```

---

# 🗓 Development Roadmap

## Week 1

✅ Django setup
✅ PostgreSQL connection
✅ JWT authentication
✅ Resume upload
✅ PDF/DOCX parsing
✅ Job description CRUD

## Week 2

⬜ NLP skill extraction
⬜ Match scoring engine
⬜ Analysis API
⬜ Report generation

## Week 3

⬜ Gemini AI integration
⬜ AI suggestions
⬜ React dashboard

## Week 4

⬜ Deployment
⬜ Testing
⬜ Optimization

---

# 🤝 Contribution

Contributions, issues, and suggestions are welcome.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Built with ❤️ using Django, React, PostgreSQL, and AI.

```
