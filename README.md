# PKD Mart

A Django product inventory management application. It provides a dashboard, product listing and search, product create/edit/delete workflows, low-stock indicators, and Django's built-in administration site.

## Requirements

- Python compatible with Django 6.1.2 (the project has been run with Python 3.13)
- pip
- Internet access to load the Bootstrap stylesheet and JavaScript from jsDelivr

## Setup on Windows

Run these commands from the project directory in PowerShell:

```powershell
py -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and sign in with the superuser credentials created above. The same account can access the Django admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

If PowerShell blocks virtual-environment activation, run the commands using `./.venv/Scripts/python.exe` instead of activating it, for example:

```powershell
./.venv/Scripts/python.exe -m pip install -r requirements.txt
./.venv/Scripts/python.exe manage.py migrate
./.venv/Scripts/python.exe manage.py createsuperuser
./.venv/Scripts/python.exe manage.py runserver
```

## Main URLs

- `/` - Sign-in page
- `/dashboard/` - Inventory summary
- `/products/` - Product list, filters, and actions
- `/products/add/` - Add a product
- `/admin/` - Django administration, including category management

Create product categories in `/admin/` before adding products. Public account registration is not enabled; create accounts through Django admin or the `createsuperuser` command.

## Tests and checks

```powershell
python manage.py check
python manage.py test
```

## Development notes

The project uses SQLite by default. The database and uploaded product images are local data and are excluded from Git by `.gitignore`. Static source files under `static/` are application assets and should remain tracked.

The settings currently contain a development `SECRET_KEY` and have `DEBUG = True`. Before deployment, use a private environment-provided secret key, disable debug mode, configure allowed hosts, and review Django's deployment checklist.