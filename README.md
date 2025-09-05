One-Click Testimonial Wall (Django starter)

What this repo contains
- Minimal Django project with a testimonials app
- Public submission form: /t/<slug>/submit
- Public wall (embeddable): /t/<slug>/wall
- Embed script: /embed/<slug>.js (injects an iframe)
- Django Admin to moderate testimonials

One-minute local run (Windows PowerShell)
1) Create and activate a virtualenv (recommended):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2) Install dependencies:
   pip install -r testimonial_wall\requirements.txt

3) Migrate and seed demo data:
   cd testimonial_wall
   python manage.py migrate
   python manage.py seed_demo
   # A demo superuser 'demo' with password 'demo1234' and a Project with slug 'demo' will be created

4) Run the dev server:
   python manage.py runserver

5) Test endpoints immediately:
   - Health:     http://127.0.0.1:8000/healthz
   - Submit:     http://127.0.0.1:8000/t/demo/submit
   - Wall:       http://127.0.0.1:8000/t/demo/wall
   - Embed JS:   http://127.0.0.1:8000/embed/demo.js
   - Admin:      http://127.0.0.1:8000/admin  (login as demo/demo1234)

Notes
- This is an MVP starter (SQLite, DEBUG on). For production, set env vars, use Postgres, and configure storage for media.
- Approve testimonials via Admin (set status to approved). Approved items will appear on the wall.
- You can embed the wall with:
  <script async src="https://yourdomain.com/embed/<slug>.js"></script>
