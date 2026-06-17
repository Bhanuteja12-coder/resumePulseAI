# ResumePulse AI Backend

This backend provides a Django REST API for resume upload, job descriptions, and analysis reports.

## New Report API Endpoints

- `GET /api/reports/` — list authenticated user's analysis reports with pagination
- `GET /api/reports/<id>/` — retrieve a single analysis report

## Behavior

- Only reports belonging to the authenticated user's resumes are returned
- Report list is paginated with `page_size` up to 50
- Each analysis report includes:
  - `resume` (ID)
  - `job_description` (nested object)
  - `match_score`
  - `match_percent`
  - `gap_analysis`
  - `ai_suggestions`
  - `created_at`

## Cleanup

Temporary Gemini helper scripts used during API debugging have been removed to keep the repository clean.
