# Discusso

## Quick Start

Use this only if initial setup is done.

1. Step 1 (see below)
2. Step 2 (see below)
3. Step 7 (see below)
4. Step 8 (see below)

## Initial Setup

1. Open another terminal
2. Create a virtual environment

   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment

   ```bash
   source .venv/bin/activate
   ```

4. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Make migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser

   ```bash
   python manage.py createsuperuser
   ```

7. Run the server

   ```bash
   python manage.py runserver
   ```

8. Open the browser and go to http://127.0.0.1:8000/
