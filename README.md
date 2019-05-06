Coding Challenge
===================

The project runs with Python 3.7 and postgresql

Installation
----------------
Clonce the repository using ``$ git clone git@github.com:ernestjumbe/cobiro-test.git``
To install clone the repository and cd into the the  ``cobiro-test`` directory.

Create a virtual envirnment with the command:
```sh
$ virtualenv -p python3 ~/.Virtualenv/cobirotestenv
```
and start the virtual environment using:
```sh
$ source ~/.Virtualenv/cobirotestenv/bin/activate
```
To install project requirements:
```sh
$ pip install requirements.txt
```
The application is setup to run using a json file. For the application to run with a json save the file in the root diretory of the project and ensure the project settings point to the given file in ``cobiro/settings/base.py`` under the settings:
```
DATA_SOURCE = 'json_file'

DATA_SOURCE_FILE = os.path.join(BASE_DIR, 'file_name' + "." + 'json')
```
where ``file_name`` is the name of the file without the file extension.

In order to use a database with the project change the setting to ``db``
```
DATA_SOURCE = 'db'
```
and create a postgres database
```sh
$ psql createdb databasename
```
and change the the database settings in
 ``cobiro/settings/local.py``
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'databasename',
        'PORT': 5432,
        'HOST': 'localhost',
        'USER': 'your_database_username',
    }
}
```
To set up database run:
```sh
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Create an admin account.
```sh
$ ./manage.py createsuperuser
```

To populate the database the management command ``import_stores`` may be used ie:
```sh
$ ./manage.py import_stores your_json_file.json
```
Where ``your_json_file.json`` is the path to the json file you would like to use to populate the database.
Running the application
----------------
To run the application:
```sh
$ ./manage.py runserver_plus
```
The application will be accessible at: http://127.0.0.1:8000/api/stores/
The admin of the application will be accessible at: http://127.0.0.1:8000/admin/ if the credentials have been created.

Additional information
----------------
When using the json file, to access the products of a store with the name ``Some Store name`` replace the spaces in the store name with underscores to create a slug i.e.: ``http://127.0.0.1:8000/api/stores/Some_Store_name/``.
In the case of using the database the slug is replace with the store id ie: ``http://127.0.0.1:8000/api/stores/644/``.
To create a store make a post request to ``http://127.0.0.1:8000/api/stores/`` with the data:
```
{
        "store_name": "Some Store name"
}
```
To create a product in a store store make a post request to ``http://127.0.0.1:8000/api/stores/{slug_or_id}`` with the data:
```
{
        "title": "Product title",
        "link": "https://example.local",
        "description": "Product description."
        "image_link": "https://example.local/img/product_image.png"
}
```
Using slug or id will depend on whether the project is running using the database or a jso file.
