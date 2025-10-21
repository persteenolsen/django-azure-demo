

# Python + Django + MySQL + Models + Azure App Service

This example shows how to use Django 5 on Azure App Service

Last updated: 21-10-2025

## Demo at Azure

https://pso-django-demo.azurewebsites.net

## Installing

- Download Python from the official website [Python](https://python.org/)
- Make sure that you have installed Python by the command in Powershell: "python --version"
- Download the Python extension for Visual Studio Code which automatically include the Pylance extionsion
- Download / fork this Django Starter Website from my GitHub
- Create the virtual environment ".venv" for the Django Web App by Powershell or by VS Code
- Virtual Environment by VS Code: "View - Command Palette - Python Create Environment"

## Install with Python commands by Powershell locally at Windows 10

- python -m venv .venv

- cd .venv

- Scripts/activate

- Copy requirements.txt to .venv

- (.venv) pip install -r requirements.txt

- (.venv) pip freeze > requirements.txt

- (.venv) cd ../

- (.venv) python manage.py runserver

When starting the Django Website from the Virtual Enviroment (.venv) you will notice that Django 5.1.11 will start. Otherwise you can use the Global Django if you have one installed by running:

- python manage.py runserver

## How it Works

Our Django application, `example` is configured as an installed application in `mysite/settings.py`:

```bash
# mysite/settings.py
INSTALLED_APPS = [
    # ...
    'example',
]
```

We allow all subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```bash
# mysite/settings.py
ALLOWED_HOSTS = ['*']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```bash
# mysite/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `mysite.wsgi` module:

```bash
# mysite/settings.py
WSGI_APPLICATION = 'mysite.wsgi.app'
```

This Django example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on PythonAnywhere

## Routing 

There are severals views in `example/views.py` which load HTML Django Templates `templates`:

The views are exposed a URL through `example/urls.py`:

```bash
# example/urls.py
from django.urls import path

from example.views import index
from example.views import about
from example.views import me

urlpatterns = [
    path('', index),
    path('about', about),
    path('me', me),
]
```
Finally, it's made accessible to the Django server inside `mysite/urls.py`:

```bash
# mysite/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

## Templates

To use templates create the dir 'templates' at root level and put the HTML files there

There is only one Django App in the Project and the dir 'templates' can be at root level

Tell Django where to look for Templates by `example/settings.py`:

Find the section TEMPLATES = [] and add the dir of the Templates

'DIRS': [BASE_DIR / 'templates']

## Running Locally

```bash
python manage.py runserver
```
Your Django application is now available at `http://127.0.0.1:8000/`.

## The Admin Backend and Databases

The Admin Backend is using a MySQL Database at Azure for Production, but is able to use a SQLite for Production as well

To connect to the MySQL use "mysqlclient" installed at Azure or install the Python package "pymysql" and the packages from the requirements.txt if you are using a virtual invironment at Azure 

```bash
pip install -r requirements.txt
```

If using "pymysql" take a look at the files needed for connecting to MySQL: `mysite/mysql_setup.py` and 

`mysite/__init__.py`

Create a Super User for the Admin Backend in the MySQL or SQLite

```bash
python manage.py createsuperuser
```

Make the Migration to the MySQL or SQLite 

```bash
python manage.py makemigrations
python manage.py migrate
```
You will need to do the Migration at first and when / if you will add, update or delete models.py which this Django Web App does not use

For using a SQLite developing / locally make the config in the setting file `mysite/settings.py`

Find the section DATABASES = {} and add support for SQLite and comment out the MySQL

## Static files for the Frontend

There is only one Django App in the Project and the dir 'static' and 'assets' can be created at root level

Make sure that the Python package 'whitenoise' is installed from the requirements.txt if you are using a virtual invironment at Azure

Note: Make sure you have the line 'whitenoise.middleware.WhiteNoiseMiddleware' in the 

MIDDLEWARE = [] at the `mysite/settings.py` along with the other packages

Finally, take a look at `mysite/settings.py`:

Find where Django now looks for the static files

STATIC_URL = 'static/'

Where you put your static files in the dir 'static'

STATIC_ROOT = BASE_DIR/'static' 

## Additional directory from which to load static files if wanted

The files in the dir 'asset' will be copied to the dir 'static' after running

```bash
python manage.py collectstatic
```

Note: The above command may not be needed as this Starter dont have a Django Admin backend

## Check that Django is serving static files by URL

Type the URL in your Browser after deployment to Vercel

https:// your project at Azure/static/pso-django.jpg

or the URL when running locally

`http://127.0.0.1:8000/static/pso-django.jpg`

If everything is fine my photo will be displayed

The CSS files can be tested the same way like the .jpg above

Now you can use the images and CSS in your Templates

## Running Locally and take a look at the Website

```bash
python manage.py runserver
```

The Django application is now available at `http://127.0.0.1:8000`

## Deployment to Azure

Make sure that your static files are ready by running

```bash
python manage.py collectstatic
```

Note: The above command may not be needed as this Starter dont have a Django Admin backend

Make sure to set Debug = False in the file `mysite/settings.py`

Copy your local files to Azure

## Models

Add the simple Model "Post" to be administrated by the Admin Backend and displayed by the Frontend.

- Create a file `example/models.py` with your new Model Post

- Make a regitration of your Model in `example/admin.py`

- Create the View for handling the Posts `example/views.py`

- Add the view / template blog in `example/urls.py`

- Create a Template for display the Posts `templates/blog.html`

- Create a folder with the path: `example/migrations` and run the command:

```bash
python manage.py makemigrations example
```
Note: It is important to add the name of the app in the command `example` !!!

This command will create a file for the migration of the Model to a Table in the SQLite or MySQL DB

- Now run the command: 

```bash
python manage.py migrate
```
This will create the Table Post in the DB and you are now ready for administrate the Posts by the Django Admin Backend

Happy use of Django :-)
