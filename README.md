## How to run

1. ### All nginx(:80) + mysql(:3306) + flask(:5000)

   ```shell
   $ docker-compose up -d
   ```

2. ### Only flask(:5000)

   2.1 first time only

     ```shell
     app$ python3 -m venv venv
     app$ source venv/bin/activate
     (venv) app$ pip install --upgrade pip
     (venv) app$ pip install -r requirements.txt
     (venv) app$ python manage.py db init
     (venv) app$ python manage.py db migrate
     (venv) app$ python manage.py db upgrade
     (venv) app$ python app.py
     ```

   2.2 from the second

     ```shell
     app$ source venv/bin/activate
     (venv) app$ python app.py
     ```


The app code refer to the https://bit.ly/2EMHZ6o code.

## How to test
   http://localhost/note
   ```shell
   $ curl -i -X GET http://localhost/api
   $ curl -i -X GET http://localhost/api/2
   $ curl -i -X POST -H "Content-Type: application/json" -d '{"title": "test", "content": "test123"}' http://localhost/api
   $ curl -i -X PUT -H "Content-Type: application/json" -d '{"title": "test", "content": "test123"}' http://localhost/api/3
   $ curl -i -X DELETE http://localhost/api/4
   ```

![swagger_ui](swagger_ui.png)
