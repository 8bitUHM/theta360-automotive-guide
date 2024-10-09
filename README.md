# theta360 Automotive Guide Website

This is the theta 360 automotive guide website ported from the old site [here](https://automotive.theta360.guide/) to Django.
Old site repo found [here](https://github.com/theta-automotive/theta-automotive.github.io)

1. [Project Structure](#project-structure)
2. [Getting the app running](#getting-the-app-running)

## Project Structure

The project is organized into several components:

- **theta360-automotive-guide**: The main Django project directory.

  - **core/**: Main or 'host' app
    - **settings.py**: Configuration settings for the project, including database settings, middleware, installed apps, and other project-specific configurations. Models are defined here.
    - **urls.py**: URL configuration for the project, mapping URLs to views.
  - **db_file_storage/**: File storage systems that allows us to store files by raw bytes and mimetype in database.
  - **website/**: Website app
    - **migrations/**: Database migration files.
    - **static/**: Static files (CSS, JavaScript, images).
    - **templates/**: HTML templates.
    - **admin.py**: Admin interface configuration.
    - **forms.py**: HTML forms. Forms define how data is input and validated by the user.
    - **models.py**: Data models. Models define the structure of the database and interact with data.
    - **serializers.py**: Serializers for converting complex data types, such as querysets and model instances, to native Python datatypes that can then be easily rendered into JSON, XML, or other content types.
    - **tests.py**: Unit tests.
    - **urls.py**: URL configuration for the portal app, mapping URLs to views.
    - **views.py**: View functions or classes. Views handle HTTP requests and return HTTP responses.

  - **manage.py**: Django's command-line utility for administrative tasks.
  - **requirements.txt**: Txt file that holds all of the projects dependencies.

## Getting the app running


1. In a new terminal run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
2. in ./core folder, create a new file called local_settings.py and add

```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG=True

DATABASES = {
  "default":{
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}
```
3. In ./core folder, create a new file called .env and add the environment variables from our project discord channel theta-360

4. Cd into theme/static_src and run `npm install`

5. Start tailwind styling compilation by running `python manage.py tailwind start` or `python manage.py tailwind build` to build once

6. Collect all static files with `python manage.py collectstatic`

7. Update your local database by running `python manage.py migrate`

8. Start the app by running `python manage.py runserver` in terminal, the app should be running locally on port 8000, http://127.0.0.1:8000/


