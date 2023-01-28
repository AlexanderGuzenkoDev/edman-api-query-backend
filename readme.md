# Description

This project is the backend code for tagging recipes from the Edman API. You can read [more info](https://developer.edamam.com/edamam-docs-recipe-api) about the Edman API.

### Setting configurations

You can set configurations in the file named 'settings.py' in the folder 'edman_api_backend'.

You can set PostgreSQL as the database.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DATABASE_NAME',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOST',
        'PORT': 5432,
    }
}
```

You can set the client url for the CORS policy and the authentication.

```
CORS_ORIGIN_WHITELIST = [
     'YOUR_CLIENT_URL'
]
CSRF_TRUSTED_ORIGINS = ['YOUR_CLIENT_URL']
```

### Running the code

You can run the code following the commands in the root folder.

Install all packages related to your project.

```
pip install -r requirements.txt
```

Migrate all migrations.

```
python manage.py migrate
```

Create the super user to manage the database

```
python manage.py createsuperuser
```

Run the code

```
python manage.py runserver
```

# Building and Deploying the project

### Deploying the django project on Pythonanywhere

You can deploy the Django project on Pythonanywhere. You can learn [how to deploy Django projects on Pythonanywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

- Upload your source code to Git and import that in Pythonanywhere
- Create a virtual env file and activate that
- Install all packages related to your project
- Create a new web app
- Set the configurations (e.g. virtual env file, project root folder)
- Change the settings
- Migrate all migrations
- Reload the web app
