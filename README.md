# Django Starter Template App with db-file-store, Whitenoise & Deployment to Vercel

1. [Contents](#contents)
3. [How to Use](#how-to-use)

## Contents

This pmp contains a start Django project with Whitenoise, db-file-store(https://github.com/shortxmas/db_file_store) and deployment to Vercel

## How to Use

1. Make sure you have python installed
2. Run ```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'``` to generate a project secret_key to use in settings.py
3. Run ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` 
4. Run ```python manage.py runserver``` or ```python3 manage.py runserver``` to start the app locally
5. Deploy the app on Vercel by deploying the repository

- Environment variables can be defined in a .env file in vercel_app and used in settings.py with os.getenv('ENV KEY')

