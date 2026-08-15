# Django Space

## About

Django Space is a small learning project built while studying Django. It recreates the "Alura Space" static layout — a gallery-style page showcasing space photos — as a Django app, using template inheritance (`base.html`), reusable partials (header, side menu, footer), and Django's static file handling.

The goal of this project is purely educational: practicing Django's URL routing, views, and template system (`{% extends %}`, `{% block %}`, `{% include %}`, `{% static %}`).

## Features

- Home page (`/`) listing a photo gallery
- Image detail page (`/imagem`)
- Shared layout via `base.html` with reusable partials for header, side menu, and footer

## Tech Stack

- Python 3
- Django 6.1
- SQLite (default database)
- python-dotenv (environment variable management)

## Project Structure

```
django-project/
├── gallery/          # Django app: views and URLs
├── setup/            # Project settings, root URL config
├── templates/
│   ├── gallery/       # base.html, index.html, imagem.html
│   └── partials/      # _header.html, _menu_lateral.html, _footer.html
├── static/            # CSS, images, icons
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/pedropcorsini/django-space.git
   cd django-space
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with a Django secret key
   ```bash
   SECRET_KEY=your-secret-key-here
   ```

5. Apply migrations
   ```bash
   python manage.py migrate
   ```

6. Run the development server
   ```bash
   python manage.py runserver
   ```

7. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

## Notes

`DEBUG` is currently set to `True` and `ALLOWED_HOSTS` is empty — this project is configured for local development only and is not production-ready.
