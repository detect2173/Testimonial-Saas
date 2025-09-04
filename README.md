One-Click Testimonial Wall (Django starter)

What this repo contains
- Minimal Django project with a testimonials app
- Public submission form: /t/<slug>/submit
- Public wall (embeddable): /t/<slug>/wall
- Embed script: /embed/<slug>.js (injects an iframe)
- Django Admin to moderate testimonials

Quick start (Windows PowerShell)
1) Create and activate a virtualenv (recommended):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2) Install dependencies:
   pip install -r testimonial_wall\requirements.txt

3) Run migrations and create a superuser:
   cd testimonial_wall
   python manage.py migrate
   python manage.py createsuperuser

4) Run the dev server:
   python manage.py runserver

5) In Django Admin (http://127.0.0.1:8000/admin/), create a Project with a unique slug and yourself as owner. Optionally create a WallConfig for it.

6) Test the public endpoints (replace my-slug):
   - Submit form: http://127.0.0.1:8000/t/my-slug/submit
   - Wall:       http://127.0.0.1:8000/t/my-slug/wall
   - Embed JS:   http://127.0.0.1:8000/embed/my-slug.js

Notes
- This is an MVP starter (SQLite, DEBUG on). For production, set env vars, use Postgres, and configure storage for media.
- Approve testimonials via Admin (set status to approved). Approved items will appear on the wall.
- You can embed the wall with:
  <script async src="https://yourdomain.com/embed/<slug>.js"></script>
