#  Django Ecommerce Project

This is a simple **Django-based Ecommerce Application** with Docker support.  
It includes product pages, templates, static files, and Django Admin for management.

---

## Requirements

- Python 3.8+  
- pip (Python package manager)  
- Virtualenv (recommended)  
- Docker & Docker Compose (for containerized setup)  

---

##  Run Locally (without Docker)

1. **Clone the repository**
   ```bash
   clone the project
   cd ecommerce_project
   ```

2. **Create & activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   App will be available at:  `http://127.0.0.1:8000`

---

##  Run with Docker

1. **Build and start containers**
   ```bash
   docker compose up --build -d
   ```

2. **Run migrations inside container**
   ```bash
   docker compose exec web python manage.py migrate
   ```

3. **Create superuser inside container**
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

4. **Collect static files**
   ```bash
   docker compose exec web python manage.py collectstatic --noinput
   ```

5. **Access the app**
   - Ecommerce site: `http://localhost:8000`
   - Admin panel:  `http://localhost:8000/admin`

---

##  Project Structure

```
ecommerce_project/
├── store/                # Django app (templates, static, views, models)
│   ├── templates/store/   # HTML templates
│   ├── static/store/      # CSS, JS, images
│   └── models.py          # Database models
├── ecommerce_project/     # Main project settings
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # Docker Compose config
├── Dockerfile             # Web container build
└── README.md              # Documentation
```

---

## Useful Commands

**Local:**
```bash
python manage.py runserver
```

**Docker:**
```bash
docker compose up -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

---

##  Features

- Django MVT architecture  
- Admin panel for product management  
- Static files & templates  
- Run locally or with Docker  

---

