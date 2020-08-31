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
     (venv) app$ pip install -r requirements.txt
     (venv) app$ python app.py
     ```

   2.2 from the second

     ```shell
     app$ source venv/bin/activate
     (venv) app$ python app.py
     ```


The app code refer to the https://bit.ly/2EMHZ6o code.
