

# Python + Django + MySQL + Azure App Service

This example shows how to use Django 5 on Azure App Service

Last updated: 22-10-2025

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

When starting the Django Website from the Virtual Enviroment (.venv) you will notice that latest Django will start. Otherwise you can use the Global Django if you have one installed by running:

- python manage.py runserver

## How it Works

The Django application, `hello_azure` is configured as an installed application in `quickstartproject/settings.py`:

```bash
# quickstartproject/settings.py
INSTALLED_APPS = [
    # ...
    'hello_azure',
]
```

We allow the Domain at Azure in production in `ALLOWED_HOSTS`, in addition to 127.0.0.1 locally:

```bash
# quickstartproject/settings.py
ALLOWED_HOSTS = ['']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```bash
# quickstartproject/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `quickstartproject.wsgi` module:

```bash
# quickstartproject/settings.py
WSGI_APPLICATION = 'quickstartproject.wsgi.app'
```

This Django example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Azure

## Routing 

There are severals views in `hello_azure/views.py` which load HTML Django Templates `templates`:

The views are exposed a URL through `hello_azure/urls.py`:

```bash
# hello_azure/urls.py
from django.urls import path

from hello_azure.views import index
urlpatterns = [
    path('', index),
]
```
Finally, it's made accessible to the Django server inside `quickstartproject/urls.py`:

```bash
# quickstartproject/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('hello_azure.urls')),
]
```

## Templates

To use templates create the dir 'templates' at root level and put the HTML files there

There is only one Django App in the Project and the dir 'templates' can be at root level

Tell Django where to look for Templates by `quickstartproject/settings.py`:

Find the section TEMPLATES = [] and add the dir of the Templates

'DIRS': [BASE_DIR / 'templates']

## Running Locally

```bash
python manage.py runserver
```
Your Django application is now available at `http://127.0.0.1:8000/`.

## The Admin Backend and Databases

The Admin Backend is using a remote MySQL Database for both Production and Developement, and is able to use a SQLite for Developement as well

To connect to the MySQL use "pymysql" installed and the packages from the requirements.txt when using a virtual invironment locally. At Azure everything will happen by DevOps 

```bash
pip install -r requirements.txt
```

For understad the "pymysql" take a look at the files needed for connecting to MySQL: `mysite/mysql_setup.py` and 

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
You will need to do the Migration at first and when / if you will add, update or delete models.py which this Django Web App does not use. 

For using a SQLite developing / locally make the config in the setting file `mysite/settings.py`

Find the section DATABASES = {} and add support for SQLite and comment out the MySQL

## Static files for the Frontend

There is only one Django App in the Project and the dir 'static' and 'assets' can be created at root level

Make sure that the Python package 'whitenoise' is installed from the requirements.txt if you are using a virtual invironment at Azure

Note: Make sure you have the line 'whitenoise.middleware.WhiteNoiseMiddleware' in the 

MIDDLEWARE = [] at the `quickstartproject/settings.py` along with the other packages

Finally, take a look at `quickstartproject/settings.py`:

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

Type the URL in your Browser after deployment to Azure

https:// your project at Azure/static/images/azure-icon.svg

or the URL when running locally

`http://127.0.0.1:8000/static/images/azure-icon.svg`

If everything is fine the Azure logo will be displayed

The CSS files can be tested the same way like the .svg above

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

Note: The above command will happen by DevOps at Azure App Service and the Django Admin backend should be ready

Make sure to set Debug = False in the file `quickstartproject/settings.py`

Make a commit to GitHub which will start GitHub Actions and the Website will be updated

Happy use of Django :-)
